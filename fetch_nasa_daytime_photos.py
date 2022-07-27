import os
import argparse
from argparse import RawTextHelpFormatter
import requests
from dotenv import load_dotenv
from general_functions import download_images


def fetch_nasa_daytime_photos(token: str, count: int) -> None:
    if not count: count = 10
    params = (
        ("api_key", token),
        ("count", count),
    )
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    nasa_daytime_photos_info = response.json()
    
    img_folder_path = "./images/"
    img_name_template = "nasa_apod_"
    nasa_daytime_photos_urls = [daytime_photo_info["url"] for daytime_photo_info in nasa_daytime_photos_info]
    download_images(nasa_daytime_photos_urls, img_folder_path, img_name_template)


def create_argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""\
        Скрипт возвращает указанное количество Astronomy Picture of the Day (APOD) фотографий сделанные NASA.\n
        По умолчанию скрипт возвращает 10 фотографий""",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-count', help='Количество запрашиваемых фотографий', type=int)
    return parser.parse_args()


def main():
    load_dotenv()
    args = create_argparser()
    NASA_API_TOKEN = os.environ['NASA_API_TOKEN']
    fetch_nasa_daytime_photos(NASA_API_TOKEN, args.count)

if __name__ == '__main__':
    main()