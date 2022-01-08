import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]//a/text()')
        price_list = response.xpath('//span[@class="lever-price red"]/span/text()')
        for i in range(0, len(name_list)):
            print(name_list[i].extract() + " : " + price_list[i].extract())
