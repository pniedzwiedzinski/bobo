import os
import requests

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def get_lucky():
    r = requests.get("https://get-lucky.netlify.com/.netlify/functions/get")
    r = r.json()
    return r["data"]["luckyNumber"], r["data"]["date"]

def main():
    lucky, date = get_lucky()
    message = f"<b>Szczesliwy numerek: {lucky}</b>"

    data = {
        "chat_id": f"-{CHAT_ID}",
        "text": message,
        "parse_mode": "HTML",
    }

    r = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data=data)
    print(r.text)

main()

