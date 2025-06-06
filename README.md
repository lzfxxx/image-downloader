# Image Downloader

A simple and efficient image downloader Dify plugin that can download images from URLs and return them as blobs.

## Features

- Support downloading images from any public URL
- Automatically detect image types and set correct MIME types
- Support common image formats (JPG, PNG, GIF, BMP, WebP, etc.)
- Simple and easy-to-use interface
- Solves CSP issues in Dify cloud version (udify.app), allowing display of images from external domains

## Installation

1. Install the plugin from [Dify Marketplace](https://marketplace.dify.ai/plugins)
2. Navigate to the **Plugins** section in your Dify workspace
3. Find the "Image Downloader" plugin and click "Install"
4. Once installed, you can use the plugin in your applications

### Adding to Applications

1. Create or edit a Chatflow or Workflow application
2. In the tool selection panel, select the "Image Downloader" tool
3. Configure the tool in your application flow as needed
4. Save and publish your application

## Usage

This plugin allows you to easily download images by providing image URLs.

### Parameters

- `image_url` (required): The URL of the image to download

## Example Usage

Basic usage:
```
Provide an image URL, and the plugin will download and return the image.
URL: https://example.com/image.jpg
```

Real-world application scenario:

As shown in the image below, LLM outputs Markdown-formatted image links in responses, but due to CSP restrictions, these external images cannot be displayed directly. You can use the following code to extract image URLs from LLM responses, then download and display images through this plugin.

```python
import re
from typing import Dict

def main(text: str) -> Dict[str, str]:
    # Match Markdown image syntax: ![xxx](url)
    match = re.search(r'!\[.*?\]\((https?://[^\s)]+)\)', text)
    url = match.group(1) if match else ""

    # Remove image part
    text_without_image = re.sub(r'!\[.*?\]\((https?://[^\s)]+)\)', '', text)

    return {
        "text": text_without_image.strip(),
        "url": url
    }
```

The above code can be used as a Python runtime node in Dify Workflow. After extracting the image URL, pass it to the image downloader plugin to solve CSP restriction issues.

![Usage Example](usage_example.png)

## Problem Solved

This plugin solves the Content Security Policy (CSP) restriction issue in Dify cloud version (udify.app). When AI needs to display images from external domains, these images cannot be displayed by default due to CSP restrictions. This plugin bypasses CSP limitations by first downloading the image and then returning it via blob, allowing external images to display normally.

When not using this plugin, attempting to load external images will encounter CSP errors similar to the following:

```
Refused to load the image '...' because it violates the following Content Security Policy directive: "img-src 'self' data: mediastream: blob: filesystem: 'nonce-MDdlNWNlZjYtMzg0MS00ZjI0LTk0ZDAtNWZiNzM5ZjQwNmM3' *.dify.ai *.udify.app udify.app .cloudflareinsights.com .sentry.io http://localhost: http://127.0.0.1: analytics.google.com googletagmanager.com *.googletagmanager.com google-analytics.com api.github.com".
```

Related issue: [Dify Issue #9878](https://github.com/langgenius/dify/issues/9878)

## Developer Information

- **Author**: lzfxxx
- **Version**: 0.0.1
- **Type**: Tool Plugin

## Feedback and Issues

If you encounter any problems or have suggestions, please submit an issue on the [GitHub repository](https://github.com/lzfxxx/image-downloader).



