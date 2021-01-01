# _*_ coding: utf-8 _*_
# @Time : 2020/12/30 11:13 
# @Author : 廖郡 
# @Version：V 0.1
# @File : test_httptestcase.py
# @desc :
import requests
import pytest
import json


class TestHttp:

    def test_login(self):
        token = self.getToken()
        print(token)
        print(self.getGoodsList(token))

    def getGoodsList(self, token=''):
        """
        获取商品列表
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        print(headers)
        r = requests.get('http://admin-api.macrozheng.com/brand/list?pageNum=1&pageSize=100', headers=headers)
        return r.text

    def getToken(self):
        # data = "{\r\n    \"username\": \"admin\",\r\n    \"password\": \"macro123\"\r\n}"
        data = {
            "username": "admin",
            "password": "macro123"
        }
        headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post('http://admin-api.macrozheng.com/admin/login', data=json.dumps(data), headers=headers)
        print(r.url)
        print(r.text)
        print(type(r.text))
        user_dict = json.loads(r.text)
        print(user_dict.get('code'))
        return user_dict.get('data').get('token')


if __name__ == '__main__':
    pytest.main(['test_httptestcase.py', '-s'])
