# author:小莉
import json

import requests
import random
import os


class TestApi:
    #全局变量
    access_token=""
    #获取token接口
    def test_get_token(self):
        print("获得token")
        urls="https://api.weixin.qq.com/cgi-bin/token"
        datas={
            "grant_type":"client_credential",
            "appid":"wx3c0714880efecd8c",
            "secret": "e37a910ab5306c7883b23b47bff2768e"
        }
        res=requests.get(url=urls, params=datas)
        print(res.json()) #返回body的json格式
        #获取access_token的值
        TestApi.access_token=res.json()["access_token"]
        # 查标签接口
    def test_select_flag(self):
        urls="https://api.weixin.qq.com/cgi-bin/tags/get?access_token="+TestApi.access_token
        res=requests.get(url=urls)
        print(json.loads(json.dumps(res.json()).replace(r"\\","\\")))
        # 创建标签接口
    def test_create_tag(self):
        urls="https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+TestApi.access_token
        #产生随机数
        datas={"tag":{"name":"第一"+str(random.randint(10000,99999))}}

        res=requests.post(url=urls,json=datas)
        #这下面一句代码与上面一句代码是相等的
        #res = requests.post(url=urls, data=json.dumps(datas))

        #先将字典转换成字符串，再替换，再次转换成字典--unicode和中文的切换
        print(json.loads(json.dumps(res.json()).replace(r"\\","\\")))  #r代表真实的，后面两\\实际上是一个\将两个斜杠，转换成一个斜杠

    # 文件上传接口
    def test_file_upload(self):
        urls="https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token="+TestApi.access_token
        datas={
            #文件上传必须要用open
            "media": open(r"D:\\lanping.jpg",'rb')
        }
        res=requests.post(url=urls,files=datas)
        print(res.json())
    #访问phpwind论坛接口
    def test_phpwind(self):
        urls="http://47.107.116.139/phpwind/"
        res=requests.get(url=urls)
        #返回的是一个网页
        print(res.text)
