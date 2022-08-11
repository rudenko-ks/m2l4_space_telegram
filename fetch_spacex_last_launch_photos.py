import argparse
from argparse import RawTextHelpFormatter
import requests
from general_functions import download_images


def get_last_launch_with_photos() -> dict:
    response = requests.get("https://api.spacexdata.com/v5/launches/")
    response.raise_for_status()
    spcx_launches_collection = response.json()
    return [spcx_launch for spcx_launch in spcx_launches_collection if spcx_launch["links"]["flickr"]["original"]].pop()


def get_launch_by_id(launch_id: str) -> dict:
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()


def fetch_spacex_last_launch_photos(launch_id: str = None) -> None:
    img_folder_path = "images"
    img_name_template = "spacex_"
    try:
        if not launch_id:
            spcx_launch = get_last_launch_with_photos()
        else:
            spcx_launch = get_launch_by_id(launch_id)
        spcx_launch_images_urls = spcx_launch["links"]["flickr"]["original"]
        
        download_images(spcx_launch_images_urls, img_folder_path, img_name_template)
    except requests.exceptions.RequestException as error:
        print('Request error:\n', error.response)
        print('Request error text:\n', error.response.text)


def create_argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""\
        Скрипт возвращает фотографии запуска космического корабля SpaceX по id запуска.\n
        При отсутсвии id возвращает фотографии последнего запуска\n
        Пример id запуска: 5eb87ce3ffd86e000604b336""",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-id', help='id запуска')
    return parser.parse_args()


def main():
    args = create_argparser()
    fetch_spacex_last_launch_photos(args.id)

if __name__ == '__main__':
    main()
