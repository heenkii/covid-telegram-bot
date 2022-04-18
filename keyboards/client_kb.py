from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

'''
keyboards = {
    "main": ["Узнать статистику 📊", "Рекомендации ВОЗ 😷", "Информация о проэкте 📃"],
    "stat": ["Статистика в России 🇷🇺", "Статистика в мире 🌍", "Поиск 🔎", "Вернуться к главному меню 🔄"],
    "info": ["Используемые ресурсы 📚", "Вернуться к главному меню 🔄"],
    "find": ["Вернуться к главному меню 🔄"]
}
'''

rec_inline_kb = InlineKeyboardMarkup(True)
button = InlineKeyboardButton(
    text="Сайт ВОЗ 🌍", url="www.who.int/ru/emergencies/diseases/novel-coronavirus-2019")
rec_inline_kb.add(button)


main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add("Узнать статистику 📊")
main_kb.add("Рекомендации ВОЗ 😷")
main_kb.insert("Информация о проэкте 📃")


countries_kb = ReplyKeyboardMarkup(resize_keyboard=True)
countries_kb.add("Статистика в России 🇷🇺")
countries_kb.insert("Статистика в мире 🌍")
countries_kb.add("Поиск 🔎")
countries_kb.add("Вернуться к главному меню 🔄")

info_kb = ReplyKeyboardMarkup(resize_keyboard=True)
info_kb.add("Используемые ресурсы 📚")
info_kb.add("Вернуться к главному меню 🔄")

find_kb = ReplyKeyboardMarkup(resize_keyboard=True)
find_kb.add("Вернуться к главному меню 🔄")
