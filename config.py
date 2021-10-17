from aiogram import types
import datetime, configparser, webparser


#base
with open("filter.txt", "r", encoding="utf-8") as file:
	words = file.read().split()


#translate countries

ru_country = {"россия":"russia", "сша":"usa", "германия":"germany", "италия":"italy", "китай":"china",
"япония":"japan", "польша":"poland", "украина":"ukraine", "великобритания":"uk", "афганистан":"afghanistan",
"новая гвинея":"Papua New Guinea", "испания":"spain", "франция":"france", "бразилия":"brazil", "туркмения":"turkey",
"иран":"iran", "индия":"india", "канада":"canada", "перу":"peru", "бельгия":"belgium",
"ниделанды":"netherlands", "саудовская аравия":"saudi arabia", "мексика":"mexico", "пакистан":"pakistan", "швейцария":"switzerland",
"чили":"chile", "эквадор":"ecuador", "португалия":"portugal", "беларусь":"belarus"}


#keyboards

keyboards ={
"main":["Узнать статистику 📊", "Рекомендации ВОЗ 😷", "Информация о проэкте 📃"],
"stat":["Статистика в России 🇷🇺", "Статистика в мире 🌍", "Поиск 🔎", "Вернуться к главному меню 🔄"],
"info":["Используемые ресурсы 📚", "Вернуться к главному меню 🔄"],
"find":["Вернуться к главному меню 🔄"]}


SETTINGS = {
	"TOKEN" : "",#string
	"owner_id" : "",
}

db = {}

# functions

def get_keyboard(name:str)->types.ReplyKeyboardMarkup:
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	for button in keyboards[name]:
		keyboard.add(button)
	return keyboard


def word_filter(text:str)->bool:
	for word_on_message in text.lower().split():
		if word_on_message in words:
			return True
	return False


def update_data():
	global db
	db = webparser.get_data()


def get_data(country:str, text:str)->str:
	if country.lower() not in db:
		return "Ошибка в получении информации🧑‍💻\nПовторите попытку позже"
	data = db[country.lower()]

	if text.lower() in ["world", "мир"] or country in ["world", "мир"]:
		return f'''Статистика в мире 🌍 на {db["date"]}

		Всего заразились 😷: {data["total_cases"]}
		Сейчас болеют 😷: {data["active_cases"]}
		Выздовели ✅: {data["total_recovered"]}
		Умерли 💀: {data["total_death"]}

За последние 24 часа 🕓
		Заболели 😷: {data["new_cases"]}
		Выздовели ✅: {data["new_recovered"]}
		Умерли 💀: {data["new_deaths"]}'''

	if text.lower() in ["russia", "россия"]:
		text = "России 🇷🇺"
	return f'''Статистика в {text.title()} на {db["date"]}

Население {data["population"]} человек

		Всего заразились 😷: {data["total_cases"]}
		Сейчас болеют 😷: {data["active_cases"]}
		Выздовели ✅: {data["total_recovered"]}
		Умерли 💀: {data["total_death"]}

За последние 24 часа 🕓
		Заболели 😷: {data["new_cases"]}
		Выздовели ✅: {data["new_recovered"]}
		Умерли 💀: {data["new_deaths"]}'''
