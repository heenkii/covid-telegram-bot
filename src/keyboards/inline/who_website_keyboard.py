from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

who_website_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Сайт ВОЗ 🌍",
                url="www.who.int/ru/emergencies/diseases/novel-coronavirus-2019",
            )
        ]
    ]
)
