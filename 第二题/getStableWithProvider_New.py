# -*- coding: utf-8 -*-
# @Time : 2021/9/10 17:04
# @Author : Leviathan_Sei
# @File : getStableWithProvider_New.py
# @Python : 3.7


import csv

with open('stable.csv', encoding='utf-8-sig') as f:
    stable_list = list(csv.reader(f))

with open('provider.csv', encoding='utf-8-sig') as f:
    provider_list = list(csv.reader(f))

name = [provider_list[i][0] for i in range(len(provider_list))]

stable_value = []

# print(name)
for n in name:
    flag = 0
    for stable in stable_list:
        if n == stable[0]:
            flag = 1
            stable_value.append(float(stable[2]))
            break
    if flag == 0:
        print(name)

for i in range(len(provider_list)):
    provider_list[i].append(stable_value[i])

provider_list.sort(key=lambda p: p[2], reverse=True)
provider_list.sort(key=lambda p: p[3], reverse=True)

with open('stableWithProvider_New.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(provider_list)
