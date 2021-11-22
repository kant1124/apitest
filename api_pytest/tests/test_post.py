# -*- coding:utf-8 -*-
import json,requests,os,sys,allure,pytest
from utils import getdata

cases, parameters = getdata.getstore('D:/PycharmProjects/pythonProject/api_pytest/data/store.yaml')
list0=list(parameters)

class Testpost(object):
    @allure.step('测试')
    @pytest.mark.parametrize("case,http,expected", list0, ids=cases)
    def test_post(self,env,case, http, expected):
        r = requests.post(url=env['url']['cs']+http['path'],data=json.dumps(http['data']))
        response = r.json()
        print(response)
        assert response["RSP"]["IN_GROUP"] == '1'

