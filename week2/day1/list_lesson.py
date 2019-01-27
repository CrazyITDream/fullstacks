#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: list_lesson.py
@time: 2019/1/13 23:03
"""
name =['小火','达达Q','卓权','仁鸿','华煜','锦泳']

#查
# print("My Name is:",name[1:])         #取到最后
# print("My Name is:",name[1:-1])       #取到倒数第二个
# print("My Name is:",name[1:-1:1])   #从左到右一个一个去取
# print("My Name is:",name[1::2])      #从左到右隔一个取一个的去取值
# print("My Name is:",name[3::-1])       #从后往前取，隔一个取一个

#增
# name.append('小红')       #将append的值插入到队列尾
# print(name)
#
# name.insert(3,'小张')     #根据insert的索引值，插入到合适的位置
# print(name)

# #修改
# name[1]='小李'
# print(name)
#
# name[1:3]=['a','b']
# print(name)

#删除 remove pop del
# name.remove(name[1])
# print(name)
#
# name1=name.pop(1)
# print(name1)
# print(name)
#
# del name[0]
# print(name)


# #count 计算某个元素出现的次数
# t=['to','mo','to','mo','to'].count('to')
# print(t)

# extend    合并某两个列表
# a=['a','b','c']
# b=['1','2','3']
# a.extend(b)
# print(a)
# print(b)


#index  index('想要拿出来的元素')返回元素的下标
# name=['小火','仁鸿','达达Q','华煜','卓权','锦泳','仁鸿','仁鸿']

# first_lg_index=name.index("仁鸿")
# print("first_lg_index",first_lg_index)
# little_list = name[first_lg_index+1:]           #切片

# second_lg_index = little_list.index("仁鸿")
# print("second_lg_index",second_lg_index)
# second_lg_index_in_big_list = first_lg_index+second_lg_index
# print("second_index_in_big_list",second_lg_index_in_big_list)
# print("second_index_in_big_list",name[second_lg_index_in_big_list])

#reverse    #将列表进行倒置
# a=['A','C','b','a','i','L','H','l','O']
# a.reverse()
# print(a)

# #sort   对数据经行从小到大排序
# #a.sort(reverse=True)表示从小到大排序
# a=[1,5,9,0,7,2,6,4]
# a.sort(reverse=True)
# print(a)