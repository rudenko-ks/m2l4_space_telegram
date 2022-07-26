import os.path
import datetime
import urllib.parse

from pathlib import Path

import requests
from dotenv import load_dotenv

IMG_FOLDER_PATH = "./images/"


def download_images(images_urls: list, file_path: str, file_name: str, token: str = None) -> None:
    Path(file_path).mkdir(parents=True, exist_ok=True)

    if token:
        params = (
            ("api_key", token),
        )
    else:
        params = None
    
    for img_number, image_url in enumerate(images_urls):
        try:
            response = requests.get(image_url, params=params)
            response.raise_for_status()

            file_extension = get_file_extension(image_url)
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


def fetch_spacex_last_launch_photos(launch_id: str) -> None:
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    spcx_launch_info = response.json()
    
    name_template = "spacex_"
    spcx_launch_images_urls = spcx_launch_info["links"]["flickr"]["original"]
    download_images(spcx_launch_images_urls, IMG_FOLDER_PATH, name_template)


def fetch_nasa_daytime_photos(token: str) -> None:
    params = (
        ("api_key", token),
        ("count", 15),
    )
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    nasa_daytime_photos_info = response.json()
    
    name_template = "nasa_apod_"
    nasa_daytime_photos_urls = [daytime_photo_info["url"] for daytime_photo_info in nasa_daytime_photos_info]
    download_images(nasa_daytime_photos_urls, IMG_FOLDER_PATH, name_template)


def fetch_nasa_epic_photos(token: str) -> None:
    params = (
        ("api_key", token),
    )
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=params)
    response.raise_for_status()
    nasa_epic_photos_info = response.json()
    
    nasa_epic_photos_urls = []
    for nasa_epic_photo_info in nasa_epic_photos_info:
        img_name = nasa_epic_photo_info["image"]
        img_datetime = nasa_epic_photo_info["date"].split()
        img_date = datetime.date.fromisoformat(img_datetime[0])
        url = f"https://api.nasa.gov/EPIC/archive/natural/{img_date.year}/{img_date.strftime('%m')}/{img_date.strftime('%d')}/png/{img_name}.png"
        nasa_epic_photos_urls.append(url)
    
    name_template = "nasa_epic_"
    download_images(nasa_epic_photos_urls, IMG_FOLDER_PATH, name_template, token)


def main():
    SPCX_LAUNCH_ID = "5eb87ce3ffd86e000604b336"
    fetch_spacex_last_launch_photos(SPCX_LAUNCH_ID)

    NASA_API_TOKEN = os.environ['NASA_API_TOKEN']
    fetch_nasa_daytime_photos(NASA_API_TOKEN)
    fetch_nasa_epic_photos(NASA_API_TOKEN)

if __name__ == "__main__":
    load_dotenv()
    main()
