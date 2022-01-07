from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

'''
无头浏览器
无界面浏览器
'''


def get_headless_browser():
    # 构建options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # 对应的chromedriver的放置目录
    path = '/Users/yh/Documents/python-app/chromedriver'
    # 构建service
    service = Service(executable_path=path)

    return webdriver.Chrome(service=service, options=chrome_options)


if __name__ == '__main__':
    browser = get_headless_browser()
    browser.get('https://www.baidu.com/')
    browser.save_screenshot('/Users/yh/Downloads/screenshot.png')
