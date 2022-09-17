# -*- coding: utf-8 -*-
# @Time : 2021/9/12 1:29
# @Author : Leviathan_Sei
# @File : getTransAns.py
# @Python : 3.7

import csv

with open('BASE.csv', encoding='utf-8-sig') as f:
    Base = list(csv.reader(f))

Name = []

for i in range(1, 403):
    tmp = ''
    if len(str(i)) == 1:
        tmp = '00' + str(i)
    elif len(str(i)) == 2:
        tmp = '0' + str(i)
    else:
        tmp = str(i)
    tmp = 'S' + tmp
    Name.append(tmp)

Ans = []

TKV = {
    'T1': 0,
    'T2': 1,
    'T3': 2,
    'T4': 3,
    'T5': 4,
    'T6': 5,
    'T7': 6,
    'T8': 7,
}

for name in Name:

    tmp = [name, '', '', '', '', '', '', '', '']
    for base in Base:
        if name == base[0]:
            tmp[TKV[base[-1]]+1] = base[-2]
            break

    Ans.append(tmp)
with open('Ans2.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(Ans)
print(Ans)
