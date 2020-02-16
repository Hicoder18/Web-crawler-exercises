import os
import requests
from random_headers import get_headers


def saveFiles(url, headers=None):
    root = "D://work_study//code//Crawler_exercise//files//"
    path = root + url.split('/')[-1]  # 取得文件名称
    try:
        if not os.path.exists(root):  # 判断文件保存路径是否存在
            os.mkdir(root)  # 不存在则新建
        if not os.path.exists(path):  # 文件不存在则保存
            r = requests.get(url, headers=headers)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功！")
        else:
            print("文件已存在！")
    except:
        print("出现异常，保存失败！")

if __name__ == "__main__":
    headers = get_headers()
    url = input("请输入需要保存的文件URL：")
    saveFiles(url,headers)


# http://books.linjianming.com/test/20191230042141203.jpg
# http://books.linjianming.com/test/人生如戏  停更5个月后的再次更新.pdf
# http://books.linjianming.com/test/demo.html
