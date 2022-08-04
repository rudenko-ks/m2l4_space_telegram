import os
from dotenv import load_dotenv

from fetch_nasa_epic_photos import fetch_nasa_epic_photos
from fetch_nasa_daytime_photos import fetch_nasa_daytime_photos
from fetch_spacex_last_launch_photos import fetch_spacex_last_launch_photos


def main():
    load_dotenv()
    fetch_spacex_last_launch_photos()

    nasa_api_token = os.environ['NASA_API_TOKEN']
    fetch_nasa_daytime_photos(nasa_api_token, count=5)
    fetch_nasa_epic_photos(nasa_api_token)

if __name__ == "__main__":
    main()
