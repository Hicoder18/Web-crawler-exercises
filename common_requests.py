import requests
from random_headers import get_headers


# 爬取网页内容
def getHTML(url, headers=None):
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()  # 如果状态码不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding  # 替换编码方式，防止显示中文乱码
        return r
    except:
        print("出现异常，爬取失败！")


if __name__ == "__main__":
    headers = get_headers()  # 随机headers，反反爬虫措施
    url = input("请输入需要爬取的网页URL：")
    print("-----------------------------------------------")
    print("状态码：", getHTML(url, headers).status_code)  # 200则表示爬取成功
    print(getHTML(url, headers).text[1000:1800])
