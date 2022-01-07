from selenium import webdriver

# 创建浏览器操作对象 path为浏览器驱动   https://npm.taobao.org/mirrors/chromedriver/
path = '/Users/yh/Documents/python-app/chromedriver'
browser = webdriver.Chrome(path)

# 访问网站
url = 'https://www.jd.com'

browser.get(url)

# 获取网页源码  可以获取秒杀模块
page_source = browser.page_source
print(page_source)
