from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Узнать статистику 📊")],
        [KeyboardButton("Рекомендации ВОЗ 😷")],
        [KeyboardButton("Информация о проекте 📃")],
    ],
    resize_keyboard=True,
)
