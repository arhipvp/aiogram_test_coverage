import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)
