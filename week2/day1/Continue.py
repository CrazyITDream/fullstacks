#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: Continue.py
@time: 2019/1/13 22:45
"""
exit_flag = False
for i in range(10):
     if i<5:
         continue
     print(i)
     for j in range(10):
         print("layer 2",j)
         if j==6:
             exit_flag = True
             break
     if exit_flag:
          break



