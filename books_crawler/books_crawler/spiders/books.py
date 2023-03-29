
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

# class BooksSpider(CrawlSpider):
#     name = "books"
#     allowed_domains = ["books.toscrape.com"]
#     start_urls = (
#                 "http://books.toscrape.com/",
#             )

#     rules = (Rule(LinkExtractor(allow=('music')), callback = 'parse_page', follow = False),)

#     def parse_page(self, response):
#         pass

from time import sleep
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException

class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/Users/daianeklein/Documents/DS/scrapy/chrome_driver/chrome_driver')
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h2/a/@href').extract()

        for book in books:
            url = 'http://books.toscrape.com' + book
            yield Request(url, callback=self.parse_book)

        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                sleep(3)
                self.logger.info('Sleeping for 3 seconds')
                next_page.click()

                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h2/a/@href').extract()
                
                for book in books:
                    url = 'http://books.toscrape.com/catalogue/' + book
                    
                    yield Request(url, callback=self.parse_book)


            except NoSuchElementException:
                self.logger.info('No more pages to load')
                self.driver.quit()
                break

    def parse_book(self, response):
        pass
