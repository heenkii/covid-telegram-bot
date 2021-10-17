import datetime, requests as rq
from bs4 import BeautifulSoup as BS

def get_data()->dict:
    url = "https://www.worldometers.info/coronavirus/"
    html = rq.get(url).text
    soup = BS(html, "html.parser")

    date = datetime.datetime.today().strftime("%d.%m")
    db = {"date" : date}

    for el in soup.select(".main_table_countries_div > .table-bordered > tbody")[:2]:
        for unit in el.select("tr"):
            data = []
            for s in unit.find_all("td"):
                n = s.get_text().strip().replace(",", ".").replace("+", "")
                if n in ["", "N/A"]:
                    n = " -"
                data += [n]
            data = data[1:15]
            # country, population, total_cases, active_cases, total_recovered, total_death, new_cases, new_recovered, new_deaths
            if not(data[0].isdigit()) and data[0].strip() != "Total:":
                db[data[0].lower()] = {
                "country" : data[0],
                "population" : data[13],
                "total_cases" : data[1],
                "active_cases" : data[7],
                "total_recovered" : data[5],
                "total_death" : data[3],
                "new_cases" : data[2],
                "new_recovered" : data[6],
                "new_deaths" : data[4],
                }
    return db
