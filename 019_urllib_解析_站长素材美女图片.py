import urllib.request
import urllib.error

import content as content
from lxml import etree


def get_content(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian_' + str(page) + '.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
    }

    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def download_images(content):
    tree = etree.HTML(content)

    alt_list = tree.xpath('//div[@id="container"]//a/img/@alt')

    # *src2
    src_list = tree.xpath('//div[@id="container"]//a/img/@src2')

    for i in range(0, len(alt_list)):
        alt = alt_list[i]
        src = src_list[i]
        url = 'https:' + src
        url = str.replace(url, '_s.jpg', '.jpg')  # _s缩略图
        urllib.request.urlretrieve(url=url, filename='/Users/yh/Downloads/jpg/' + alt + '.jpg')


if __name__ == '__main__':
    pageSize = int(input('请输入下载页数:'))

    for page in range(1, pageSize + 1):
        content = get_content(page)
        download_images(content)
