import requests
from pathlib import Path


def main():
    img_path = "images/"
    Path(img_path).mkdir(parents=True, exist_ok=True)
    
    filename = "satellite.jpeg"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

    response = requests.get(url)
    response.raise_for_status()

    with open(img_path + filename, "wb") as file:
        file.write(response.content)

if __name__ == "__main__":
    main()
