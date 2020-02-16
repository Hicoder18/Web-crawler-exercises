import requests
from random_headers import get_headers

def searchSo(keywords=None, headers=None):
    try:
        url = "https://www.so.com/s"
        r = requests.get(url, params=keywords, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        print("出现异常，爬取失败！")


if __name__ == "__main__":
    headers = get_headers()    
    print(headers)
    keyword = input("请输入需要搜索的关键词：")
    keywords = {"q":keyword}
    print(searchSo(keywords,headers).text[:2000])
    print("-----------------------------------------------")
    print(searchSo(keywords,headers).headers)

