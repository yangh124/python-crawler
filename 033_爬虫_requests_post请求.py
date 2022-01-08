import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

data = {
    'kw': 'eye'
}

response = requests.post(url=url, data=data, headers=headers)

text = response.text

print(json.loads(text))
