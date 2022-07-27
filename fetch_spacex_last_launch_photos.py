import argparse
from argparse import RawTextHelpFormatter
from general_functions import download_images
import requests


def get_last_launch_with_photos() -> dict:
    response = requests.get("https://api.spacexdata.com/v5/launches/")
    response.raise_for_status()
    spcx_launches_info = response.json()
    return [spcx_launch_info for spcx_launch_info in spcx_launches_info if spcx_launch_info["links"]["flickr"]["original"]].pop()


def get_launch_by_id(launch_id: str) -> dict:
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()


def fetch_spacex_last_launch_photos(launch_id: str = None) -> None:
    if not launch_id:
        spcx_launch_info = get_last_launch_with_photos()
    else:
        spcx_launch_info = get_launch_by_id(launch_id)
    
    img_folder_path = "./images/"
    img_name_template = "spacex_"
    spcx_launch_images_urls = spcx_launch_info["links"]["flickr"]["original"]
    download_images(spcx_launch_images_urls, img_folder_path, img_name_template)


def main():
    parser = argparse.ArgumentParser(
        description="""\
        Скрипт возвращает фотографии запуска космического короабля SpaceX по id запуска.\n
        При отсутсвии id возвращает фотографии последнего запуска\n
        Пример id запуска: 5eb87ce3ffd86e000604b336""",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-id', help='id запуска')
    args = parser.parse_args()
    fetch_spacex_last_launch_photos(args.id)

if __name__ == '__main__':
    main()
