import os
import random 
from dotenv import load_dotenv
import telegram


def main():
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_TOKEN']
    img_folder_path = "./images/"
    bot = telegram.Bot(telegram_bot_token)
    
    try:
        imgs_in_folder=os.listdir(img_folder_path)
        if imgs_in_folder:
            rand_img=random.choice(imgs_in_folder)
            bot.send_photo(chat_id="@DvmnLrng", photo=open(f'{img_folder_path}{rand_img}', 'rb'))
        else:
            print("Images foldes is empty!")
    except FileNotFoundError:
        print("Images folder doesn't exist!")

if __name__ == '__main__':
    main()
