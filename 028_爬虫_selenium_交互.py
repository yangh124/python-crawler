from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建浏览器操作对象 path为浏览器驱动   https://npm.taobao.org/mirrors/chromedriver/
path = '/Users/yh/Documents/python-app/chromedriver'
browser = webdriver.Chrome(path)

# 访问网站
url = 'https://www.baidu.com/'

# 打开浏览器
browser.get(url)

# 休眠5s
time.sleep(2)

# 获取input
input = browser.find_element(value='#kw', by=By.CSS_SELECTOR)
input.send_keys('周杰伦')

time.sleep(2)

# 获取百度按钮
search_button = browser.find_element(value='#su', by=By.CSS_SELECTOR)
search_button.click()

time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页按钮  //a[@class='n']
next_button = browser.find_element(value='//a[@class="n"]', by=By.XPATH)
next_button.click()

time.sleep(2)

# 返回（向前）
browser.back()

time.sleep(2)

# 向前
browser.forward()

time.sleep(3)

# 关闭
browser.close()
