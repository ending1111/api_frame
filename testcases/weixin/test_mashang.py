# author:小莉
import requests


class TestBaili:
    def test_05_get_token(self,kwkwkwkw,base_url):
        print("获得鉴权码呀1"+kwkwkwkw)
        print(base_url+'/phpwind/')
        requests.get(url=base_url+'/phpwind/')