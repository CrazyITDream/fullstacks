#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: function_parameter.py
@time: 2019/1/22 21:41
"""

#函数必须参数(输入的顺序必须和函数调用相同)
# def print_info(name,age):
#     print('Name：%s'%name)
#     print('Age：%d'%age)
#
# print_info('小火',20)

#函数关键字参数(按照关键字查询)
# def print_info(name,age):
#     print('Name：%s'%name)
#     print('Age：%d'%age)
#
# print_info(name='小火',age=20)

#函数的默认参数(函数某个参数已经赋值了，默认参数放后面)
# def print_info(name='',age='',sex='mile'):
#     print('Name：%s'%name)
#     print('Age：%s'%age)
#     print('Sex：%s'%sex)
#
# print_info(name='小火',age=18,sex='Women')

# 不定长参数
# def add(a,b):
#     print('x+y=%s:'%(a+b))
# add(1,2)

#1、不定长参数定义(*参数)
# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(1,2,4,3)

#2、不定长参数定义(**参数（带键值对）)
# def print_info(*args,**kwargs):
#     print(args)
#     for i in kwargs:
#         print('%s %s' %(i,kwargs[i]))
# print_info('alex',18,'male',hobby='boy',height=180)

#按照参数必须原则
def print_info(sex='male',*args,**kwargs):
    for i in args:
        print('%s' %i)
    for i in kwargs:
        print('%s %s' %(i,kwargs[i]))

print_info(1,2,3,34,'female',hobby='boy',name='小火',age=18)






