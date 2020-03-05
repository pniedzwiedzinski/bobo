import os
import requests
import codecs
import json
from datetime import datetime

from holidays import get_today_holiday
from lesson import get_lessons_start, get_lessons_end, LESSON_HOURS

# Pobieranie wrażliwych danych z konfiguracji systemu
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def get_name(number):
    with codecs.open('./config.json', "r", "utf-8") as f:
        data = json.load(f)
    if number in data:
        return data[number]
    return number

def get_lessons():
    r = requests.get("https://kapskypl.github.io/planyn-backend/classes/3E.json")
    table = r.json()
    today = table[datetime.today().weekday()]
    lessons = [ lesson for lesson in today if lesson ]
    return lessons

# Ta funkcja pobiera szczęśliwy numerek z https://get-lucky.netlify.com/
def get_lucky():
    r = requests.get("https://get-lucky.netlify.com/.netlify/functions/get")
    r = r.json()
    return r["data"]["luckyNumber"], r["data"]["date"]

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


def main():
    lucky, date = get_lucky()
    send_msg(f"<b>Szczesliwy numerek: {get_name(str(lucky))} ({lucky})</b>")

    start_hour = get_lesson_start()
    end_hour = get_lesson_end    
    send_msg("Dzisiaj lekcje trwają od " + (LESSON_HOURS[start_hour]["start"]) + " do " + (LESSON_HOURS[end_hour]["end"])
    
    try:
        holiday, link = get_today_holiday()
        send_msg(f"Dzisiaj jest: <a href=\"{link}\">{holiday.upper()}</a>")
    except:
        return

main()
