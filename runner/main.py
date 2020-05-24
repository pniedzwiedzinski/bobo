import os
import json
import requests
from time import sleep

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

api = f"https://api.telegram.org/{TOKEN}"
data = {
   "chat_id": CHAT_ID,
}


store = {}
with open("store.json", "r") as f:
    store = json.load(f)

received = set()

def dump_store():
    with open("store.json", "w") as f:
        json.dump(store, f)

def get_updates():
    r = requests.post(f"{api}/getUpdates", data=data)
    resp = r.json()
    return resp["result"]

def _send_msg(msg):
    d = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    }
    r = requests.post(f"{api}/sendMessage", data=d)

def send_msg(name, id):
    _send_msg(f"Zarejestrowano <a href=\"tg://user?id={id}\">@{name}</a>")



def main():
    updates = get_updates()

    for update in updates:
        msg = update["message"]

        if update["update_id"] not in received and "text" in msg:
            if msg["text"] == ("/kurwa_spock"):
                user = msg["from"]
                name = user["first_name"]
                if "last_name" in user:
                    name += ' ' + user["last_name"]
                id = str(user["id"])
                if id not in store:
                    store[id] = name
                    send_msg(name, id)
                    dump_store()
                    print(store[id])
            elif msg["text"] == "/all":
                m = [f"<a href=\"tg://user?id={id}\">@{name}</a>" for id, name in store.items()]
                _send_msg(' '.join(m))
            elif msg["text"] == "/shrug":
                _send_msg("¯\_(ツ)_/¯")
            received.add(update["update_id"])





if __name__ == "__main__":
    while True:
        main()
        sleep(10)

