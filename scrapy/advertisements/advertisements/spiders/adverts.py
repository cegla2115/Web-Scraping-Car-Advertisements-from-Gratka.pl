import scrapy

class AdvertsSpider(scrapy.Spider):
    name = "adverts"
    allowed_domains = ["gratka.pl"]
    start_urls = [f'https://gratka.pl/motoryzacja/osobowe?page={i+1}' for i in range(0, 15)]

    scrape_100 = True
    scrape_count = 0
    limit = 100

    def parse(self, response):
        for link in response.css('div.listing__teaserWrapper a::attr(href)'):
            advert_url = response.urljoin(link.get())
            yield scrapy.Request(advert_url, callback=self.parse_advert)

    def parse_advert(self, response):
        self.scrape_count += 1

        yield {
            'Link': response.url,
            'Name': response.css('h1.sticker__title::text').get().strip(),
            'Mileage': response.css('ul.parameters__singleParameters li:contains("Przebieg") b.parameters__value::text').get(),
            'Engine Capacity': response.css('ul.parameters__singleParameters li:contains("Pojemność silnika [cm3]") b.parameters__value::text').get(),
            'Year of manufacture': response.css('ul.parameters__singleParameters li:contains("Rok produkcji") b.parameters__value::text').get(),
            'Fuel type': response.css('ul.parameters__singleParameters li:contains("Rodzaj paliwa") b.parameters__value::text').get(),
            'Price': response.css('span.priceInfo__value::text').get().strip(),
        }

        if self.scrape_100 and self.scrape_count >= self.limit:
            raise scrapy.exceptions.CloseSpider('Reached the limit of 100 advertisements')


