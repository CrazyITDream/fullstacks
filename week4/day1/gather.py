#!/usr/bin/python
#coding:utf-8

#集合
"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: gather.py
@time: 2019/1/20 15:14
"""

# #创建集合
# s = set(['a','b','c','a','d','d'])
# s1 = list(s)
# print(s1)
#
# #判断是不是在集合里面
# print('a' in s)
#
# #对集合进行更新
#
# #1、将元素增加到集合中(只能添加一个元素)
# s.add('u')
# print(s)
#
# #2、添加内容(可以添加序列)
# s.update([12,'dwadwadw'])
# print(s)
#
# #3、删除元素
# #1、删除指定元素
# s.remove('a')
# print(s)
#
# #2、随机删除元素
# s.pop()
# print(s)
#
# #3、清空集合，删除集合里面的元素
# s.clear()
# print(s)
#
# #4、删除集合，是删除整个集合
# del s
#

# print(set('alex') == set('alexexexal'))
#
# print(set('alex')<set('alexexal'))
#
# print(set('alex')>set('alexes'))

# print(set('alex')and set('alexw'))  #取全部的元素，公共的不要
#
# print(set('alex') or set('alexw'))  #取两个共有的元素

a=({1,2,3,4,5,6})
b=({4,5,6,7,8})
# print(a.intersection(b))        #交集(&)
#
# print(a.union(b))               #并集(|)

#差集(-)
# print(a.difference(b))          #表示的是b的差集，就是b缺少的元素
#
# print(b.difference(a))          #表示的是a的差集，就是a缺少的元素
#
# print(a.symmetric_difference(b))    #对称差集(^)，反向交集，就是去掉两个集合共有的元素，取两个都没有的元素

# 超集，父集
# print(a.issuperset(b))
#
# 子集
# print(a.issubset(b))








