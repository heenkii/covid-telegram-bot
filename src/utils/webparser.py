import requests as rq
from bs4 import BeautifulSoup as BS


def split_num(num: int) -> str:
    num = str(num)
    for ind in range(len(num), 0, -3):
        if ind != len(num):
            num = num[:ind] + " " + num[ind:]
    return num


def get_data() -> dict:
    url = "https://www.worldometers.info/coronavirus/"
    html = rq.get(url).text
    soup = BS(html, "html.parser")

    db = {}

    elements = soup.select(".table-bordered > tbody")[:2]

    for el in elements:
        for unit in el.select("tr"):
            data = []
            for s in unit.find_all("td"):
                n = (s.get_text()
                     .strip().replace(",", "")
                     .replace("+", ""))
                if n in ["", "N/A"]:
                    n = "-"
                data += [n]
            data = data[1:15]
            # country, population, total_cases,
            # active_cases, total_recovered, total_death,
            # new_cases, new_recovered, new_deaths
            if data[0]:
                if not (data[0].isdigit()) and data[0].strip() != "Total:":
                    db[data[0].lower()] = {
                        "country": data[0],
                        "population": split_num(data[13]),
                        "total_case": split_num(data[1]),
                        "active_case": split_num(data[7]),
                        "total_recover": split_num(data[5]),
                        "total_death": split_num(data[3]),
                        "new_case": split_num(data[2]),
                        "new_recover": split_num(data[6]),
                        "new_death": split_num(data[4]),
                    }
    return db
