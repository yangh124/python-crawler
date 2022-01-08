import requests

url = 'https://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

# 可能失效
proxies = {
    'http': '27.22.85.58:8100'
}

params = {
    'wd': 'ip'
}

response = requests.get(url=url, params=params, headers=headers, proxies=proxies)

text = response.text

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(text)
