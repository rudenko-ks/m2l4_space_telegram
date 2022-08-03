import os
from dotenv import load_dotenv
import telegram


def main():
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(telegram_bot_token)
    bot.send_message(chat_id="@DvmnLrng", text="Hello, python newbie ^_^")

if __name__ == '__main__':
    main()
