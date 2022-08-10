import os
import argparse
from argparse import RawTextHelpFormatter
from wsgiref.simple_server import demo_app
import requests
from dotenv import load_dotenv
from general_functions import download_images


def fetch_nasa_daytime_photos(token: str, count: int) -> None:
    params = (
        ("api_key", token),
        ("count", count),
    )
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    photos_collection_with_metadata = response.json()
    
    img_folder_path = "./images/"
    img_name_template = "nasa_apod_"
    daytime_photos_urls = [photo_metadata["url"] for photo_metadata in photos_collection_with_metadata]
    download_images(daytime_photos_urls, img_folder_path, img_name_template)


def create_argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""\
        Скрипт возвращает указанное количество Astronomy Picture of the Day (APOD) фотографий сделанные NASA.\n
        По умолчанию скрипт возвращает 5 фотографий""",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-count', help='Количество запрашиваемых фотографий', type=int, default=5)
    return parser.parse_args()


def main():
    load_dotenv()
    args = create_argparser()
    nasa_api_token = os.environ['NASA_API_TOKEN']
    fetch_nasa_daytime_photos(nasa_api_token, args.count)

if __name__ == '__main__':
    main()
