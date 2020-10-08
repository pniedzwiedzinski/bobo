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
    message += "POLSKA, śmierci: " + str(countries["Poland"][3]).replace(".0","") + " (+" + str(countries["Poland"][4]).replace(".0","") + ")\n\n"
    message += "ŚWIAT, zarażeni: " + str(countries["World"][1]).replace(".0","") + " (+" + str(countries["World"][2]).replace(".0","") + ")\n"
    message += "ŚWIAT, aktywne: " + str(countries["World"][7]).replace(".0","") + "\n"
    message += "ŚWIAT, śmierci: " + str(countries["World"][3]).replace(".0","") + " (+" + str(countries["World"][4]).replace(".0","") + ")\n\n"
    return message
