import scrapy

class AdvertsSpider(scrapy.Spider):
    # Spider configuration
    name = "adverts"  # Spider name
    allowed_domains = ["gratka.pl"]  # List of allowed domains
    #start_urls = [f'https://gratka.pl/motoryzacja/osobowe?page={i+1}' for i in range(0, 15)]  # URLs to start scraping
    start_urls = [f'https://gratka.pl/motoryzacja/osobowe?page={i+1}' for i in range(0, 2)] 

    def parse(self, response):
        # Parse method to handle the response from each URL
        for link in response.css('div.listing__teaserWrapper a::attr(href)'):
            # Extract the URL of each individual car advertisement
            advert_url = response.urljoin(link.get())
            yield scrapy.Request(advert_url, callback=self.parse_advert)

    def parse_advert(self, response):
        # Parse method to extract specific details from each car advertisement
        yield {
            'Link': response.url,  # URL of the advertisement
            'Name': response.css('h1.sticker__title::text').get().strip(),  # Name of the car
            'Mileage': response.css('ul.parameters__singleParameters li:contains("Przebieg") b.parameters__value::text').get(),  # Mileage
            'Engine Capacity': response.css('ul.parameters__singleParameters li:contains("Pojemność silnika [cm3]") b.parameters__value::text').get(),  # Engine capacity in cubic centimeters
            'Year of manufacture': response.css('ul.parameters__singleParameters li:contains("Rok produkcji") b.parameters__value::text').get(),  # Production year
            'Fuel type': response.css('ul.parameters__singleParameters li:contains("Rodzaj paliwa") b.parameters__value::text').get(),  # Fuel type
            'Price': response.css('span.priceInfo__value::text').get().strip(),  # Price of the car
        }







        


