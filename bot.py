import asyncio, config

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Filter


bot = Bot(token=config.SETTINGS["TOKEN"])
dp = Dispatcher(bot)


class IsAdmin(Filter):

    async def check(self, message: types.Message)->bool:
        return message.from_user.id == int(config.SETTINGS["OWNER_ID"])


@dp.message_handler(commands = "start")
async def start(message: types.Message):
    user_id = message.from_user.id

    await bot.send_message(user_id, "Бип-бип...\nПривет!\nЭтот бот был разработан для распространения информации о короновирусной инфекции (Covid-19)🦠", reply_markup=config.get_keyboard("main"))
    await bot.send_sticker(user_id, "CAACAgIAAxkBAAIIgF65ucQNXFE8q86mjl_E3OuLiPXzAALOAQACVp29Cq2jmuzmnvpMGQQ")
    await bot.send_message(user_id, "Нажми одну из кнопок внизу\n😉 🔽")


@dp.message_handler(IsAdmin(), commands = "update")
async def update(message: types.Message):
    config.update_data()
    await bot.send_message(message.from_user.id, "База данных обновлена ✅")


@dp.message_handler(content_types=["text"])
async def send_data(message: types.Message):

    user_id = message.from_user.id
    text = message.text.strip()


    # main page
    if text == "Узнать статистику 📊":
        await bot.send_message(message.from_user.id, "Статистика в... 🔽", reply_markup=config.get_keyboard("stat"))

    elif text == "Рекомендации ВОЗ 😷":
        message_keyboard = types.InlineKeyboardMarkup(True)
        button = types.InlineKeyboardButton(text="Сайт ВОЗ 🌍", url="www.who.int/ru/emergencies/diseases/novel-coronavirus-2019")
        message_keyboard.add(button)
        await bot.send_message(user_id, "Всемирная организация здравоохранения", reply_markup=message_keyboard)
        await bot.send_sticker(user_id, "CAACAgIAAxkBAAIIoV65vLrWbECKVD86BVQLM14hUQr4AALyAQACVp29CgqJR4ysf4fyGQQ")

    elif text == "Информация о проэкте 📃":
        await bot.send_message(user_id, "Информация о проэкте 📃", reply_markup=config.get_keyboard("info"))


    # static page
    elif text == "Статистика в России 🇷🇺":
        await bot.send_message(user_id, config.get_data("russia", "России 🇷🇺"))

    elif text == "Статистика в мире 🌍":
        await bot.send_message(user_id, config.get_data("world", ""))

    elif text == "Поиск 🔎":
        await bot.send_message(user_id, "Введите название страны 🔽", reply_markup=config.get_keyboard("find"))

    elif text == "Вернуться к главному меню 🔄":
        await bot.send_message(user_id, "Главное меню 🔁", reply_markup=config.get_keyboard("main"))

    elif ( (text.lower() in config.ru_country.keys()) or (text.lower() in config.db) ) and (text.lower() != "date"):
        country = text.lower()
        if country.lower() in config.ru_country.keys():
            country = config.ru_country[country.lower()]
        await bot.send_message(user_id, config.get_data(country, text))


    # info page
    elif text== "Используемые ресурсы 📚":
        await bot.send_message(user_id, "Источник информации 📊 - worldometers.info")


    else:
        if (config.word_filter(text)):
            await bot.send_message(user_id, "Ненадо так 😣😭")
        else:
            await bot.send_message(user_id, "Я не могу выполнить ваш запрос 😔")


#update statistic
async def update_data(whait_for=3600):
    while True:
        config.update_data()
        await asyncio.sleep(whait_for)


#async run bot and update static
if __name__ == "__main__":
    dp.bind_filter(IsAdmin)
    loop = asyncio.get_event_loop()
    loop.create_task(update_data(10800))
    executor.start_polling(dp, skip_updates=True)
