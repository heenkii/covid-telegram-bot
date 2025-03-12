import sqlite3
from utils import webparser

from datetime import datetime
from config import DATABASE


class Database:

    def __init__(self) -> None:
        self.db = sqlite3.connect(DATABASE)
        self.sql = self.db.cursor()
        self.sql.execute(
            """CREATE TABLE IF NOT EXISTS covid_data (
            country_ru TEXT,
            country_en TEXT,
            date_update TEXT,
            population TEXT,
            total_case TEXT,
            active_case TEXT,
            total_recover TEXT,
            total_death TEXT,
            new_case TEXT,
            new_recover TEXT,
            new_death TEXT);"""
        )
        self.db.commit()

    def get_country_data(self, country) -> dict or bool:
        query_en = "SELECT * FROM covid_data WHERE country_en = ?"
        query_ru = "SELECT * FROM covid_data WHERE country_ru = ?"
        answer_en = self.sql.execute(query_en, (country,)).fetchall()
        answer_ru = self.sql.execute(query_ru, (country,)).fetchall()
        answer = answer_en + answer_ru
        if answer == []:
            return False
        answer = list(answer[0])
        country_data = {
            "country_ru": answer[0],
            "country_en": answer[1],
            "date_update": answer[2],
            "population": answer[3],
            "total_case": answer[4],
            "active_case": answer[5],
            "total_recover": answer[6],
            "total_death": answer[7],
            "new_case": answer[8],
            "new_recover": answer[9],
            "new_death": answer[10],
        }
        return country_data

    def get_all_countries(self) -> list:
        query = "SELECT country_en FROM covid_data"
        answer = self.sql.execute(query).fetchall()
        answer = list(map(lambda word: word[0], answer))
        return answer

    def update_data(self) -> bool:
        try:
            parse_data = webparser.get_data()
            db_countries = self.get_all_countries()
            update_date = datetime.now().strftime("%d.%m")
            for country in parse_data:
                country = country.strip().lower()
                if country in db_countries:
                    query = f"""UPDATE covid_data SET
                    date_update = ?,
                    population = ?,
                    total_case = ?,
                    active_case = ?,
                    total_recover = ?,
                    total_death = ?,
                    new_case = ?,
                    new_recover = ?,
                    new_death = ?
                    WHERE country_en = ?"""
                    self.sql.execute(
                        query,
                        [
                            update_date,
                            parse_data[country]["population"],
                            parse_data[country]["total_case"],
                            parse_data[country]["active_case"],
                            parse_data[country]["total_recover"],
                            parse_data[country]["total_death"],
                            parse_data[country]["new_case"],
                            parse_data[country]["new_recover"],
                            parse_data[country]["new_death"],
                            country,
                        ],
                    )
                    self.db.commit()
            return True
        except:
            return False

    def close(self) -> None:
        self.db.close()
