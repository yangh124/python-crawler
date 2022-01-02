import urllib.request
import urllib.error

# 和风天气
url = 'https://www.qweather.com/'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'cookie': '_ga=GA1.2.1053634299.1635670780; _gid=GA1.2.152018977.1641047001; i_c=jianggan-101210111; '
              'Hm_lvt_70906f408d58a995c42bc9d3b000a278=1641047107,1641047122,1641047209,1641047218; '
              'Hm_lpvt_70906f408d58a995c42bc9d3b000a278=1641050722',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="100", "Google Chrome";v="100", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('和风天气.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
