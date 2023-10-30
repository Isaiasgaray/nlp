import telebot
import os
import sys
from dotenv import load_dotenv

load_dotenv()

try:
    bot = telebot.TeleBot(
            os.environ.get('TOKEN', ''))

    bot_info = bot.get_me()

    if bot_info:
        print('Iniciando bot')
        bot.infinity_polling()

except Exception as e:
    print(f'Error -> {e}', file=sys.stderr)
    sys.exit(1)
