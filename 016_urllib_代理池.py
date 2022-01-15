import random
import urllib.request
import urllib.error

# 百度ip
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

# 快代理
# proxies_pool = [
#     {'http': '222.78.6.190:8083'},
#     {'http': '222.78.6.191:8083'},
#     {'http': '222.78.6.192:8083'},
# ]

# proxy = random.choice(proxies_pool)
proxy_url = urllib.request.urlopen('http://localhost:5555/random').read().decode('utf-8').strip()

proxy = {'http': 'http://' + proxy_url}

# 获取ProxyHandler
handler = urllib.request.ProxyHandler(proxies=proxy)

# 创建opener
opener = urllib.request.build_opener(handler)

# 调用open
response = opener.open(request)

content = response.read().decode('utf-8')

with open('代理.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
