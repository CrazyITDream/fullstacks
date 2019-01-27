#!/usr/bin/python
#coding:utf-8

"""
@author: 小火
@contact: xx@xx.com
@software: PyCharm
@file: 3menu.py
@time: 2019/1/20 10:54
"""

menu = {
    '广州':{
        '天河':{
            '华南农业大学':{}
        },
        '黄埔':{
            '航海学院':{}
        },
        '白云':{
            '白云学院':{}
        },
        '越秀':{
            '越秀公园':{}
        },
        '海珠':{
            '中山大学':{}
        },
        '荔湾':{
            '上下九':{}
        },
        '从化':{
            '珠江学院':{}
        },
        '增城':{
            '华工':{}
        },
    },
    '深圳':{
        '南山':{},
    },
    '珠海':{
        '香洲':{
            '前山':{
                '前山城轨站':{}
            },
            '明珠':{
                '明珠城轨站':{}
            },
        },
        '斗门':{
            '斗门机场':{},
        },
        '唐家':{
            '唐家站':{}
        },
    },
}

current_layer = menu
parent_layers = {}
while True:
    for key in current_layer:
        print(key)
    choice = input("请输入城市：")
    if len(choice) ==0:
        continue
    if choice in current_layer:
        parent_layer = current_layer
        current_layer=current_layer[choice]
    elif choice=='b':
            if parent_layer:
                    current_layer = parent_layers.pop()
    else:
        print('无此项')
