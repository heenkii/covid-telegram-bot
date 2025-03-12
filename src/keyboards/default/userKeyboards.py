from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Узнать статистику 📊")],
        [KeyboardButton("Рекомендации ВОЗ 😷")],
        [KeyboardButton("Информация о проекте 📃")],
    ],
    resize_keyboard=True,
)

countries_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Статистика в России 🇷🇺")],
        [KeyboardButton("Статистика в мире 🌍")],
        [KeyboardButton("Поиск 🔎")],
        [KeyboardButton("Вернуться к главному меню 🔄")],
    ],
    resize_keyboard=True,
)

find_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Вернуться к главному меню 🔄")],
    ],
    resize_keyboard=True,
)

info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Используемые ресурсы 📚")],
        [KeyboardButton("Вернуться к главному меню 🔄")],
    ],
    resize_keyboard=True,
)
