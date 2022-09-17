# -*- coding: utf-8 -*-
# @Time : 2021/9/12 1:21
# @Author : Leviathan_Sei
# @File : getOneWeek.py
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

# print(Name)
Ans = []

for name in Name:
    flag = 0
    for base in Base:
        if name == base[0]:
            flag = 1
            Ans.append([name, base[-2]])
    if flag == 0:
        Ans.append([name, ''])

with open('Ans1.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(Ans)
print(Ans)

