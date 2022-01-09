import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_readbook_041.items import ScrapyReadbook041Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="book-info"]//img')
        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            if src is None:
                src = img.xpath('./@src').extract_first()
            name = img.xpath('./@alt').extract_first()
            book = ScrapyReadbook041Item(name=name, src=src)
            yield book
