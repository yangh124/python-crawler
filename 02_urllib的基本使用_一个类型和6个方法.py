import urllib.request

# 定义请求的url
url = 'http://www.baidu.com/'

# 使用urllib打开url
resp = urllib.request.urlopen(url)

# 打印获取到的响应的数据类型  http.client.HTTPResponse
print(type(resp))

# 一个字节一个字节的读
print(resp.read())

# 只读取一行
print(resp.readline())

# 一行一行的读取
print(resp.readlines())

# 获取http状态码
print(resp.getcode())

# 获取url
print(resp.geturl())

# 获取响应head
print(resp.getheaders())
