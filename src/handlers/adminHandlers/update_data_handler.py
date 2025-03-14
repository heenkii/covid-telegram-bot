from aiogram import types
from filters import IsAdmin
from loader import bot, dp
from utils.sqlighter import Database


@dp.message_handler(
    IsAdmin(),
    commands=["update"],
    state="*")
async def update(message: types.Message):
    db = Database()
    db.update_data()
    await bot.send_message(
        message.from_user.id,
        "База данных обновлена ✅"
    )
