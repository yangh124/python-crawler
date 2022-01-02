import urllib.request
import urllib.error

url = 'https://blog.csdn.net/qq_42790527/article/details/121237196'
headers = {
    'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print("HTTP error")
except urllib.error.URLError:
    print("URL error")
