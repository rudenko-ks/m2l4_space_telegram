import os
import datetime
import requests
from dotenv import load_dotenv
from general_functions import download_images


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
    
    img_folder_path = "./images/"
    img_name_template = "nasa_epic_"
    download_images(nasa_epic_photos_urls, img_folder_path, img_name_template, token)


def main():
    load_dotenv()
    NASA_API_TOKEN = os.environ['NASA_API_TOKEN']
    fetch_nasa_epic_photos(NASA_API_TOKEN)

if __name__ == '__main__':
    main()
