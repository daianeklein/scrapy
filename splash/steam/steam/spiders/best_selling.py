import scrapy
from ..items import SteamItem
from w3lib.html import remove_tags

class BestSellingSpider(scrapy.Spider):
    name = "best_selling"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/search/?filter=topsellers"]

    def get_platforms(self, list_classes):
        platforms = []
        for item in list_classes:
            platform = item.split(' ')[-1]
            
            if platform == 'win':
                platforms.append('Windows')
            if platform == 'mac':
                platforms.append('MacOs')
            if platform == 'linux':
                platforms.append('Linux')
            if platform == 'vr_supported':
                platforms.append('VR Supported') 
        
        return platforms
    
    def remove_html(self,review_summary):
        cleaned_review_summary = ''
        try:
            cleaned_review_summary = remove_tags(review_summary)
        except TypeError:
            cleaned_review_summary = 'No Reviews'

        return cleaned_review_summary
    
    def clean_discount_rate(self, discount_rate):
        if discount_rate:
            return discount_rate.lstrip('-')
        return discount_rate
    
    def get_original_price(self, selector_obj):
        original_price = ''
        div_with_dicount = selector_obj.xpath('.//div[contains(@class, "search_price discounted")]')
        if div_with_dicount == None:
            original_price = selector_obj.xpath('normalize-space(.//div[contains(@class, "search_price")]/text())').get()
        else:
            if len(div_with_dicount) > 0:
                original_price = div_with_dicount.xpath('.//span/strike/text()').get()
            else:
                original_price = selector_obj.xpath('normalize-space(.//div[contains(@class, "search_price")]/text())').get()
            
        return original_price
    
    def clean_discounted_price(self, discounted_price):
        if discounted_price:
            return discounted_price.strip()
        
        return discounted_price

    def parse(self, response):
        steam_item = SteamItem()
        games = response.xpath('//div[@id="search_result_container"]/div/a')

        for game in games:
            steam_item['game_url'] = game.xpath('.//@href').get()
            steam_item['img_url'] = game.xpath('.//div[@class="col search_capsule"]/img/@src').get()
            steam_item['game_name'] = game.xpath('//span[@class="title"]/text()').get()
            steam_item['release_date'] = game.xpath('//div[@class="col search_released responsive_secondrow"]/text()').get()
            steam_item['platforms'] = self.get_platforms(game.xpath('//span[contains(@class, "platform_img") or @class="vr_supported"]/@class').getall())
            steam_item['reviews_summary'] = self.remove_html(game.xpath('//span[contains(@class, "search_review_summary")]/@data-tooltip-html').get())
            steam_item['discount_rate'] = self.clean_discount_rate(game.xpath('//div[contains(@class, "search_discount")]/span/text()').get())
            steam_item['original_price'] = self.get_original_price(game.xpath('.//div[contains(@class, "search_price_discount_combined")]'))
            steam_item['discount_price'] = self.clean_discounted_price(game.xpath('(.//div[contains(@class, "search_discount")]//text())[2]').get())

            yield steam_item

        next_page = response.xpath('//a[@class="pagebtn" and text()=">"]/@href').get()
        if next_page:
            yield scrapy.Request(
                url = next_page,
                callback=self.parse)



