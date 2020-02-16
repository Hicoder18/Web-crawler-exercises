import os
import requests
from bs4 import BeautifulSoup
import bs4
import xlwt  # 写
import xlrd  # 读
from xlutils.copy import copy
 
def getHTMLText(url,headers):
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("getHTML error!")
     
def parsePage(blist, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        for li in soup.find('ul',attrs={'class':'video-list clearfix'}).find_all('li'):
            url = 'https:' + li.find('a',attrs={'class':'img-anchor'}).get('href')
            title = li.find('a',attrs={'class':'img-anchor'}).get('title')
            span = li.find('div',attrs={'class':'info'}).find('div',attrs={'class':'tags'}).find_all('span')
            upname = span[3].find('a',attrs={'class':'up-name'}).get_text()
            upurl = 'https:' + span[3].find('a',attrs={'class':'up-name'}).get('href')
            blist.append([title, url.split('?')[0], upname, upurl.split('?')[0]])
    except:
        print("parsePage error!")

def saveVData(blist, keyword):
    root = 'D://work-study//code//Crawler-exercise//files//'
    path = root + 'BiliBili_Videos_info.xls'
    try:
        if not os.path.exists(root):  # 判断文件保存路径是否存在
            os.mkdir(root)
        if not os.path.exists(path):  # 文件不存在则新建并保存
            workbook = xlwt.Workbook()  # 新建一个工作簿
            sheet = workbook.add_sheet('bilibili_'+ keyword +'_video_info',cell_overwrite_ok=True)  # 在工作簿中新建一个表格
            sheet.write(0,0, '序号')
            sheet.write(0,1, '视频名')
            sheet.write(0,2, '视频链接')
            sheet.write(0,3, 'up主')
            sheet.write(0,4, 'up主空间')
            count = 0
            for item in blist:
                count = count + 1
                sheet.write(count, 0, count)  # 像表格中写入数据（对应的行和列和值）
                sheet.write(count, 1, item[0])  
                sheet.write(count, 2, item[1])
                sheet.write(count, 3, item[2])
                sheet.write(count, 4, item[3]) 
            workbook.save(path)  # 保存
            print("保存到BiliBili_Videos_info.xls成功！")
        else:
            rd = xlrd.open_workbook(path, formatting_info = True)   # 打开文件
            wt = copy(rd)   # 复制
            sheet = wt.add_sheet('bilibili_'+ keyword +'_video_info',cell_overwrite_ok=True)   # 读取第一个工作表
            sheet.write(0,0, '序号')
            sheet.write(0,1, '视频名')
            sheet.write(0,2, '视频链接')
            sheet.write(0,3, 'up主')
            sheet.write(0,4, 'up主空间')
            count = 0
            for item in blist:
                count = count + 1
                sheet.write(count, 0, count)  # 向表格中写入数据（对应的行和列和值）
                sheet.write(count, 1, item[0])  
                sheet.write(count, 2, item[1])
                sheet.write(count, 3, item[2])
                sheet.write(count, 4, item[3]) 
            wt.save(path)  # 保存
            print("BiliBili_Videos_info.xls再次保存成功！")
    except:
        print("保存文件出错！")

def printVInfoList(blist):
    print("---------------------------------------------------------------------------")
    count = 0
    for item in blist:
        count = count + 1
        print("序号：{}\n视频名：{}\n视频链接：{}\nup主：{}\nup主空间：{}".format(count, item[0], item[1], item[2], item[3]))
        print("---------------------------------------------------------------------------")
         
def searchKeyword():
    keyword = input("请输入需要爬取的视频信息关键词keyword：")
    repeat = 0
    f = 'D://work-study//code//Crawler-exercise//files//keywords.txt'
    with open(f) as lines:  # 一次性读入txt文件，并把内容放在变量lines中
        array = lines.readlines()  # 返回的是一个列表，该列表每一个元素是txt文件的每一行
        new_array = []  # 使用一个新的列表来装去除换行符\n后的数据
        for elem in array:  # 遍历array中的每个元素
            elem = elem.strip('\n')  # 去掉换行符\n
            new_array.append(elem)  # 把去掉换行符的数据放入array2中
    for i in range(len(new_array)):
        if keyword == new_array[i]:
            repeat = repeat + 1
    with open(f, 'a') as file:
        file.write(keyword + '\n')
    return keyword, repeat

def main():
    tup = searchKeyword()
    keyword = tup[0]
    repeat = tup[1]
    depth = input("请输入希望爬取页数depth（请输入整数）：")
    if isinstance(int(depth), int) and not repeat:
        start_url = 'https://search.bilibili.com/video?keyword=' + keyword
        infoList = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
        for i in range(int(depth)):
            try:
                url = start_url + '&page=' + str(i+1)
                html = getHTMLText(url,headers)
                parsePage(infoList, html)
            except:
                continue
        printVInfoList(infoList)
        saveVData(infoList,keyword)
    else:
        print("depth获取的输入非整数或者keyword已经爬取过！无法爬取！Bye~")
     
main()
