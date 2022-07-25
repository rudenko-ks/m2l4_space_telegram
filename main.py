import os.path
import urllib.parse

from pathlib import Path
from webbrowser import get

import requests

SPCX_LAUNCH_ID = "5eb87ce3ffd86e000604b336"


def download_images(images_urls: list, path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

    for img_number, image_url in enumerate(images_urls):
        response = requests.get(image_url)
        response.raise_for_status()
        
        file_extension = get_file_extension(image_url)
        filename = f"spacex_{img_number}{file_extension}"
        with open(path + filename, "wb") as file:
            file.write(response.content)


def get_file_extension(images_url: str) -> str:
    parsed_url = urllib.parse.urlparse(images_url)
    return os.path.splitext(parsed_url.path)[1]


def fetch_spacex_last_launch(launch_id: str) -> None:
    img_folder_path = "./images/"
    spacex_api_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    spcx_launch_info = response.json()
    
    spcx_launch_images_urls = spcx_launch_info["links"]["flickr"]["original"]
    download_images(spcx_launch_images_urls, img_folder_path)


def main():
    fetch_spacex_last_launch(SPCX_LAUNCH_ID)

if __name__ == "__main__":
    main()
