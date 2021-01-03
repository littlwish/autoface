# _*_ coding: utf-8 _*_
# @Time : 2020/12/31 10:44 
# @Author : 廖郡 
# @Version：V 0.1
# @File : runner.py
# @desc :

import pytest
import os

pytest.main(["test_case/test_case.py", '--alluredir', './temp', '-s'])
#os.system('allure generate ./temp -o ./allure-report --clean')
