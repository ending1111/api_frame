# author:小莉
import json
import re

import requests
import random
import os


class TestApi:
    #全局变量  全局变量使用类名+变量名调用
    access_token=""
    csrf_token=""
    #通过session会话去关联，session默认的情况下会自动关联cookie
    #session表示生成一个session对象
    session=requests.session()

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
        #敲重点：使用session调用请求
        res=TestApi.session.request("get",urls)
        #返回的是一个网页,使用text输出
        print(res.text)
        #re表示正则表达式匹配，从res.txt中匹配到token的值,group表示取到第一个匹配的值  用类名调用表示使用的是全局变量
        TestApi.csrf_token=re.search('name="csrf_token" value="(.*?)"',res.text).group(1)
        print(TestApi.csrf_token)
    #phpwind登录接口
    def test_phpwind_login(self):
        urls="http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        datas={
            "username":"admin",
            "password":"msjy123",
            "csrf_token": TestApi.csrf_token,
            "backurl":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        headers={
            "Accept":"application/json, text/javascript, /; q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }
        res=TestApi.session.request("post",url=urls,data=datas,headers=headers)
        #访问和登录需要用到cookies关联，因此需要传cookies
        print(res.text)
