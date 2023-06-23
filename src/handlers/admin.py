from create_bot import bot, dp
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Filter
from sqlighter import Database
from settings import Config


# class CustomFilters:

class IsAdmin(Filter):

    async def check(self, message: types.Message) -> bool:
        return message.from_user.id == int(Config["OWNER_ID"])


async def update(message: types.Message):
    db = Database()
    db.update_data()
    await bot.send_message(message.from_user.id, "База данных обновлена ✅")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        update,
        IsAdmin(),
        state="*",
        commands=["update"]
    )
