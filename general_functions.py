import os.path
from pathlib import Path
import requests
import urllib.parse


def download_images(images_urls: list, file_path: str, file_name: str, url_params: dict = None) -> None:
    Path(file_path).mkdir(parents=True, exist_ok=True)
    for img_number, image_url in enumerate(images_urls):
        file_extension = get_file_extension(image_url) 
        if not file_extension: continue

        response = requests.get(image_url, params=url_params)
        response.raise_for_status()
        
        filename = f"{file_name}{img_number}{file_extension}"
        file = Path(file_path, filename)
        with open(file, "wb") as file:
            file.write(response.content)


def get_file_extension(images_url: str) -> str:
    parsed_url = urllib.parse.urlparse(images_url)
    return os.path.splitext(parsed_url.path)[1]
