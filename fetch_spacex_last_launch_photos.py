import requests
from general_functions import download_images


def fetch_spacex_last_launch_photos(launch_id: str) -> None:
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    spcx_launch_info = response.json()
    
    img_folder_path = "./images/"
    img_name_template = "spacex_"
    spcx_launch_images_urls = spcx_launch_info["links"]["flickr"]["original"]
    download_images(spcx_launch_images_urls, img_folder_path, img_name_template)