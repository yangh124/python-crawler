import urllib.request

# 定义请求的url
url = 'https://www.baidu.com/'

# response = urllib.request.urlopen(url)

# content = response.read().decode('utf-8')

# 没有user-agent 获取失败
# print(content)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36'}
# 定制request
request = urllib.request.Request(url=url, headers=headers)

content = urllib.request.urlopen(request).read().decode('utf-8')

print(content)
