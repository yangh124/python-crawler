import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://hz.58.com/sou/?key=java%E5%BC%80%E5%8F%91']
    start_urls = ['https://hz.58.com/sou/?key=java%E5%BC%80%E5%8F%91']

    def parse(self, response):
        # # 字符串
        # content = response.text
        # # 二进制
        # body = response.body
        # print('==================================')
        # print(content)

        print('==================================')
        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print(span.extract())
