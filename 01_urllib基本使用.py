import urllib.request

# 定义请求的url
url = 'http://www.baidu.com/'

# 使用urllib打开url
resp = urllib.request.urlopen(url)

# 获取响应结果
content = resp.read().decode('UTF-8')

# 打印获取到的数据 -> 网页源码
print(content)
