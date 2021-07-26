import asyncio, configparser, config, logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(filename="app.log", filemode="w", level=logging.INFO)

bot = Bot(token=config.get_bot_token())
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бип-бип...\nПривет!\nЭтот бот был создан для распространения информации о статистике по коронавирусу (Covid-19)🦠', reply_markup=config.main_k)
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAIIgF65ucQNXFE8q86mjl_E3OuLiPXzAALOAQACVp29Cq2jmuzmnvpMGQQ')
    await bot.send_message(message.from_user.id, 'Нажми одну из кнопок внизу\n😉 🔽')


@dp.message_handler(content_types=['text'])
async def send_data(message: types.Message):

    user_id = message.from_user.id
    text = message.text.strip()


    # main page

    if text== 'Узнать статистику 📊':
        await bot.send_message(message.from_user.id, 'Выбери ниже какую статистику ты хочешь узнать 😉 🔽', reply_markup=config.static_k)

    elif text== 'Рекомендации ВОЗ 😷':
        m = types.InlineKeyboardMarkup(True)
        btn = types.InlineKeyboardButton(text='Сайт ВОЗ 🌍', url='www.who.int/ru/emergencies/diseases/novel-coronavirus-2019')
        m.add(btn)
        await bot.send_message(user_id, 'Всемирная организация здравоохранения', reply_markup=m)
        await bot.send_sticker(user_id, 'CAACAgIAAxkBAAIIoV65vLrWbECKVD86BVQLM14hUQr4AALyAQACVp29CgqJR4ysf4fyGQQ')

    elif text== 'Информация о проэкте':
        await bot.send_message(user_id, 'Информация о проэкте', reply_markup=config.info_k)


    # static page

    elif text== 'Статистика в России 🇷🇺':
        await bot.send_message(user_id, config.get_data("russia", "России 🇷🇺"), reply_markup=config.static_k)

    elif text== 'Статистика в мире 🌍':
        await bot.send_message(user_id, config.get_data("world", ""), reply_markup=config.static_k)

    elif text== 'Узнать статистику в любой стране':
        await bot.send_message(user_id, 'Введите название страны', reply_markup=config.find_k)

    elif text == 'Вернуться к главному меню 🔄':
        await bot.send_message(user_id, 'Главное меню', reply_markup=config.main_k)

    elif (text.lower() in config.ru_country.keys()) or (text.lower() in config.db):
        country = text.lower()
        if country.lower() in config.ru_country.keys():
            country = config.ru_country[country.lower()]
        await bot.send_message(user_id, config.get_data(country, text), reply_markup=config.find_k)


    # info page

    elif text== 'Используемые ресурсы':
        await bot.send_message(user_id, 'База данных - worldometers.info', reply_markup=config.main_k)

    else:
        if (config.word_filter(text)):
            await bot.send_message(user_id, 'Ненадо так 😣😭')
        else:
            await bot.send_message(user_id, 'Я пока не могу выполнить данный запрос или найти статистику в этой стране 😔')


async def update_data(whait_for=3600):
    while True:
        config.update_data()
        await asyncio.sleep(whait_for)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(update_data(10800))
    executor.start_polling(dp, skip_updates=True)
