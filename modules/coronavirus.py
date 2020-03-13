"""
Ten moduł służy do wysyłania informacji o koronawirusie
"""

import requests
from bs4 import BeautifulSoup


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

        country = row.findAll("td")[0].contents[0]
        if len(country) == 1:
            try:
                country = row.findAll("td")[0].a.contents[0]
            except:
                country = "Diamond Princess"

        countries[country.strip()]=numbers

    message = "BIEŻĄCE INFORMACJE O KORONAWIRUSIE\n\n"
    message += "POLSKA, zarażeni: " + str(countries["Poland"][0]).replace(".0","") + "\n"
    message += "POLSKA, wyleczeni: " + str(countries["Poland"][4]).replace(".0","") + "\n"
    message += "POLSKA, śmierci: " + str(countries["Poland"][2]).replace(".0","") + "\n\n"
    total_victims = 0
    total_recovered = 0
    total_deaths = 0
    for country in countries:
        total_victims += countries[country][0]
        total_recovered += countries[country][4]
        total_deaths += countries[country][2]
    message += "ŚWIAT, zarażeni: " + str(total_victims).replace(".0","") + "\n"
    message += "ŚWIAT, wyleczeni: " + str(total_recovered).replace(".0","") + "\n"
    message += "ŚWIAT, śmierci: " + str(total_deaths).replace(".0","") + "\n"
    return message
