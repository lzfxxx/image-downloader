from collections.abc import Generator
import os
import requests
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ImageDownloaderTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # Get image URL parameter
        image_url = tool_parameters.get("image_url", "")
        
        if not image_url:
            yield self.create_text_message("No image URL provided.")
            return
        
        try:
            # Download image
            image_data = self._download_image(image_url)
            
            # Extract filename from URL
            filename = image_url.split('/')[-1]
            
            # Check file extension, default to jpg if none
            if '.' not in filename:
                filename += '.jpg'
            
            # Return success message
            yield self.create_text_message(f"Image '{filename}' downloaded successfully")
            
            # Return image data as blob
            mime_type = self._get_mime_type(filename)
            yield self.create_blob_message(
                blob=image_data, 
                meta={
                    "mime_type": mime_type,
                    "filename": filename
                }
            )
        except Exception as e:
            yield self.create_text_message(f"Error downloading image: {str(e)}")
    
    def _download_image(self, url: str) -> bytes:
        """Download image from URL and return binary data"""
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Ensure request is successful
        return response.content
    
    def _get_mime_type(self, filename: str) -> str:
        """Return corresponding MIME type based on file extension"""
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
