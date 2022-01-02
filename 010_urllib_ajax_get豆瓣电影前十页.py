import urllib.request
import urllib.parse


# 生成request
def create_request(page, rows):
    # 豆瓣动作电影排行
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
    }
    params = {
        'type': 5,
        'interval_id': '100:90',
        'action': '',
        'start': (page - 1) * 20,
        'limit': rows
    }

    data = urllib.parse.urlencode(params).encode('utf-8')

    request = urllib.request.Request(url=url, data=data, headers=headers)

    return request


# 下载内容
def get_content(request, page):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    with open('豆瓣动作片_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page, 20)
        get_content(request, page)
