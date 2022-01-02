import urllib.parse
import urllib.request

# encode编码 中文
name = urllib.parse.quote('周杰伦')

url = 'https://www.baidu.com/s?wd=' + name

print(url)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
