from aiogram import Bot, Dispatcher, types, executor
import logging
import os
from PIL import *

# Logging
logging.basicConfig(level=logging.INFO)

# token

TOKEN = ("6123832925:AAGpqIFX91f3TvfWD953CCtIqea3n6G7Y3E")

# Bot
dp = Dispatcher(Bot(token=TOKEN))
bot = Bot(token=TOKEN)