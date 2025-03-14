from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

countries_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Статистика в России 🇷🇺")],
        [KeyboardButton("Статистика в мире 🌍")],
        [KeyboardButton("Поиск 🔎")],
        [KeyboardButton("Вернуться к главному меню 🔄")],
    ],
    resize_keyboard=True,
)
