from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Используемые ресурсы 📚")],
        [KeyboardButton("Вернуться к главному меню 🔄")],
    ],
    resize_keyboard=True,
)
