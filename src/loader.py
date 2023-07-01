from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from config import TOKEN


storage = MongoStorage(host='database', port=27017, db_name="test")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
