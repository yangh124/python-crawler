import urllib.request
import urllib.error

# 获取百度首页
url = 'http://www.baidu.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

# 获取Handler
handler = urllib.request.HTTPHandler()

# 创建opener
opener = urllib.request.build_opener(handler)

# 调用open
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
