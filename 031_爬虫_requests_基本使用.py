import requests

url = 'https://www.baidu.com/'

response = requests.get(url=url)

# 一个类型 6个属性
# <class 'requests.models.Response'>
print(type(response))

# 设置编码
response.encoding = 'utf-8'
# 获取网页源码
print(response.text)

# 返回url地址
print(response.url)

# 返回二进制数据
print(response.content)

# 获取响应状态码
print(response.status_code)

# 获取响应头
print(response.headers)
