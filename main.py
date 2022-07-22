import requests
from pathlib import Path


def download_image(url: str, path: str) -> None:
    response = requests.get(url)
    response.raise_for_status()

    filename = "hubble.jpeg"
    with open(path + filename, "wb") as file:
        file.write(response.content)


def main():
    img_path = "images/"
    Path(img_path).mkdir(parents=True, exist_ok=True)

    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    download_image(url, img_path)

if __name__ == "__main__":
    main()
