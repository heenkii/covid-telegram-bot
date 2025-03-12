from loader import dp, bot
from FSM import user_states
from keyboards.default import info_keyboard
from aiogram import types


@dp.message_handler(text="Информация о проекте 📃", state=user_states.main_page)
async def about_project(message: types.Message):
    await user_states.info_page.set()
    await bot.send_message(
        message.from_user.id, "Информация о проекте 📃", reply_markup=info_keyboard
    )


@dp.message_handler(text="Используемые ресурсы 📚", state=user_states.info_page)
async def using_data(message: types.Message):
    await bot.send_message(
        message.from_user.id, "Источник информации 📊 - worldometers.info"
    )
