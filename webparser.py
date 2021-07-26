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
            if not(data[0].isdigit()) and data[0].strip() != "Total:":
                db[data[0].lower()] = {"country":data[0], "total_cases":data[1], "new_cases":data[2],
                "total_deaths":data[3], "new_deaths":data[4], "total_recovered":data[5],
                "new_recovered":data[6], "active_cases":data[7], "population":data[13]}
    return db
