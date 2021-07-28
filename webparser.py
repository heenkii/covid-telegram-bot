import requests as rq
from bs4 import BeautifulSoup as BS

def get_data()->dict:
    url = "https://www.worldometers.info/coronavirus/"
    html = rq.get(url).text
    soup = BS(html, "html.parser")

    db = {}

    for el in soup.select(".main_table_countries_div > .table-bordered > tbody")[:2]:
        for unit in el.select("tr"):
            data = []
            for s in unit.find_all("td"):
                n = s.get_text().strip().replace(",", ".").replace("+", "").replace("N/A", "")
                if n == "":
                    n = "0"
                data += [n]
            data = data[1:15]
            # country, population, total_cases, active_cases, total_recovered, total_death, new_cases, new_recovered, new_deaths
            if not(data[0].isdigit()) and data[0].strip() != "Total:":
                db[data[0].lower()] = [data[0], data[13], data[1], data[7], data[5], data[3], data[2], data[6], data[4]]
    return db
