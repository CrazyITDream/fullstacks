#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: lesson_dict.py
@time: 2019/1/16 19:22
"""

#字典创建
# dic={'name':'xiaohuo','age':'21','hobby':{'girl_name':'pig','age':18},'is_handsome':'handsome'}
# print(dic['name'])
# print(dic)

# 字典创建
# a=dict((('name','猪婆'),))
# print(a)

#字典增加
# dicl={'name':'猪婆'}
# dicl['age'] = 21
# print(dicl)
#
# rel=dicl.setdefault('age','34')
# print(rel)
# rel1=dicl.setdefault('hobby','girl')
# print(rel1)
# print(dicl)

# #修改
# dicl ={'姓名:':'钟火雄','年龄:':'20'}
# print(dicl)
# dicl['年龄:']=19
# print(dicl)

# #增加
# dicl['爱好:']='girl'
# print(dicl)
# dicl.setdefault('homeWork','IT')
# print(dicl)

# #删除
# del dicl['homeWork']
# print(dicl)
# dicl.pop('爱好:')
# print(dicl)

#STring的内置方法
string="Hello World {name} is {age}"
print(string.count('H'))        #统计元素个数
print(string.capitalize())      #首字母大写
print(string.center(50,' '))    #居中
print(string.encode())           #字节码、编码
print(string.endswith('1'))     #判断字符串是否依据某个字符串结尾
print(string.startswith('H'))   #判断字符串是不是依据某个字符开始
# print(string.expandtabs(tablesize=20))   #设置tab的值
print(string.find('e'))     #查找元素
print(string.format(name='xiaohuo',age=21))         #格式化输出
print(string.format_map({'name':'小火','age':20}))
print(string.index('r'))            #返回字符的位置
print(string.isalnum())             #判断是否是字母或者是数字
print(string.isdecimal())           #判断是不是十进制的数
print(string.isdigit())             #判断像不像数字
print(string.isnumeric())           #判断像不像数字
print(string.isidentifier())        #判断是不是非法字符
print(string.islower())             #判断是不是全部小写
print(string.isupper())             #判断是不是全部是大写
print(string.isspace())             #判断是不是含有空格
print(string.istitle())             #判断是不是标题
print(string.lower())               #将所有的大写变成小写
print(string.upper())               #将所有的小写转换成大写
print(string.swapcase())            #将大写转成小写，小写转成大写
print(string.strip())               #将换行符去掉空格也去掉
print(string.replace('old字符','new字符','几个'))             #替换字符
print(string.rfind('o'))               #查找某个字符的索引
print(string.split('l',1))             #将内容按照某个字符分开
print(string.title())                  #按照标题格式进行，每一个单词开头大写


