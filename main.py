import requests
from pathlib import Path

SPCX_LAUNCH_ID = "5eb87ce3ffd86e000604b336"


def download_images(images_urls: list, path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

    for img_number, image_url in enumerate(images_urls):
        response = requests.get(image_url)
        response.raise_for_status()
        
        filename = f"spacex_{img_number}.jpeg"
        with open(path + filename, "wb") as file:
            file.write(response.content)


def fetch_spacex_last_launch(launch_id: str) -> None:
    img_folder_path = "./images/"
    spacex_api_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    launch = response.json()
    
    launch_images_urls = launch["links"]["flickr"]["original"]
    download_images(launch_images_urls, img_folder_path)


def main():
    fetch_spacex_last_launch(SPCX_LAUNCH_ID)

if __name__ == "__main__":
    main()
