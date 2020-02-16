import requests
from bs4 import BeautifulSoup
import bs4
from random_headers import get_headers

def getHTMLText(url):
    headers = get_headers()
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('爬取失败！')

def saveBookInfo(blist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for li in soup.find('ul',attrs={'class':'list-col list-col5 list-express slide-item'}).find_all('li'):
        cover = li.find('div',attrs={'class':'cover'}).a.img.get('src')
        title = li.find('div',attrs={'class':'title'}).text
        author = li.find('div',attrs={'class':'author'}).text
        blist.append([title, author, cover])

def printBookInfo(blist):
    print("--------------------------------------------------------------------------")
    for i in range(len(blist)):
        book = blist[i]
        print("第{}本书：\n".format(i+1))
        print("书名：{}\n作者：{}\n封面：{}\n".format(book[0].strip(),book[1].strip(),book[2].strip()))
        print("--------------------------------------------------------------------------")

def main():
    binfo = []
    url = 'https://book.douban.com/'
    html = getHTMLText(url)
    saveBookInfo(binfo, html)
    printBookInfo(binfo)

main()  # 程序入口
