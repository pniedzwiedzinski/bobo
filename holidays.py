#!/usr/bin/env python3
#
"""
Ten moduł służy do pobierania dzisiejszego nietypowego święta
"""

import requests
from datetime import datetime

months = {
    1: "stycznia",
    2: "lutego",
    3: "marca",
    4: "kwietnia",
    5: "maja",
    6: "czerwca",
    7: "lipca",
    8: "sierpnia",
    9: "września",
    10: "października",
    11: "listopada",
    12: "grudnia"
}

def get_holiday(month: int, day: int) -> (str, str):
    r = requests.get(f"https://pniedzwiedzinski.github.io/kalendarz-swiat-nietypowych/{month}/{day}.json")
    holidays = r.json()
    return holidays[0]["name"], f"https://nonsa.pl/wiki/{day}_{months[month]}"

def get_today_holiday() -> (str, str):
    now = datetime.today()
    return get_holiday(now.month, now.day)
