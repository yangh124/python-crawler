# 参数
# __VIEWSTATE: LDbk/O63NqsxzO3FJS2HRtb5P4bNTYiDJXoePadf1VqS1GXHKKa9sH2dk5ycKo6FTS+Jf3KvrUJcWF5Y+t8+Vbtt46BnsGU4FqNvkAm7TdFUYCKGjlJfFNpKubg=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx?type=s
# email: yh.124@qq.com
# pwd: 342445435
# code: 84vn
# denglu: 登录
import requests
from bs4 import BeautifulSoup
import urllib.request

'''
    （1）获取登陆页源码 获取到 __VIEWSTATE 和 __VIEWSTATEGENERATOR
    （2）下载验证码图片 手动查看
    （3）登陆请求和获取验证码请求使用同一个session
'''

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx?type=s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

# 获取网页代码
text = response.text

# 解析页面
soup = BeautifulSoup(text, 'lxml')

# 获取__VIEWSTATE
__VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')
print(__VIEWSTATE)

# 获取__VIEWSTATE
__VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
print(__VIEWSTATEGENERATOR)

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code

# 下载验证码 不能用这个 登陆请求和获取验证码请求不是同一个
# urllib.request.urlretrieve(code_url, filename='code.jpg')

# 解决办法 使用session
session = requests.session()
response_code = session.get(code_url)
# 这里是图片 使用.content
content_code = response_code.content

# wb  write binary
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

# 获取验证码图片后 下载到本地查看验证码
code_name = input("请输入验证码")

url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx%3ftype%3ds'
data_post = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx?type=s',
    'email': 'yh.124@qq.com',
    'pwd': '*****',
    'code': code_name,
    'denglu': '登录'
}

response_post = session.post(url=url_post, headers=headers, data=data_post)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
