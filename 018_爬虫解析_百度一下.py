import urllib.request
import urllib.error
from lxml import etree

url = 'https://www.baidu.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.HTTPSHandler()

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

# 解析服务器响应html
tree = etree.HTML(content)

res = tree.xpath('//input[@id="su"]/@value')[0]

print(res)
