import requests
from general_functions import download_images


def fetch_nasa_daytime_photos(token: str) -> None:
    params = (
        ("api_key", token),
        ("count", 15),
    )
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    nasa_daytime_photos_info = response.json()
    
    img_folder_path = "./images/"
    img_name_template = "nasa_apod_"
    nasa_daytime_photos_urls = [daytime_photo_info["url"] for daytime_photo_info in nasa_daytime_photos_info]
    download_images(nasa_daytime_photos_urls, img_folder_path, img_name_template)