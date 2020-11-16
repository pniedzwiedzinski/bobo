"""
Ten moduł służy do wysyłania informacji o koronawirusie
"""

import requests
from bs4 import BeautifulSoup
import re
from datetime import date

def coronavirus_tests():
    url = "https://koronawirusunas.pl/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    today = date.today().strftime("%d.%m.%Y")
    result = re.search(rf"przyrost_testy.*\n.*?{{.*?{re.escape(today)}.*?p_testy:\s?(\d*)", str(soup))
    new_tests = result.groups()[0]
    all_tests = soup.find(class_="badge-testy").text.replace(" ", "")
    return {"new": int(new_tests), "all": int(all_tests)}

def coronavirus():
    url = "https://www.worldometers.info/coronavirus/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find("tbody")
    rows = table.findAll("tr", attrs={"style":""})
    countries = {}
    for row in rows:
        cols = row.findAll("td")[1:]
        numbers = []
        for col in cols:
            if len(col.contents) > 0:
                number = str(col.contents[0])
                if "+" in  number:
                    number = number.replace("+","")
                if "," in number:
                    number = number.replace(",","")
                try:
                    numbers.append(float(number))
                except:
                    numbers.append(0.0)
            else:
                numbers.append(0.0)

        try:
            country = row.findAll("td")[1].a.contents[0]
        except:
            try:
                country =  row.findAll("td")[1].span.contents[0]

            except:
                country = row.findAll("td")[1].contents[0]


        countries[country.strip()]=numbers

    message = "BIEŻĄCE INFORMACJE O KORONAWIRUSIE\n\n"
    message += "POLSKA, zarażeni: " + str(countries["Poland"][1]).replace(".0","") + " (+" + str(countries["Poland"][2]).replace(".0","") + ")\n"
    message += "POLSKA, aktywne: " + str(countries["Poland"][7]).replace(".0","") + "\n"
    message += "POLSKA, śmierci: " + str(countries["Poland"][3]).replace(".0","") + " (+" + str(countries["Poland"][4]).replace(".0","") + ")\n"
    try:
        tests = coronavirus_tests()
        message += "POLSKA, testy: " + str(tests["all"]) + " (+" + str(tests["new"]) + ")\n"
        message += "POLSKA, testy pozytywne: " + str(round(countries["Poland"][1]/tests["all"]*100, 2)) + "% (" + str(round(countries["Poland"][2]/tests["new"]*100, 2)) + "%)\n\n"
    except:
        message += "POLSKA testy: nie udało się pobrać danych\n\n"
    message += "ŚWIAT, zarażeni: " + str(countries["World"][1]).replace(".0","") + " (+" + str(countries["World"][2]).replace(".0","") + ")\n"
    message += "ŚWIAT, aktywne: " + str(countries["World"][7]).replace(".0","") + "\n"
    message += "ŚWIAT, śmierci: " + str(countries["World"][3]).replace(".0","") + " (+" + str(countries["World"][4]).replace(".0","") + ")\n\n"
    print(message)
    return message

coronavirus()
