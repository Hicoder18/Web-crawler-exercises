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
        'cookie': 'miid=1586383670828841924; t=a44dffcfc38229d053d4ec7dfca31b45; cna=tdJvFsfaziICAd9oCsZYiR3Q; lgc=%5Cu6797%5Cu9038nzs; tracknick=%5Cu6797%5Cu9038nzs; tg=0; thw=cn; _m_h5_tk=efe5ae6a1e2cf18ef669d448c7ea36e5_1580299451372; _m_h5_tk_enc=14bae382de2616ce6296c17c88010f17; _samesite_flag_=true; cookie2=1abe6c73e617dd3281b63d2dfbc13499; _tb_token_=e89e47a37aeb9; unb=2264733107; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dBxdsRiCYeWMH10dE%3D&nk2=oiRajx6ejw%3D%3D&id2=UUpnjMcj5H9X2w%3D%3D; csg=d313bbff; cookie17=UUpnjMcj5H9X2w%3D%3D; dnk=%5Cu6797%5Cu9038nzs; skt=2558f1ff0e4c05af; existShop=MTU4MDgwMTcwNQ%3D%3D; uc4=nk4=0%40oCaCTnrGw0W3YqQBd9aejB%2BR&id4=0%40U2gtHRYDQRsvyQv6D9iExErt%2FSvB; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=s72; _nk_=%5Cu6797%5Cu9038nzs; cookie1=URwTpkY8qICWYZoQt%2BfcG1hamM35IZ2d5CijXwEfiO0%3D; enc=%2FGAXD6yQxaHe1brOWEAiFMS95G8amj3xlTyp8fuWzN6w469TnmIOIEaldbvCoZ0HJR8nzbPCVsm%2BGMSrrniD4A%3D%3D; JSESSIONID=0DD25BB0DEF7C52E759821C70E97E4AE; l=cBEYOExlq8Jp6qvsBOCanurza77OSIRYSuPzaNbMi_5I06Ysd6_OoVio4Fv6VjWd9k8B4Tn8Nrv9-etuZpVGacK-g3fP.; isg=BB8fIIBFve9jo7oiRS-6f9HNrnOphHMmZGhFerFsu04VQD_CuVQDdp2SBtA-XUue; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=Vq8l%2BKCLivbS%2FaO0ok9fyA%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTUOqiueZUnyg%3D%3D&tag=8&lng=zh_CN; mt=ci=4_1; v=0'
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
