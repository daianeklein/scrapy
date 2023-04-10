import scrapy


class TableSpider(scrapy.Spider):
    name = "table"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population"]

    def parse(self, response):
        table = response.xpath('//table[contains(@class, "wikitable sortable")]')[0]
        trs = table.xpath('//tr')[2:]

        ranks = trs.xpath('//span[@data-sort-value]/text()').extract()
        states = trs.xpath('//tr/th/a/text()').extract()
        
        for rank, state in zip(ranks, states):
            yield {'rank' : rank,
                    'state' : state}



