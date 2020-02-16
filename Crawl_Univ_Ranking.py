import requests
from bs4 import BeautifulSoup
import bs4
from random_headers import get_headers

def getHTMLText(url):
    headers = get_headers()
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败！')

def saveUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:12}\t{2:^8}\t{3:<8}"
    print(tplt.format("排名","学校名称","地区","总分",chr(12288)))
    print('---------------------------------------------------------------')
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    saveUnivList(uinfo, html)
    printUnivList(uinfo, 50)  # 50 univs

main()
