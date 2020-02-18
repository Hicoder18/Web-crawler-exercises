import json
import time
import requests
from bs4 import BeautifulSoup
from random_headers import get_headers

def downloadHTML(url):
    headers = get_headers()
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encodeing = 'utf-8'
        return r.text
    except:
        print("爬取失败！")

def extractBookInfo(blst, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tbl in soup.find('div',attrs={'class':'indent'}).find_all('table'):
        bimg = tbl.find('a',attrs={'class':'nbg'}).img.get('src')
        bname = tbl.find('div',attrs={'class':'pl2'}).a.text.replace(' ','').replace('\n','')
        blink = tbl.find('div',attrs={'class':'pl2'}).a.get('href')
        bdesc = tbl.find('p',attrs={'class':'pl'}).text
        brate = tbl.find('span',attrs={'class':'rating_nums'}).text
        # bquote = tbl.find('span',attrs={'class':'inq'}).text
        blst.append([bimg, bname, blink, bdesc, brate])
    print(len(blst))

def saveToJSON(blst):
    filename = 'D:/work_study/code/Crawler_exercise/Douban_Reading_List/files/topbook250.json'
    bdic = {"code": 200, "booklist": blst}
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(bdic, indent=4, sort_keys=True, ensure_ascii=False))
        print("数据保存成功！")

def main():
    binfo = []
    start_url = 'https://book.douban.com/top250'
    for i in range(10):
        try:
            url = start_url + '?start=' + str(i*25)
            html = downloadHTML(url)
            time.sleep(3)
            extractBookInfo(binfo, html)
        except:
            continue
    saveToJSON(binfo)

main()
