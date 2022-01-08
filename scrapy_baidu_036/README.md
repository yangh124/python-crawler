1. 创建项目 `scrapy startproject scrapy_baidu_036`
2. 创建爬虫文件
    1. 在scrapy_baidu_036/scrapy_baidu_036/spiders目录下
    2. scrapy genspider 爬虫文件的名称 要爬取的网页 `scrapy genspider baidu www.baidu.com`
3. 运行爬虫代码
    1. setting.py `ROBOTSTXT_OBEY = False`
    2. `scrapy crawl baidu`  