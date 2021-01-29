"""
Obliczanie dni do matury 2021
"""

from datetime import datetime

def days_to(d1):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.now()
    return abs((d2 - d1).days)

def do_matury():
    return f"Do matury zostało {days_to('2021-05-05')} dni 🎉"
