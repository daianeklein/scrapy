from scrapy.selector import Selector
from scrapy_splash import SplashRequest
import scrapy
import json

class ListingsSpider(scrapy.Spider):
    name = 'centris_listings'
    allowed_domains = ['www.centris.ca']

    position = {
        'startPosition' : 0
    }

    script = '''
        function main(splash, args)
            splash:on_request(function(request)
                if request.url:find('css') then
                    request.abort()
                end
            end)
            splash.images_enabled = false
            splash.js_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()
        end
    '''

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.centris.ca/UserContext/Lock',
            method='POST',
            headers={
                'x-requested-with': 'XMLHttpRequest',
                'content-type': 'application/json'
            },
            body=json.dumps({'uc': 0}),
            callback=self.generate_uck
        )

    def generate_uck(self, response):
        uck = response.body
        query = {"query": {"UseGeographyShapes": 0, "Filters": [{"MatchType": "CityDistrictAll", "Text": "Montréal (All boroughs)", "Id": 5}], "FieldsValues": [{"fieldId": "CityDistrictAll", "value": 5, "fieldConditionId": "", "valueConditionId": ""}, {"fieldId": "Category", "value": "Residential", "fieldConditionId": "", "valueConditionId": ""}, {"fieldId": "SellingType", "value": "Rent", "fieldConditionId": "", "valueConditionId": ""}, {
            "fieldId": "LandArea", "value": "SquareFeet", "fieldConditionId": "IsLandArea", "valueConditionId": ""}, {"fieldId": "RentPrice", "value": 0, "fieldConditionId": "ForRent", "valueConditionId": ""}, {"fieldId": "RentPrice", "value": 3000, "fieldConditionId": "ForRent", "valueConditionId": ""}]}, "isHomePage": True}
        yield scrapy.Request(
            url="https://www.centris.ca/property/UpdateQuery",
            method="POST",
            body=json.dumps(query),
            headers={
                'Content-Type': 'application/json',
                'x-requested-with': 'XMLHttpRequest',
                'x-centris-uc': 0,
                'x-centris-uck': uck
            },
            callback=self.update_query
        )
        #print(uck)

    def update_query(self, response):
        yield scrapy.Request(
            url = 'https://www.centris.ca/Property/GetInscriptions',
            method = 'POST',
            body = json.dumps(self.position),
            headers = {'Content-Type' : 'application/json'},
            callback = self.parse 

        )
        print(response.body)

    def parse(self, response):
        resp_dict = json.loads(response.body)
        html = resp_dict.get('d').get('Result').get('html')
        sel = Selector(text=html)

        listings = sel.xpath('//*[contains(@class, "property-thumbnail-item thumbnailItem")]').extract()

        for listing_html in listings:
            listing = Selector(text=listing_html)
            category = listing.xpath('//span[@class="category"]/div/text()').get().replace(' ', '').replace('\r', '').replace('\n', '')
            price = listing.xpath('//div[@class="price"]/span/text()').get().replace('\xa0', '')
            url = listing.xpath('//*[@class="property-thumbnail-summary-link"]/@href').get()
            abs_url = f'https://www.centris.ca{url}'

            # yield {'category': category,
            #     'price': price,
            #     'url': url}
            yield SplashRequest(
                url = abs_url,
                endpoint = "execute",
                callback = self.parse_summary,
                args = {
                    'lua_source' : self.script
                },

                meta = {
                    'cat' : category,
                    'price' : price,
                    'url' : abs_url
                }
            )
        
        count = resp_dict.get('d').get('Result').get('count')
        increment_number = resp_dict.get('d').get('Result').get('inscNumberPerPage')

        if self.position['startPosition'] <= count:
            self.position['startPosition'] += increment_number
            yield scrapy.Request(
                url = "https://www.centris.ca/Property/GetInscriptions",
                method = 'POST',
                body = json.dumps(self.position),
                headers = {'Content-Type' : 'application/json'},
                callback = self.parse
            )

    def parse_summary(self, response):
        address = response.xpath('//h2[@itemprop="address"]/text()').get()
        description = response.xpath('normalize-space(//div[@itemprop="description"]/text())').get()
        category = response.request.meta['cat']
        price = response.request.meta['price']
        url = response.request.meta['url']

        yield {
            'address' : address,
            'description' : description,
            'category' : category,
            'price' : price
        }
        # with open('index.html', 'w') as f:
        #     f.write(html)


