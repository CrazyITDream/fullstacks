#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: 递归函数.py
@time: 2019/1/24 21:34
"""

#普通函数计算阶乘
# def f(n):
#     ret =1
#     for i in range(2,n+1):
#         ret = ret *i
#         return ret
# print(f(5))


#递归函数计算阶乘
# def fact(n):
#      if n==1:
#          return 1
#      else:
#          return n*fact(n-1)
# print(fact(5))

#斐波那契数列非递归
# def fibo(n):
#     before=0
#     after=1
#     for i in  range(n-1):
#         ret=before+after
#         before=after
#         after=ret
#     return ret
#
# print(fibo(8))

#斐波那契数列递归 0 1 1 2 3 5 8 13 21 34 55 89 .........
# def fibo(n):
#     if n<=1:        #n==0 or n==1
#         return n
#     else:
#         return (fibo(n-1)+fibo(n-2))
#
# print(fibo(8))
