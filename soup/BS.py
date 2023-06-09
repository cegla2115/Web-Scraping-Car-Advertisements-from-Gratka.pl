import csv
from urllib import request
from bs4 import BeautifulSoup as BS

scrape_100 = False

base_url = 'https://gratka.pl/motoryzacja/osobowe?page='

# Step 1: Extract links and save to CSV
with open('advertisements.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['link', 'name', 'przebieg', 'Pojemność silnika [cm3]', 'rok produkcji', 'rodzaj paliwa', 'cena']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for page in range(1, 21):
        url = base_url + str(page)
        html = request.urlopen(url)
        bs = BS(html.read(), 'html.parser')

        tags = bs.find_all('a', class_='teaserLink')

        for tag in tags:
            link = tag['href']
            writer.writerow({'link': link})

# Step 2: Extract names and Przebieg values, and update CSV
with open('advertisements.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)[0:100] if scrape_100 else list(reader)

with open('advertisements.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['link', 'name', 'przebieg', 'Pojemność silnika [cm3]', 'rok produkcji', 'rodzaj paliwa', 'cena']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        link = row['link']
        html = request.urlopen(link)
        bs = BS(html.read(), 'html.parser')

        # name
        name_element = bs.find('h1', class_='sticker__title')
        if name_element:
            name = name_element.get_text(strip=True)
        else:
            print(f"No name element found for link: {link}")
            name = "NaN"

        # przebieg
        przebieg_element = bs.find('span', text='Przebieg')
        if przebieg_element:
            przebieg = przebieg_element.find_next('b', class_='parameters__value').get_text(strip=True)
        else:
            przebieg = "NaN"

        # pojemnosc silnika
        poj_element = bs.find('span', text='Pojemność silnika [cm3]')
        if poj_element:
            poj = poj_element.find_next('b', class_='parameters__value').get_text(strip=True)
        else:
            poj = "NaN"

        # rok produkcji
        rok_element = bs.find('span', text='Rok produkcji')
        if rok_element:
            rok = rok_element.find_next('b', class_='parameters__value').get_text(strip=True)
        else:
            rok = "NaN"

        # paliwo
        paliwo_element = bs.find('span', text='Rodzaj paliwa')
        if paliwo_element:
            paliwo = paliwo_element.find_next('b', class_='parameters__value').get_text(strip=True)
        else:
            paliwo = "NaN"

        # cena
        cena_element = bs.find('span', class_='priceInfo__value')
        if cena_element:
            cena = cena_element.get_text(strip=True)
            currency_element = cena_element.find('span', class_='priceInfo__currency')
        else:
            cena = "NaN"

        # to csv
        writer.writerow({'link': link, 'name': name, 'przebieg': przebieg, 'Pojemność silnika [cm3]': poj, 'rok produkcji': rok, 'rodzaj paliwa': paliwo, 'cena': cena})