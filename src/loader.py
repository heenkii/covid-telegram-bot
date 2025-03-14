from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from config import TOKEN, MONGO_HOST, MONGO_PORT, MONGO_DATABASE


storage = MongoStorage(
    host=MONGO_HOST,
    port=MONGO_PORT,
    db_name=MONGO_DATABASE
)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
