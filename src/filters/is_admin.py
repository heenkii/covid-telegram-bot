from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from config import OWNER_ID
class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id == OWNER_ID
