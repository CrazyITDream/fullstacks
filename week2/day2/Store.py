#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: Store.py
@time: 2019/1/15 12:09
"""
product_list =[
    ('Mac',9000),
    ('Kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),
]

money = input('Please input your money:')
Store =[]
if money.isdigit():
    saving=int(money)
    while True:
        for i,v in  enumerate(product_list,1):
            print(i,'>>>>>',v)
        choice = input('请你选择要购买的商品[退出:0]：')

        if choice.isdigit():
            choice=int(choice)
            if choice > 0 and choice < len(product_list):

                item=product_list[choice-1]

                if item[1] < money:
                    money -= item[1]
                    Store.append(item)
                    print('%s'%money)
                else:
                    print('余额不足,还剩下%s'%money)
            else:
                print('Error')
        elif choice == '0':
                print('- - - - - - - 你购买的商品如下 - - - - - - - ')
                for i in Store:
                    print(i)
                    print('你还剩下钱%s元'%money)
                    print('- - - - - - - 欢迎你下次光临 - - - - - - - ')
                break
        else:
            print('请你输入正确编号:')
else:
    print('请输入数字')
