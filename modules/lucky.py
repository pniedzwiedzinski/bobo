"""
This module gets the lucky number.
"""

import requests

old_API_URL = "https://zsk-poznan.github.io/szczesliwy-numerek-backend"
API_URL = "https://get-lucky.netlify.app/.netlify/functions/get"

def old_get_lucky():
    r = requests.get(old_API_URL)
    r = r.json()
    return r["TK"]

def get_lucky():
    r = requests.get(API_URL)
    r = r.json()
    if "data" in r:
        return r["data"]["luckyNumber"]
    return 0
