# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import numpy as np
import pandas as pd

scrape_100 = False

# Driver's path
DRIVER_PATH='C:/Users/KacperSokolowski/Desktop/&&&/chrome_driver/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Accept cookies
site='https://gratka.pl/'
driver.get(site)
sleep(2)
driver.find_element(By.XPATH, '//button[@aria-label="accept and close"]').click()
sleep(1)

# Get announcements
urls_list = [f'https://gratka.pl/motoryzacja/osobowe?page={i+1}' for i in range(0,15)]

announcements_links = []

for url in urls_list:
    driver.get(url)
    sleep(2)
    ts = driver.find_elements(By.XPATH, '//a[@data-cy="teaserLink"]')
    for t in ts:
        announcements_links.append(t.get_attribute('href'))

# Remove duplicated links (if any)
announcements_links = list(dict.fromkeys(announcements_links))

# Containers for storing scrapped information
price            = []
title            = []
km               = []
engine_capacity  = []
manufacture_year = []
fuel_type        = []
link             = []

limit = 100 if scrape_100 else len(announcements_links)

# Loop through all announcements
for i in range(0,limit):
    # Open new announcement
    new_site = announcements_links[i]
    driver.get(new_site)
    sleep(2)
    
    # Get required information
    try:
        price_cont = driver.find_element(By.XPATH, '//span[@class="priceInfo__value"]').text
    except:
        price_cont = ''
    try:
        title_cont = driver.find_element(By.XPATH, '//h1[@data-cy="offerTitle"]').text
    except:
        title_cont = ''
    try:
        km_cont = driver.find_element(By.XPATH, '//li/span[.="Przebieg"]/following-sibling::b[@class="parameters__value"]').text
    except:
        km_cont = ''
    try:
        engine_capacity_cont = driver.find_element(By.XPATH, '//li/span[.="Pojemność silnika [cm3]"]/following-sibling::b[@class="parameters__value"]').text
    except:
        engine_capacity_cont = ''
    try:
        manufacture_year_cont = driver.find_element(By.XPATH, '//li/span[.="Rok produkcji"]/following-sibling::b[@class="parameters__value"]').text
    except:
        manufacture_year_cont = ''
    try:
        fuel_type_cont = driver.find_element(By.XPATH, '//li/span[.="Rodzaj paliwa"]/following-sibling::b[@class="parameters__value"]').text
    except:
        fuel_type_cont = ''
    
    # Save results
    price.append(price_cont)
    title.append(title_cont)
    km.append(km_cont)
    engine_capacity.append(engine_capacity_cont)
    manufacture_year.append(manufacture_year_cont)
    fuel_type.append(fuel_type_cont)
    link.append(new_site)

# Close driver
driver.close()

# Create data frame
df = pd.DataFrame({
    "link": link,
    "price": price,
    "title": title,
    "km": km,
    "engine_capacity": engine_capacity,
    "manufacture_year": manufacture_year,
    "fuel_type": fuel_type
})

# Save results
df.to_csv('C:/Users/KacperSokolowski/Desktop/gratka.csv',
          na_rep='NaN',
          index=False,
          encoding='utf-8'
)