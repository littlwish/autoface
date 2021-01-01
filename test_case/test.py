# _*_ coding: utf-8 _*_
# @Time : 2020/12/30 14:08 
# @Author : 廖郡 
# @Version：V 0.1
# @File : test.py
# @desc :

import xlrd

from mako.template import Template
from mako.runtime import Context
from io import StringIO
from mako.template import Template
t = Template('hello, ${name}!')
p = {}
p.pop('name','yeolar')
print(t.render([],p))