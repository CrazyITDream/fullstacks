#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: 闭包.py
@time: 2019/1/26 12:10
"""

def outer():
    x=10
    def inner():
        print('%s' %x)
    return inner()

outer()
