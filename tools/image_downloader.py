from collections.abc import Generator
import os
import requests
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ImageDownloaderTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # 获取图片 URL 参数
        image_url = tool_parameters.get("image_url", "")
        
        if not image_url:
            yield self.create_text_message("没有提供图片URL。")
            return
        
        try:
            # 下载图片
            image_data = self._download_image(image_url)
            
            # 从 URL 中提取文件名
            filename = image_url.split('/')[-1]
            
            # 检测文件扩展名，如果没有则默认为 jpg
            if '.' not in filename:
                filename += '.jpg'
            
            # 返回成功消息
            yield self.create_text_message(f"图片 '{filename}' 下载成功")
            
            # 返回图片数据作为 blob
            mime_type = self._get_mime_type(filename)
            yield self.create_blob_message(
                blob=image_data, 
                meta={
                    "mime_type": mime_type,
                    "filename": filename
                }
            )
        except Exception as e:
            yield self.create_text_message(f"下载图片时出错: {str(e)}")
    
    def _download_image(self, url: str) -> bytes:
        """从 URL 下载图片并返回二进制数据"""
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 确保请求成功
        return response.content
    
    def _get_mime_type(self, filename: str) -> str:
        """根据文件扩展名返回对应的 MIME 类型"""
        ext = filename.split('.')[-1].lower()
        mime_types = {
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'png': 'image/png',
            'gif': 'image/gif',
            'bmp': 'image/bmp',
            'webp': 'image/webp',
            'svg': 'image/svg+xml',
            'tiff': 'image/tiff',
            'ico': 'image/x-icon',
        }
        return mime_types.get(ext, 'application/octet-stream')
