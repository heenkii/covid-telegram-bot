from aiogram import types
from aiogram.dispatcher.filters import Filter
from sqlighter import Database


def get_data(country: str, text: str) -> str:
    db = Database()
    country_data = db.get_country_data(country=country.strip().lower())
    db.close()
    if country_data == False:
        return "Ошибка в получении информации🧑‍💻\nПовторите попытку позже"

    if text.lower() in ["world", "мир"] or country in ["world", "мир"]:
        text = "мире 🌍"

    if text.lower() in ["russia", "россия"]:
        text = "России 🇷🇺"
    return f'''Статистика в {text} на {country_data["date_update"]}


Население {country_data["population"]} человек

		Всего заразились 😷: {country_data["total_case"] if country_data["total_case"] != "N one" else "-"}
		Сейчас болеют 😷: {country_data["active_case"] if country_data["active_case"] != "N one" else "-"}
		Выздовели ✅: {country_data["total_recover"] if country_data["total_recover"] != "N one" else "-"}
		Умерли 💀: {country_data["total_death"] if country_data["total_death"] != "N one" else "-"}

За последние 24 часа 🕓
		Заболели 😷: {country_data["new_case"] if country_data["new_case"] != "N one" else "-"}
		Выздовели ✅: {country_data["new_recover"] if country_data["new_recover"] != "N one" else "-"}
		Умерли 💀: {country_data["new_death"] if country_data["new_death"] != "N one" else "-"}'''
