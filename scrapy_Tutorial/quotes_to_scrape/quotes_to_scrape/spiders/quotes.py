import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        
        title = all_div_quotes.css('span.text::text').extract()
        quotes = all_div_quotes.css('.author::text').extract()
        tag = all_div_quotes.css('.tag::text').extract()

        yield {'title' : title,
                'quotes' : quotes,
                'tag' : tag}





        #author = response.css('author::text').extract()
        # author = response.xpath('//*[@class="author"]/text()').extract()
        # page_number = response.css('li.next a').xpath('@href').extract()
        
        # yield {'Author' : author,
        #         'page_number' : page_number }