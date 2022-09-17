# -*- coding: utf-8 -*-
# @Time : 2021/9/10 16:37
# @Author : Leviathan_Sei
# @File : getStable.py
# @Python : 3.7

import csv

def getStable(list):

    cnt = 0
    for i in list:
        if int(i) != 0:
            cnt += 1
    return cnt/240

with open('supply.csv', encoding='utf-8-sig') as f:
    supply_list = list(csv.reader(f))

stable_list = []
for supply in supply_list:
    tmp_stable = [supply[0], supply[1], getStable(supply[2:242])]
    stable_list.append(tmp_stable)
stable_list.sort(key=lambda stb: stb[2], reverse=True)
with open('stable.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(stable_list)

