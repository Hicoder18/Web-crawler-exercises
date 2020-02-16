import requests
import re
 
def getHTMLText(url,headers):
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("getHTML error!")
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("parsePage error!")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
         
def main():
    goods = input("请输入需要爬取的商品名称：")
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    # 构造Request Headers
    # 先用自己电脑的浏览器访问 https://s.taobao.com/search?q=Python  需登录淘宝
    # 然后获取自己访问的 user-agent:... 以及 cookie:...
    # 如果不如此，进入不了 https://s.taobao.com/search?q=Python 爬取不到数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'cookie': '你的cookie'
    }
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url,headers)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()
