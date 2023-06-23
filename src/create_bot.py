from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings import Config

bot = Bot(token=Config["TOKEN"])
dp = Dispatcher(bot, storage=MemoryStorage())
