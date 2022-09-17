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
with open('C:\\Users\\17215\\Desktop\\美赛\\文件\\分表\\' + name + '供货.csv', 'r', encoding='utf-8-sig') as f:
    # 这里将csv.reader()迭代器强制转换为list格式
    list_data_G = list(csv.reader(f))

# 需求
with open('C:\\Users\\17215\\Desktop\\美赛\\文件\\分表\\' + name + '订货.csv', 'r', encoding='utf-8-sig') as f:
    # 这里将csv.reader()迭代器强制转换为list格式
    list_data_X = list(csv.reader(f))

print(len(list_data_X))
K_value = []
sum_of_G = [0, 0]
# 每列 最大最小
MinCol = [int(list_data_G[0][i]) for i in range(2, 242)]
MinCol = [0, 0] + MinCol
MaxCol = [int(list_data_G[0][i]) for i in range(2, 242)]
MaxCol = [0, 0] + MaxCol
# 寻找每列 最大最小值
for index in range(len(list_data_X)):
    for jndex in range(2, 242):
        MinCol[jndex] = min(int(list_data_G[index][jndex]), MinCol[jndex])
        MaxCol[jndex] = max(int(list_data_G[index][jndex]), MaxCol[jndex])

for index in range(len(list_data_X)):
    tmp_list = [list_data_G[index][0], list_data_G[index][1], 0]
    for jndex in range(2, 242):
        flag_k = 1.0
        # print(list_data_X[index][jndex], list_data_G[index][jndex])
        if int(list_data_X[index][jndex]) * 0.9 > int(list_data_G[index][jndex]):
            flag_k -= abs(int(list_data_X[index][jndex]) - int(list_data_G[index][jndex])) / int(
                list_data_X[index][jndex])

        if int(list_data_X[index][jndex]) * 1.5 < int(list_data_G[index][jndex]):
            flag_k -= abs(int(list_data_X[index][jndex]) - int(list_data_G[index][jndex])) / int(
                list_data_X[index][jndex])
        # print(flag_k)

        tmp_value = flag_k * ((int(list_data_G[index][jndex]) - MinCol[jndex]) / (MaxCol[jndex] - MinCol[jndex]))

        tmp_list[2] += tmp_value
    tmp_list[2] /= 240

    K_value.append(tmp_list)

    # print(K_value)
K_value.sort(key=lambda l: l[2], reverse=True)
with open("KValue//" + name + "K_New240.csv", 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(K_value)
