# -*- coding: utf-8 -*-
# @Time : 2021/9/11 9:12
# @Author : Leviathan_Sei
# @File : getAvgWasteRate.py
# @Python : 3.7

import csv
import math


def getAvg(list):
    new_list = []
    for i in list:
        if float(i) != 0:
            new_list.append(float(i))
    return sum(new_list)/len(new_list)


with open('WasteRate.csv', encoding='utf-8-sig') as f:
    WasteRate = list(csv.reader(f))

AvgWasteRate = []
for one in WasteRate:
    tmp = [one[0], getAvg(one[1:])]
    AvgWasteRate.append(tmp)

AvgWasteRate.sort(key=lambda AWR: AWR[1])

with open('AvgWasteRate.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(AvgWasteRate)
