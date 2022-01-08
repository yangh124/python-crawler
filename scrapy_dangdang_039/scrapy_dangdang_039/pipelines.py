# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request


# 需要在settings中开启管道
class ScrapyDangdang039Pipeline:

    def open_spider(self, spider):
        print('===============start===============')
        self.book_list = []

    # item 就是book
    def process_item(self, item, spider):
        # a -> append
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))
        # 上面这种方式不推荐 self.book_list.append(spider)
        self.book_list.append(str(item).replace('\'', '"').replace(' ', ''))
        return item

    def close_spider(self, spider):
        fp = open('book.json', 'w', encoding='utf-8')

        fp.write('[')
        for i in range(0, len(self.book_list)):
            fp.write(self.book_list[i])
            if i != len(self.book_list) - 1:
                fp.write(',')

        fp.write(']')

        fp.close()


# 多条管道同时开启
# 'scrapy_dangdang_039.pipelines.DangdangDownloadPipeline': 301
class DangdangDownloadPipeline:

    # item 就是book
    def process_item(self, item, spider):
        url = item.get('src')
        filename = '/Users/yh/Downloads/jpg/' + item.get('name') + '.jpg'

        urllib.request.urlretrieve(url=url, filename=filename)
        return item
