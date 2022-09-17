# -*- coding: utf-8 -*-
# @Time : 2021/9/9 20:38
# @Author : Leviathan_Sei
# @File : 合并操作ABC.py
# @Python : 3.7

import csv

with open("KValue/AK_New240.csv", encoding='utf-8-sig') as f:
    AK = list(csv.reader(f))

with open("KValue/BK_New240.csv", encoding='utf-8-sig') as f:
    BK = list(csv.reader(f))

with open("KValue/CK_New240.csv", encoding='utf-8-sig') as f:
    CK = list(csv.reader(f))

AllK = AK + BK + CK
for k in range(len(AllK)):
    AllK[k][2] = float(AllK[k][2])
AllK.sort(key=lambda k: k[2], reverse=True)
with open('KValue/AllK_New240.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(AllK)
