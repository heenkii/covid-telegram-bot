from loader import dp, bot
from FSM import user_states
from keyboards.default import find_keyboard
from utils import get_data

from aiogram import types
import json


@dp.message_handler(text="Поиск 🔎", state=user_states.countries_page)
async def get_find_page(message: types.Message):
    await user_states.find_page.set()
    await bot.send_message(
        message.from_user.id,
        "Введите название страны 🔽",
        reply_markup=find_keyboard
    )


@dp.message_handler(state=user_states.find_page)
async def find_statistic(message: types.Message):
    country = message.text.lower()
    with open("utils/countries_translate.json") as file:
        countries = json.load(file)
    flag = False
    if country in countries.keys() or country in countries.values():
        flag = True
    if country == "date":
        flag = False

    if flag:
        if country.lower() in countries.keys():
            country = countries[country.lower()]
        await bot.send_message(
            message.from_user.id,
            get_data(country, message.text))
    else:
        await bot.send_message(
            message.from_user.id,
            "У меня нет такой информации 😔")
