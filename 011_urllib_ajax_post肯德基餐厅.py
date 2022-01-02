import urllib.request
import urllib.parse
import json

# 肯德基餐厅
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers = {
    'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
}
params = {
    'cname': '杭州',
    'pid': '',
    'pageIndex': 1,
    'pageSize': 10
}

data = urllib.parse.urlencode(params).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(json.loads(content))
