from loader import dp, bot
from keyboards.inline import who_website_inline_keyboard
from FSM import user_states

from aiogram import types


@dp.message_handler(text="Рекомендации ВОЗ 😷", state=user_states.main_page)
async def recomendation(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Всемирная организация здравоохранения",
                           reply_markup=who_website_inline_keyboard)
    await bot.send_sticker(message.from_user.id,
                           "CAACAgIAAxkBAAIIoV65vLrWbECKVD86BVQLM14hUQr4AALyAQACVp29CgqJR4ysf4fyGQQ")
