from bs4 import BeautifulSoup
from common_requests import getHTML
from random_headers import get_headers


def parserHTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


if __name__ == '__main__':
    headers = get_headers()  # 随机headers，反反爬虫措施
    url = input('请输入需要爬取的HTML页面：')
    html = getHTML(url,headers).text[:1000]
    sp = parserHTML(html)
    print(sp.prettify())
