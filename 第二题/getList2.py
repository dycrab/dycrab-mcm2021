# -*- coding: utf-8 -*-
# @Time : 2021/9/10 21:39
# @Author : Leviathan_Sei
# @File : getList2.py
# @Python : 3.7

import csv

with open('stableWithProvider_New.csv', encoding='utf-8-sig') as f:
    swpn = list(csv.reader(f))

name3 = [swpn[i][0] for i in range(len(swpn))]
v31 = [swpn[i][2] for i in range(len(swpn))]
v32 = [swpn[i][3] for i in range(len(swpn))]

with open('画图需要/name3', 'w', encoding='utf-8-sig', newline='') as f:
    f.write(str(name3))
with open('画图需要/v31', 'w', encoding='utf-8-sig', newline='') as f:
    f.write(str(v31))
with open('画图需要/v32', 'w', encoding='utf-8-sig', newline='') as f:
    f.write(str(v32))
