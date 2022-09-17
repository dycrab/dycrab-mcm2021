# -*- coding: utf-8 -*-
# @Time : 2021/9/10 19:25
# @Author : Leviathan_Sei
# @File : getList1.py
# @Python : 3.7

import csv

with open('stable.csv', 'r', encoding='utf-8-sig') as f:
    provider_list = list(csv.reader(f))

name1 = [provider_list[i][0]+"_"+str(i+1) for i in range(len(provider_list))]
v1 = [float(provider_list[i][2]) for i in range(len(provider_list))]

with open('画图需要/name2','w',encoding='utf-8-sig', newline='') as f:

    f.write(str(name1))

# with open('画图需要/v2','w',encoding='utf-8-sig', newline='') as f:
#     f.write(str(v1))
