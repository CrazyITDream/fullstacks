#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: time_date.py
@time: 2019/1/22 21:08
"""

#日志记录
import time

def logger(n):
     time_fromat='%Y-%m-%d  %X'
     time_curront = time.strftime(time_fromat)

     with open('日志记录','a') as f:
         f.write(' %s end action %s \n' %(time_curront,n))

def action(n):
    print('starting  action1.....')
    logger(n)


action(11)
action(12)
action(13)
