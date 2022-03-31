import datetime
import requests as rq
from bs4 import BeautifulSoup as BS


def get_data() -> dict:
    url = "https://www.worldometers.info/coronavirus/"
    html = rq.get(url).text
    soup = BS(html, "html.parser")

    db = {}

    for el in soup.select(".main_table_countries_div > .table-bordered > tbody")[:2]:
        for unit in el.select("tr"):
            data = []
            for s in unit.find_all("td"):
                n = s.get_text().strip().replace(",", "").replace("+", "")
                if n in ["", "N/A"]:
                    n = None
                data += [n]
            data = data[1:15]
            # country, population, total_cases, active_cases, total_recovered, total_death, new_cases, new_recovered, new_deaths
            if data[0] != None:
                if not(data[0].isdigit()) and data[0].strip() != "Total:":
                    db[data[0].lower()] = {
                        "country": data[0],
                        "population": data[13],
                        "total_case": data[1],
                        "active_case": data[7],
                        "total_recover": data[5],
                        "total_death": data[3],
                        "new_case": data[2],
                        "new_recover": data[6],
                        "new_death": data[4],
                    }
    return db
