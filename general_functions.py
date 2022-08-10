import os.path
import urllib.parse
from pathlib import Path
import requests


def download_images(images_urls: list, file_path: str, file_name: str, url_params: dict = None) -> None:
    Path(file_path).mkdir(parents=True, exist_ok=True)
    for img_number, image_url in enumerate(images_urls):
        try:
            response = requests.get(image_url, params=url_params)
            response.raise_for_status()

            file_extension = get_file_extension(image_url) 
            if not file_extension:
                print(f"The file extension cannot be recognized. Wrong link:\n{image_url}")
                continue
            
            filename = f"{file_name}{img_number}{file_extension}"
            with open(file_path + filename, "wb") as file:
                file.write(response.content)
        except requests.exceptions.RequestException as error:
            print('Request error:\n', error.response)
            print('Request error:\n', error.response.text)
            continue


def get_file_extension(images_url: str) -> str:
    parsed_url = urllib.parse.urlparse(images_url)
    return os.path.splitext(parsed_url.path)[1]
