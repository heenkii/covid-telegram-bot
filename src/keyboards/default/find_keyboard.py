from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

find_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Вернуться к главному меню 🔄")],
    ],
    resize_keyboard=True,
)
