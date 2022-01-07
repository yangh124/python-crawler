from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器操作对象 path为浏览器驱动   https://npm.taobao.org/mirrors/chromedriver/
path = '/Users/yh/Documents/python-app/chromedriver'
browser = webdriver.Chrome(path)

# 访问网站
url = 'https://www.baidu.com/'

browser.get(url)


# 根据css选择器获取
button = browser.find_element(value='#su', by=By.CSS_SELECTOR)
print(button.get_attribute('class'))
print(button.text)
print(button.tag_name)

browser.close()
