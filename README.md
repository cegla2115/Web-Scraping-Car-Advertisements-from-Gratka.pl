# WebScraping Car Advertisements from Gratka.pl
The project involves scraping data from the website "https://gratka.pl/motoryzacja/osobowe?page=1" which is a section of the website Gratka.pl dedicated to advertisements for personal vehicles. The scraped data includes various details about car advertisements such as the link, name of the car, mileage (Przebieg), engine capacity (Pojemność silnika [cm3]), production year (rok produkcji), fuel type (rodzaj paliwa), and price (cena). 
To do this were used three scrapers: one using Beautiful Soup, one using Scrapy, one using Selenium (each in a separate folder). All of them scrap the same information.
## In description.pdf you can see a description of:
- the project, 
- all scraper mechanics,
- the output,
- elementary data analysis.

## In soup folder you have both .ipynb and .py files. To run them you should:
1. Open a command prompt or terminal and install Beautiful Soup if you haven't already: 
'pip install beautifulsoup4'
2. Run the BS file, and the data will be scraped and saved to a CSV file named advertisements.csv.

## In scrapy folder you have both .ipynb and .py files. To run them you should:
1. Open a command prompt or terminal and install Scrapy if you haven't already: 
'pip install scrapy'
2. Navigate to the scrapy folder: cd path_to_scrapy_folder
3. Run the scraper by executing the following command in the terminal: 
'scrapy crawl adverts'
or if you want to save it as .CSV:
'scrapy crawl adverts -o adverts.csv'
After the scraping process is complete, you will find the scraped data saved in a CSV file named adverts.csv.

## In selenium folder you have both .ipynb and .py files. To run them you should:
1. Open a command prompt or terminal and install Selenium if you haven't already: 
'pip install selenium'
2. Download the Chrome WebDriver from the official website (https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory on your machine.
3. Update the DRIVER_PATH variable with the path to the Chrome WebDriver executable you downloaded.
4. Run the Selenium file, and the data will be scraped and saved to a CSV file named gratka.csv.
