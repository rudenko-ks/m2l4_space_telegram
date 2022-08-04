# Space Telegram

This set of scripts downloads:
- photos of SpaceX launches
- EPIC photo from NASA
- APOD photo from NASA
- automatically publishes a random photo to the Telegram channel at a specified interval

## How to install

This should be enough for quickstart:
- Python3 should be already installed. 
- Create virtual environment (optional)
```
python -m venv .venv
source .venv/bin/activate
```
- Install all requirements:
```
pip install -r requirements.txt
```
- Create `.env` file in project directory and copy-paste this:
``` bash 
NASA_API_TOKEN=<ENTER YOUR NASA API TOKEN HERE>
TELEGRAM_TOKEN=<ENTER YOUR TELEGRAM BOT TOKEN HERE>
PHOTO_POSTING_PERIOD=4 #<PERIOD TO POST PHOTOS IN A CHANNEL IN HOURS>
```

## How to run scripts
Each of the photo services has its own script that can work independently.
Also, there is a script that can download photos from three services at the same time.
And a script was written separately that runs and publishes photos to the Telegram channel with a specified time interval

#### fetch_nasa_daytime_photos.py
The script downloads the specified number of Astronomy Picture of the Day (APOD) photos taken by NASA.
By default, the script downloads 5 photos
```
python fetch_nasa_daytime_photos.py [-h] [-count COUNT]
```

options: 

`-h, --help` show this help message and exit 

`-count COUNT` Number of photos to download

#### fetch_nasa_epic_photos.py
The script downloads EPIC photo from NASA
```
python fetch_nasa_epic_photos.py
```

#### fetch_spacex_last_launch_photos.py
The script returns photos of SpaceX launches by id.
If id is not specified, then the script returns the photos of the last launch.
Example launch id: `5eb87ce3ffd86e000604b336`
```
python fetch_spacex_last_launch_photos.py [-h] [-id ID] 
```
options:

`-h, --help` show this help message and exit

`-id ID` launch id

#### fetch_them_all.py
The script downloads photos from three services at the same time.
```
python fetch_them_all.py
```

#### posting_in_tg_channel.py
The script automatically posts photos every 'period' hours.
If the 'period' parameter is missing, the publication occurs every 4 hours.
```
python posting_in_tg_channel.py [-h] [-period PERIOD]
```
options:

`-h, --help`      show this help message and exit

`-period PERIOD` frequency of posting pictures in hours

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
