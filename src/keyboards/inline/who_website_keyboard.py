from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

url = "who.int/ru/emergencies/diseases/novel-coronavirus-2019"

who_website_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Сайт ВОЗ 🌍",
                url=url
            )
        ]
    ]
)
