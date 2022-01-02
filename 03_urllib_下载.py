import urllib.request

# 定义请求的url
url = 'http://www.baidu.com/'

# 下载文件
resp = urllib.request.urlretrieve(url, 'baidu.html')
