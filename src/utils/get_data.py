from .sqlighter import Database


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
    return f"""Статистика в {text} на {country_data["date_update"]}


Население {country_data["population"]} человек

		Всего заразились 😷: {country_data["total_case"] }
		Сейчас болеют 😷: {country_data["active_case"]}
		Выздовели ✅: {country_data["total_recover"]}
		Умерли 💀: {country_data["total_death"]}

За последние 24 часа 🕓
		Заболели 😷: {country_data["new_case"]}
		Выздовели ✅: {country_data["new_recover"]}
		Умерли 💀: {country_data["new_death"]}"""
