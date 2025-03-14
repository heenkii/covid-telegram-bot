from FSM import user_states
from aiogram import types
from keyboards.default import countries_keyboard
from loader import dp, bot
from utils import get_data


@dp.message_handler(
    text="Узнать статистику 📊",
    state=user_states.main_page)
async def get_statistic_page(message: types.Message):
    await user_states.countries_page.set()
    await bot.send_message(
        message.from_user.id,
        "Статистика в... 🔽",
        reply_markup=countries_keyboard
    )


@dp.message_handler(
    text="Статистика в России 🇷🇺",
    state=user_states.countries_page)
async def statistic_in_russia(message: types.Message):
    await bot.send_message(message.from_user.id,
                           get_data("russia", "России 🇷🇺"))


@dp.message_handler(
    text="Статистика в мире 🌍",
    state=user_states.countries_page)
async def statistic_in_world(message: types.Message):
    await bot.send_message(message.from_user.id,
                           get_data("world", ""))
