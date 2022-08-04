import os
import random 
import argparse
import time
from argparse import RawTextHelpFormatter
from dotenv import load_dotenv
import telegram


def create_argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""\
        Скрипт автоматически публикует фотографии каждые 'period' часов.\n
        При отсутсвии параметра 'period' публикация происходит каждые 4 часа.""",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-period', help='периодичность публикации картинок в часах', type=float)
    return parser.parse_args()


def main():
    load_dotenv()
    args = create_argparser()
    img_folder_path = "./images/"
    telegram_bot_token = os.environ['TELEGRAM_TOKEN']
    photo_posting_period = os.environ['PHOTO_POSTING_PERIOD']
    bot = telegram.Bot(telegram_bot_token)
    
    if args.period: photo_posting_period = args.period

    while True:
        try:
            imgs_in_folder=os.listdir(img_folder_path)
            if imgs_in_folder:
                rand_img=random.choice(imgs_in_folder)
                bot.send_photo(
                    chat_id="@DvmnLrng",
                    photo=open(f'{img_folder_path}{rand_img}', 'rb')
                    )
            else:
                print("Images folder is empty!")
        except FileNotFoundError:
            print("Images folder doesn't exist!")
        time.sleep(float(photo_posting_period)*3600)

if __name__ == '__main__':
    main()
