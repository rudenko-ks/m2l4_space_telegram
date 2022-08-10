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
    photos_collection_with_metadata = response.json()
    
    nasa_epic_photos_urls = []
    for photo_metadata in photos_collection_with_metadata:
        img_name = photo_metadata["image"]
        img_datetime = photo_metadata["date"].split()
        img_date = datetime.date.fromisoformat(img_datetime[0])
        url = f"https://api.nasa.gov/EPIC/archive/natural/{img_date.year}/{img_date.strftime('%m')}/{img_date.strftime('%d')}/png/{img_name}.png"
        nasa_epic_photos_urls.append(url)
    
    img_folder_path = "./images/"
    img_name_template = "nasa_epic_"
    download_images(nasa_epic_photos_urls, img_folder_path, img_name_template, params)


def main():
    load_dotenv()
    nasa_api_token = os.environ['NASA_API_TOKEN']
    fetch_nasa_epic_photos(nasa_api_token)

if __name__ == '__main__':
    main()
