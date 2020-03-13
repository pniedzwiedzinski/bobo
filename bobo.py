import os
import requests
import codecs
import json
from datetime import datetime
from bs4 import BeautifulSoup

from modules.holidays import get_today_holiday
from modules.lesson import get_lessons_start, get_lessons_end, LESSON_HOURS
from modules.lucky import get_lucky

# Pobieranie wrażliwych danych z konfiguracji systemu
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def get_name(number):
    with codecs.open('./config.json', "r", "utf-8") as f:
        data = json.load(f)
    if number in data:
        return data[number]
    return number

def send_msg(msg: str) -> str:
    # Format wiadomości wymagany przez telegrama
    data = {
        "chat_id": f"-{CHAT_ID}",
        "text": msg,
        "parse_mode": "HTML",
    }

    # Wysłanie wiadomości
    r = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data=data)
    # Print który wypisuje odpowiedź od serwera telegrama
    print(r.text)

def coronavirus():
    countries = {}
    for row in rows:
        cols = row.findAll("td")[1:]
        numbers = []
        for col in cols:
            if len(col.contents) > 0:
                number = str(col.contents[0])
                if "+" in  number:
                    number = number.replace("+","")
                if "," in number:
                    number = number.replace(",","")
                try:
                    numbers.append(float(number))
                except:
                    numbers.append(0.0)
            else:
                numbers.append(0.0)

        country = row.findAll("td")[0].contents[0]
        if len(country) == 1:
            try:
                country = row.findAll("td")[0].a.contents[0]
            except:
                country = "Diamond Princess"

        countries[country.strip()]=numbers
        
    message = "BIEŻĄCE INFORMACJE O KORONAWIRUSIE\n\n"
    message += "POLSKA, zarażeni: " + str(countries["Poland"][0]).replace(".0","") + "\n"
    message += "POLAND, wyleczeni: " + str(countries["Poland"][4]).replace(".0","") + "\n"
    message += "POLAND, śmierci: " + str(countries["Poland"][2]).replace(".0","") + "\n\n"
    total_victims = 0
    total_recovered = 0
    total_deaths = 0
    for country in countries:
        total_victims += countries[country][0]
        total_recovered += countries[country][4]
        total_deaths += countries[country][2]
    message += "ŚWIAT, zarażeni: " + str(total_victims).replace(".0","") + "\n"
    message += "ŚWIAT, wyleczeni: " + str(total_recovered).replace(".0","") + "\n"
    message += "ŚWIAT, śmierci: " + str(total_deaths).replace(".0","") + "\n"
    return message

def main():
    #lucky = get_lucky()
    #send_msg(f"<b>Szczesliwy numerek: {get_name(str(lucky))} ({lucky})</b>")

    #start_hour = get_lessons_start()
    #end_hour = get_lessons_end()
    #send_msg("Dzisiaj lekcje trwają od " + (LESSON_HOURS[start_hour]["start"]) + " do " + (LESSON_HOURS[end_hour]["end"]))

    try:
        holiday, link = get_today_holiday()
        send_msg(f"Dzisiaj jest: <a href=\"{link}\">{holiday.upper()}</a>")
    except:
        return

main()
