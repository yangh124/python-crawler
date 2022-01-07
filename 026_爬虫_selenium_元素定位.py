from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器操作对象 path为浏览器驱动   https://npm.taobao.org/mirrors/chromedriver/
path = '/Users/yh/Documents/python-app/chromedriver'
browser = webdriver.Chrome(path)

# 访问网站
url = 'https://www.baidu.com/'

browser.get(url)

# 元素定位 获取百度一下按钮
button = browser.find_element(value='su', by=By.ID)
print(button)
# button = browser.find_element_by_name('wd')

# 根据xpath获取
button = browser.find_element(value='//input[@id="su"]', by=By.XPATH)
print(button)

# 根据标签的名字获取
button = browser.find_element(value='input', by=By.TAG_NAME)
print(button)

# 根据css选择器获取
button = browser.find_element(value='#su', by=By.CSS_SELECTOR)
print(button)

# 获取a标签
button = browser.find_element(value='新闻', by=By.LINK_TEXT)
print(button)
