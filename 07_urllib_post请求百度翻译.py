import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36'}

data = {
    'kw': 'spider'
}

# post请求必须要encode参数，必须调用encode方法
data = urllib.parse.urlencode(data).encode('UTF-8')

request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

res = json.loads(content)

print(res)
