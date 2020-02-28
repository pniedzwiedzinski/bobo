#!/usr/bin/env python3
#
"""
Ten moduł służy do pobierania dzisiejszego nietypowego święta
"""

import requests
from datetime import datetime

def get_holiday(month: int, day: int) -> str:
    r = requests.get(f"https://pniedzwiedzinski.github.io/kalendarz-swiat-nietypowych/{month}/{day}.json")
    holidays = r.json()
    return holidays[0]["name"]

def get_today_holiday() -> str:
    now = datetime.today()
    return get_holiday(now.month, now.day)
