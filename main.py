import os
from dotenv import load_dotenv

from fetch_nasa_epic_photos import fetch_nasa_epic_photos
from fetch_nasa_daytime_photos import fetch_nasa_daytime_photos
from fetch_spacex_last_launch_photos import fetch_spacex_last_launch_photos


def main():
    load_dotenv()
    #SPCX_LAUNCH_ID = "5eb87ce3ffd86e000604b336"
    #fetch_spacex_last_launch_photos(SPCX_LAUNCH_ID)
    fetch_spacex_last_launch_photos()

    NASA_API_TOKEN = os.environ['NASA_API_TOKEN']
    fetch_nasa_daytime_photos(NASA_API_TOKEN, 15)
    fetch_nasa_epic_photos(NASA_API_TOKEN)

if __name__ == "__main__":
    main()
