from aiogram import types
import datetime, configparser, webparser


#base
with open('filter.txt', 'r', encoding="utf-8") as file:
	words = file.read().split()


ru_country = {'россия':'russia', 'сша':'usa', 'германия':'germany', 'италия':'italy', 'китай':'china',
'япония':'japan', 'польша':'poland', 'украина':'ukraine', 'великобритания':'uk', 'афганистан':'afghanistan',
'новая гвинея':'Papua New Guinea', 'испания':'spain', 'франция':'france', 'бразилия':'brazil', 'туркмения':'turkey',
'иран':'iran', 'индия':'india', 'канада':'canada', 'перу':'peru', 'бельгия':'belgium',
'ниделанды':'netherlands', 'саудовская аравия':'saudi arabia', 'мексика':'mexico', 'пакистан':'pakistan', 'швейцария':'switzerland',
'чили':'chile', 'эквадор':'ecuador', 'португалия':'portugal', 'беларусь':'belarus'}


db = {}


#keyboards

main_k = types.ReplyKeyboardMarkup(resize_keyboard = True)

main_k.add('Узнать статистику 📊')
main_k.add('Рекомендации ВОЗ 😷')
main_k.add('Информация о проэкте')


static_k = types.ReplyKeyboardMarkup(resize_keyboard = True)

static_k.add('Статистика в России 🇷🇺')
static_k.add('Статистика в мире 🌍')
static_k.add('Узнать статистику в любой стране')
static_k.add('Вернуться к главному меню 🔄')


info_k = types.ReplyKeyboardMarkup(resize_keyboard = True)

info_k.add('Используемые ресурсы')
info_k.add('Вернуться к главному меню 🔄')


find_k = types.ReplyKeyboardMarkup(resize_keyboard = True)

find_k.add('Вернуться к главному меню 🔄')

z_k = types.ReplyKeyboardMarkup(True)


date = ""


# functions

def get_bot_token()->str:
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    return cfg["bot_data"]["token"]


def word_filter(text:str)->bool:
	for word_on_message in text.lower().split():
		if word_on_message in words:
			return True
	return False


def update_data():
	global db, date
	date = datetime.datetime.today().strftime('%d.%m')
	db = {}
	data = webparser.get_data()
	for country in data:
		base = data[country]
		country = base["country"]
		population = base["population"]
		all = base["total_cases"]
		active = base["active_cases"]
		recover = base["total_recovered"]
		death = base["total_deaths"]
		new_case = base["new_cases"]
		new_death = base["new_deaths"]
		new_recover = base["new_recovered"]
		db[country.lower()] = [country, population, all, active, recover, death, new_case, new_recover, new_death]


def get_data(country:str, text:str)->str:
	data = db[country.lower()]
	if text.lower() in ["world", "мир"] or country in ["world", "мир"]:
		return f"Статистика в мире 🌍 на {date}\n\nВсего заразились 😷: {data[2]}\nСейчас болеют 😷: {data[3]}\nВыздовели ✅: {data[4]}\nУмерли 💀: {data[5]}\n\nЗа последние 24 часа 🕓\nЗаболели 😷: {data[6]}\nВыздовели ✅: {data[7]}\nУмерли 💀: {data[8]}"
	if text.lower() in ["russia", "россия"]:
		text = 'России 🇷🇺'
	return f"Статистика в {text.title()} на {date}\n\nНаселение {data[1]} человек\n\nВсего заразились 😷: {data[2]}\nСейчас болеют 😷: {data[3]}\nВыздовели ✅: {data[4]}\nУмерли 💀: {data[5]}\n\nЗа последние 24 часа 🕓\nЗаболели 😷: {data[6]}\nВыздовели ✅: {data[7]}\nУмерли 💀: {data[8]}"
