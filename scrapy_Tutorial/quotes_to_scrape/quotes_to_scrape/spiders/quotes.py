import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        #author = response.css('author::text').extract()
        author = response.xpath('//*[@class="author"]/text()').extract()
        page_number = response.css('li.next a').xpath('@href').extract()
        
        yield {'Author' : author,
                'page_number' : page_number }