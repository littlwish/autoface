# _*_ coding: utf-8 _*_
# @Time : 2020/11/29 20:02 
# @Author : 廖郡 
# @Version：V 0.1
# @File : logger.py
# @desc :
import logging

log = logging.getLogger("logger")
log.setLevel(logging.DEBUG)
format = logging.Formatter(fmt='%(asctime)s')

sh = logging.StreamHandler()
sh.setFormatter(format)

log.addHandler(sh)
