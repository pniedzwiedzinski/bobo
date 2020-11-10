"""
This module gets the lucky number.
"""

import requests

API_URL = "https://zsk-poznan.github.io/szczesliwy-numerek-backend"
old_API_URL = "https://get-lucky.netlify.app/.netlify/functions/get"

def get_lucky():
    r = requests.get(API_URL)
    r = r.json()
    return r["TK"]

def old_get_lucky():
    r = requests.get(old_API_URL)
    r = r.json()
    if "data" in r:
        return r["data"]["luckyNumber"]
    return 0
