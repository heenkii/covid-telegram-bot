from aiogram import Dispatcher, types
from create_bot import bot
from settings import Config
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards import client_kb

import handlers.tools as tools


class Fsm_user(StatesGroup):
    main_page = State()
    countries_page = State()
    find_page = State()
    info_page = State()


async def start(message: types.Message):
    await Fsm_user.main_page.set()
    await bot.send_message(message.from_user.id,
                           "Бип-бип...\nПривет!\nЭтот бот был разработан для распространения информации о короновирусной инфекции (Covid-19)🦠")
    await bot.send_sticker(message.from_user.id,
                           "CAACAgIAAxkBAAIIgF65ucQNXFE8q86mjl_E3OuLiPXzAALOAQACVp29Cq2jmuzmnvpMGQQ")
    await bot.send_message(message.from_user.id,
                           "Нажми одну из кнопок внизу\n😉 🔽",
                           reply_markup=client_kb.main_kb)


async def get_statistic_page(message: types.Message):
    await Fsm_user.countries_page.set()
    await bot.send_message(message.from_user.id,
                           "Статистика в... 🔽",
                           reply_markup=client_kb.countries_kb)


async def recomendation(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Всемирная организация здравоохранения",
                           reply_markup=client_kb.rec_inline_kb)
    await bot.send_sticker(message.from_user.id,
                           "CAACAgIAAxkBAAIIoV65vLrWbECKVD86BVQLM14hUQr4AALyAQACVp29CgqJR4ysf4fyGQQ")


async def about_project(message: types.Message):
    await Fsm_user.info_page.set()
    await bot.send_message(message.from_user.id,
                           "Информация о проэкте 📃",
                           reply_markup=client_kb.info_kb)


async def statistic_in_russia(message: types.Message):
    await bot.send_message(message.from_user.id,
                           tools.get_data("russia", "России 🇷🇺"))


async def statistic_in_world(message: types.Message):
    await bot.send_message(message.from_user.id,
                           tools.get_data("world", ""))


async def get_find_page(message: types.Message):
    await Fsm_user.find_page.set()
    await bot.send_message(message.from_user.id,
                           "Введите название страны 🔽",
                           reply_markup=client_kb.find_kb)


async def back_to_main_screen(message: types.Message):
    await Fsm_user.main_page.set()
    await bot.send_message(message.from_user.id,
                           "Главное меню 🔁",
                           reply_markup=client_kb.main_kb)


async def find_statistic(message: types.Message):
    country = message.text.lower()
    flag = False
    if country in tools.ru_country.keys() or country in tools.db:
        flag = True
    if country == "date":
        flag = False

    if flag == True:
        if country.lower() in tools.ru_country.keys():
            country = tools.ru_country[country.lower()]
        await bot.send_message(message.from_user.id,
                               tools.get_data(country, message.text))
    else:
        await bot.send_message(message.from_user.id,
                               "У меня нет такой информации 😔")


async def using_data(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Источник информации 📊 - worldometers.info")


async def answer_error(message: types.Message):
    await bot.send_message(message.from_user.id, "Я не могу выполнить ваш запрос 😔")


# register handlers
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "help"])

    dp.register_message_handler(get_statistic_page,
                                Text(equals="Узнать статистику 📊"),
                                state=Fsm_user.main_page)

    dp.register_message_handler(recomendation,
                                Text(equals="Рекомендации ВОЗ 😷"),
                                state=Fsm_user.main_page)

    dp.register_message_handler(about_project,
                                Text(equals="Информация о проэкте 📃"),
                                state=Fsm_user.main_page)

    dp.register_message_handler(statistic_in_russia,
                                Text(equals="Статистика в России 🇷🇺"),
                                state=Fsm_user.countries_page)

    dp.register_message_handler(statistic_in_world,
                                Text(equals="Статистика в мире 🌍"),
                                state=Fsm_user.countries_page)

    dp.register_message_handler(get_find_page,
                                Text(equals="Поиск 🔎"),
                                state=Fsm_user.countries_page)

    dp.register_message_handler(back_to_main_screen,
                                Text(equals="Вернуться к главному меню 🔄"),
                                state="*")

    dp.register_message_handler(find_statistic,
                                state=Fsm_user.find_page)

    dp.register_message_handler(using_data,
                                Text(equals="Используемые ресурсы 📚"),
                                state=Fsm_user.info_page)

    dp.register_message_handler(answer_error, state="*")
