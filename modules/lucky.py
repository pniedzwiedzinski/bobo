"""
This module gets the lucky number.
"""

import requests

API_URL = "https://zsk-poznan.github.io/szczesliwy-numerek-backend"

def get_lucky():
    r = requests.get(API_URL)
    r = r.json()
    return r["TK"]

