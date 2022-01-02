import urllib.request
import json

# 豆瓣动作电影排行
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# open方法默认使用gbk编码
# fp = open('豆瓣动作片.json', 'w', encoding='utf-8')
# fp.write(content)
# fp.close()

with open('豆瓣动作片.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
