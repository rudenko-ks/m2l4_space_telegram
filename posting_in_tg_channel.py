import os
import random 
import argparse
import time
from argparse import RawTextHelpFormatter
from unittest.mock import DEFAULT
from dotenv import load_dotenv
import telegram


def create_argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""\
        Скрипт автоматически публикует фотографии каждые 'period' часов.\n
        При отсутсвии параметра 'period' публикация происходит каждые 4 часа.""",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-period', help='периодичность публикации картинок в часах', type=float, default=4)
    return parser.parse_args()


def main():
    load_dotenv()
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    args = create_argparser()
    img_folder_path = "./images/"
    telegram_bot_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(telegram_bot_token)
    
    while True:
        try:
            imgs_in_folder=os.listdir(img_folder_path)
            if imgs_in_folder:
                rand_img=random.choice(imgs_in_folder)
                with open(f'{img_folder_path}{rand_img}', 'rb') as img:
                    bot.send_photo(
                        chat_id=telegram_chat_id,
                        photo=img
                    )
            else:
                print("Images folder is empty!")
        except FileNotFoundError:
            print("Images folder doesn't exist!")
        time.sleep(float(args.period)*3600)

if __name__ == '__main__':
    main()
