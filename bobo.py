import os
import requests

# Pobieranie wrażliwych danych z konfiguracji systemu
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

# Ta funkcja pobiera szczęśliwy numerek z https://get-lucky.netlify.com/
def get_lucky():
    r = requests.get("https://get-lucky.netlify.com/.netlify/functions/get")
    r = r.json()
    return r["data"]["luckyNumber"], r["data"]["date"]

def main():
    lucky, date = get_lucky()
    message = f"<b style="color: red">Szczesliwy numerek: {lucky}</b>"

    # Format wiadomości wymagany przez telegrama
    data = {
        "chat_id": f"-{CHAT_ID}",
        "text": message,
        "parse_mode": "HTML",
    }

    # Wysłanie wiadomości
    r = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data=data)
    # Print który wypisuje odpowiedź od serwera telegrama
    print(r.text)

main()

