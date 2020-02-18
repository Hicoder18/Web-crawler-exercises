from qiniu import Auth, put_file, etag
from qiniu import BucketManager
import qiniu.config
import os
import qiniu_access


def upload():
    # 七牛的配置信息
    access_key = '7ahEZ3FtZE9AmNLHUPcG59KmJtzOfulkLI71unHH'  # 输入你自己的
    secret_key = 'zcx3MGQ22bfSWl2AYYIaxnutgy4WvNFn20ixNsPY'  # 输入你自己的

    q = Auth(access_key, secret_key)

    # 文件上传的七牛空间
    bucket_name = 'my-statics'

    # 上传后保存的文件名
    key = 'api/books/topbook250.json'

    # 判断七牛key是否已经存在
    buc = BucketManager(q)
    res, info1 = buc.stat(bucket_name, key)
    if(res != None):
        print("文件已存在")
        exit()

    # 上传文件的地址
    localfile  = 'D:/work_study/code/Crawler_exercise/Douban_Reading_List/files/topbook250.json'
    if(os.path.exists(localfile) == False):
        print("文件不存在")
        exit()

    # 获取上传的token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 36000000)

    # 上传文件
    ret, info = put_file(token, key, localfile)
    if(ret == None):
        # 上传失败
        print("上传失败")
        exit()
    print("上传成功")

if __name__ == '__main__':
    upload()
