import scrapy

from scrapy_movie_040.items import ScrapyMovie040Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/jddy/index.html']

    def parse(self, response):
        a_list = response.xpath('//table[@class="tbspan"]//td[2]//a[@class="ulink"]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://www.dytt8.net' + href

            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']

        movie = ScrapyMovie040Item(src=src, name=name)

        yield movie
