import scrapy


class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['https://fanyi.baidu.com/sug']

    # post 不需要 start_urls parse()
    # start_urls = ['//https://fanyi.baidu.com/sug/']

    # def parse(self, response):
    #    pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        res = response.json()
        print(res)
