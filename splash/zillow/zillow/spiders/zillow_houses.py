import scrapy
from ..utils import URL

class ZillowHousesSpider(scrapy.Spider):
    name = "zillow_houses"
    allowed_domains = ["www.zillow.com"]
    start_urls = [URL]
    handle_httpstatus_list = [403]

    def parse(self, response):
        print(response.body)
