import json

import scrapy

from scrapy_dangdang_039.items import ScrapyDangdang039Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=java&act=input&page_index=1']

    base_url = 'https://search.dangdang.com/?key=java&act=input&page_index='

    page = 1

    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构

        # //ul[@id='component_59']/li//img/@src
        # //ul[@id='component_59']/li//img/@alt
        # //ul[@id='component_59']/li//p[@class='price']/span[1]/text()

        li_list = response.xpath('//ul[@id="component_59"]/li')
        # 所有的selector对象都可以再次调用xpath方法
        for li in li_list:
            # data-original 才是图片地址 懒加载
            src = li.xpath('.//img/@data-original').extract_first()
            if src is None:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            book = ScrapyDangdang039Item(src='http:' + src, name=name, price=price)
            # 让pipelines去下载
            yield book

        # 爬取多页数据
        if self.page < 10:
            self.page += 1
            url = self.base_url + str(self.page)

            yield scrapy.Request(url=url, callback=self.parse)
