# 图片下载器 (Image Downloader)

一个简单而高效的图片下载 Dify 插件，可以从 URL 下载图片并将其作为 blob 返回。

## 功能特点

- 支持从任何公开的 URL 下载图片
- 自动检测图片类型并设置正确的 MIME 类型
- 支持常见图片格式（JPG、PNG、GIF、BMP、WebP 等）
- 简单易用的接口

## 安装方式

1. 从 [Dify Marketplace](https://marketplace.dify.ai/plugins) 安装插件
2. 导航到 Dify 工作区中的**插件**部分
3. 找到"图片下载器"插件并点击"安装"
4. 安装完成后，你可以在应用程序中使用该插件

### 添加到应用程序

1. 创建或编辑一个 Chatflow 或 Workflow 应用
2. 在工具选择面板中，选择"图片下载器"工具
3. 根据需要在应用流程中配置工具
4. 保存并发布应用

## 使用方法

这个插件允许你通过提供图片 URL 来轻松下载图片。

### 参数

- `image_url`（必需）：要下载的图片的 URL

## 示例用法

```
提供图片 URL，插件将下载并返回图片。
URL: https://example.com/image.jpg
```

## 开发者信息

- **作者**: lzfxxx
- **版本**: 0.0.1
- **类型**: 工具插件

## 反馈和问题

如果你遇到任何问题或有建议，请在 [GitHub 仓库](https://github.com/lzfxxx/image-downloader) 提交 issue。



