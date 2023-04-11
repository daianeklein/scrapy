import scrapy


class TableSpider(scrapy.Spider):
    name = "table"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population"]

    def parse(self, response):
        table = response.xpath('//table[contains(@class, "wikitable sortable")]')[1]

        ranks = table.xpath('//span[@data-sort-value]/text()').extract()
        states = table.xpath('//tr/th/a/text()').extract()
        population = table.xpath('//tr/td[1]/following-sibling::td[3]/text()').extract()
        
        for rank, state, population in zip(ranks, states, population):
            yield {'rank' : rank,
                    'state' : state,
                    'population' : population}



