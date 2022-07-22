from socket import NI_NAMEREQD
import requests
from pathlib import Path

SPCX_LAUNCH_ID = "5eb87ce3ffd86e000604b336"

def download_image(url: str, path: str) -> None:
    response = requests.get(url)
    response.raise_for_status()

    filename = "hubble.jpeg"
    with open(path + filename, "wb") as file:
        file.write(response.content)


def get_spcx_launch_images(launch_id: str) -> None:
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()
    return launch["links"]["flickr"]["original"]


def main():
    img_path = "images/"
    Path(img_path).mkdir(parents=True, exist_ok=True)

    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    download_image(url, img_path)
    
    spcx_launch_images = get_spcx_launch_images(SPCX_LAUNCH_ID)
    print(spcx_launch_images)

if __name__ == "__main__":
    main()
