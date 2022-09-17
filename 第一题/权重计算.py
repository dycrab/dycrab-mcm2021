# -*- coding: utf-8 -*-
# @Time : 2021/9/9 19:46
# @Author : Leviathan_Sei
# @File : 权重计算.py
# @Python : 3.7

# A 146
# B 134
# C 122

import csv
name = input('请输入名：')
# 供给
with open('C:\\Users\\17215\\Desktop\\美赛\\文件\\分表\\'+name+'供货.csv', 'r', encoding='utf-8-sig') as f:
    # 这里将csv.reader()迭代器强制转换为list格式
    list_data_G = list(csv.reader(f))

# 需求
with open('C:\\Users\\17215\\Desktop\\美赛\\文件\\分表\\'+name+'订货.csv', 'r', encoding='utf-8-sig') as f:
    # 这里将csv.reader()迭代器强制转换为list格式
    list_data_X = list(csv.reader(f))

print(len(list_data_X))
K_value = []
sum_of_G = [0, 0]
MinCol = []
MaxCol = []
for jndex in range(2, 242):
    sum_of_G.append(0)
for index in range(len(list_data_X)):
    for jndex in range(2, 242):
        sum_of_G[jndex] += int(list_data_G[index][jndex])


for index in range(len(list_data_X)):
    # 计算第index个供需关系的权重

    # 供给
    Tmp_List_G = list_data_G[index]

    # 需求
    Tmp_List_X = list_data_X[index]
    print(Tmp_List_X)
    tmp_list = [Tmp_List_G[0], Tmp_List_G[1], 0]
    # 计算第jndex周的值 并加起来
    RealGX = 240
    for jndex in range(2, 242):
        if int(Tmp_List_X[jndex]) == 0:
            RealGX -= 1
            # print(RealGX)
        try:
            tmp_value = (int(Tmp_List_G[jndex]) / int(Tmp_List_X[jndex])) * (
                        int(Tmp_List_G[jndex]) / int(sum_of_G[jndex]))
        except ZeroDivisionError:
            tmp_value = 0
        try:
            tmp_list[2] += (tmp_value / RealGX) * 240
        except ZeroDivisionError:
            print(tmp_value)
            tmp_list[2] += tmp_value
    K_value.append(tmp_list)
    # print(K_value)
K_value.sort(key=lambda l: l[2], reverse=True)
with open("KValue//"+name+"K_New.csv", 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(K_value)
