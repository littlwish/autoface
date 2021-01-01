# _*_ coding: utf-8 _*_
# @Time : 2020/12/31 10:42 
# @Author : 廖郡 
# @Version：V 0.1
# @File : test_case.py
# @desc : 测试用例
import json
import logging as log

import allure
import pytest
import requests
from mako.template import Template

from tools.get_excel import TestCaseData


class TestCase:
    # 全局环境变量
    _enriment = {}

    def replace(self, tpl):
        token = self._enriment.get('token')
        if token:
            t = Template(tpl)
            text = t.render(token=token)
            return text
        else:
            return tpl

    def setEnrimentValue(self, key, value):
        """
        设置环境变量的值
        :param key:         key
        :param value:       value
        :return:
        """
        self._enriment[key] = value

    @pytest.mark.parametrize('case', TestCaseData.getExcelCases())
    def test_excel(self, case):
        """
        执行测试用例
        :return:
        """
        print('开始用例测试', case)
        # 请求方式
        pattern = case.get('pattern')

        # 设置用例名称
        allure.dynamic.feature(case.get('case_moudle'))
        allure.dynamic.story(case.get('case_fun'))
        allure.dynamic.title(case.get('case_name'))
        allure.dynamic.description(case.get('case_desc'))
        log.warning('开始:' + case.get('case_name'))
        url = self.buildUrl(case)
        log.warning('请求地址:' + url)
        headers = self.buildHeaders(case)
        log.warning('请求头参数:' + str(headers))
        param = self.buildParams(case)
        log.warning('请求体参数:' + str(param))
        # ex_headers = case.get('headers').lstrip()
        # headers = json.loads(ex_headers)
        # params = json.loads(case.get('param'))
        if url is not None:
            if pattern == 'POST':
                result = requests.post(url, headers=headers, data=json.dumps(param))
                log.warning('请求结果:' + result.text)
                self.checkResult(case, result.text)
            elif pattern == 'GET':
                result = requests.get(url, headers=headers, data=json.dumps(param))
                log.warning('请求结果:' + result.text)
                self.checkResult(case, result.text)

    @allure.step('构建请求路径')
    def buildUrl(self, case):
        """
        构建请求url
        :param case:
        :return:
        """
        url = case.get('case_url') + case.get('case_controller')
        return url

    @allure.step('构建请求头')
    def buildHeaders(self, case):
        """
        构建请求头参数
        :return:
        """
        headers = case.get('headers')
        return json.loads(self.replace(headers)) if headers else {}

    @allure.step('构建请求参数')
    def buildParams(self, case):
        """
        构建请求参数
        :param case:
        :return:
        """
        param = case.get('param')
        return json.loads(self.replace(param)) if param else {}

    @allure.step('结果校验')
    def checkResult(self, case, response_text):
        """
        结果校验
        :param response_text:  返回结果体
        :param case:           用例参数
        :return:
        """
        result_key = case.get('result')
        expect = case.get('expect')
        result_json = json.loads(response_text)
        if case.get('case_number') == 'T001':
            token = result_json.get('data').get('tokenHead') + result_json.get('data').get('token')
            self.setEnrimentValue('token', token)
        assert expect == result_json.get(result_key)
