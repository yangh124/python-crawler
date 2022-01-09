# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

# 加载settings文件
from scrapy.utils.project import get_project_settings


class ScrapyReadbook041Pipeline:
    def open_spider(self, spider):
        self.book_list = []

    # item 就是book
    def process_item(self, item, spider):
        self.book_list.append(item)
        return item

    def close_spider(self, spider):
        sql = 'INSERT INTO book(name,src) VALUES'
        for book in self.book_list:
            sql += '("{}","{}"),'.format(book['name'], book['src'])
        sql = sql.rstrip(',')
        sql += ';'
        settings = get_project_settings()
        connect = pymysql.connect(host=settings['DB_HOST'], user=settings['DB_USER'], port=settings['DB_PORT'], password=settings['DB_PASSWORD'],
                                  db=settings['DB_NAME'], charset=settings['DB_CHARSET'])
        cursor = connect.cursor()
        cursor.execute(sql)
        connect.commit()
        connect.close()
