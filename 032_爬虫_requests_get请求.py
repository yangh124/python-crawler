import requests

'''
urllib：
    （1）一个类型以及6个方法
    （2）get请求
    （3）post请求   百度翻译
    （4）ajax get请求
    （5）ajax post请求
    （6）cookie登陆 微博
    （7）代理

requests：
    （1）一个类型以及6个方法
    （2）get请求
    （3）post请求
    （4）代理
    （5）cookie登陆 验证码
    
'''

url = 'https://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

params = {
    'wd': '北京'
}

response = requests.get(url=url, params=params, headers=headers)

text = response.text

print(text)
