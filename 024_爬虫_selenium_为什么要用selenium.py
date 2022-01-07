import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

# 获取的页面缺少秒杀模块

