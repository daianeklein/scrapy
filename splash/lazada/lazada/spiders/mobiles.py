import scrapy
from scrapy_splash import SplashRequest

class MobilesSpider(scrapy.Spider):
    name = "mobiles"

    def start_requests(self):
        url = 'https://www.lazada.com.ph/shop-mobiles/?spm=a2o4l.searchlistcategory.cate_1.1.7047a5104EfIn0'
        yield SplashRequest(url)

    def parse(self, response):
        products_cards_selector = response.xpath('//div[@class="Ms6aG MefHh"]')

        for product in products_cards_selector:
            product_name = product.xpath('//div[@class="Ms6aG MefHh"]//div[@class="RfADt"]/a/@title').extract()

            yield {
                'product_name' : product_name
            }
            

