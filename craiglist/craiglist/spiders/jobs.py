import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
import time


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["newyork.craigslist.org"]
    start_urls = ('https://newyork.craigslist.org/search/egr',) #only when response is set

    def parse(self, response):
        path = '/Users/daianeklein/Documents/DS/scrapy/chrome_driver'
        self.driver = webdriver.Chrome(path + 'chromedriver')
        self.driver.get('https://newyork.craigslist.org/search/egr')
        time.sleep(3)

        sel = Selector(text=self.driver.page_source)
        job_urls = sel.xpath('//li[@class="cl-search-result cl-search-view-mode-thumb"]//a[@class="titlestring"]/@href').extract()
        job_titles = sel.xpath('//li[@class="cl-search-result cl-search-view-mode-thumb"]//a[@class="titlestring"]/text()').extract()
        
        for job_url, job_title in zip(job_urls, job_titles):
            yield { 'job_title' : job_title,
                    'job_url' : job_url}


    #link
    #sel.xpath('//li[@class="cl-search-result cl-search-view-mode-thumb"]//a[@class="titlestring"]/@href').extract()

    #titulo
    #sel.xpath('//li[@class="cl-search-result cl-search-view-mode-thumb"]//a[@class="titlestring"]/text()').extract_first()
