from selenium import webdriver
import time

# 创建浏览器操作对象 path为phantomjs
path = '/Users/yh/Documents/python-app/phantomjs'

browser = webdriver.PhantomJS(path)

# 访问网站
url = 'https://www.baidu.com/'

# 打开浏览器
browser.get(url)

# 截图
browser.save_screenshot('百度.png')


'''
新版的selenium已经不支持PhantomJS了
'''
