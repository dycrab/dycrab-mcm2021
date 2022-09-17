# -*- coding: utf-8 -*-
# @Time : 2021/9/10 15:41
# @Author : Leviathan_Sei
# @File : getProvider.py
# @Python : 3.7

# -*- coding: utf-8 -*-
# @Time : 2021/9/10 8:29
# @Author : Leviathan_Sei
# @File : getProvider_AC_Supply.py
# @Python : 3.7

import csv


def getSupply(supply_one):
    # print(supply_one)
    ans = 0
    for i in supply_one:
        ans += int(i)
    ans_list = []
    # print(ans, supply_one[0])
    for i in supply_one:

        ans_list.append(int(i) * (1 / 240))

    return sum(ans_list)


# with open('provider.csv', 'r', encoding='utf-8-sig') as f:
#     provider = list(csv.reader(f))

with open('supply.csv', 'r', encoding='utf-8-sig') as f:
    supply_list = list(csv.reader(f))


# 总
# 'S005':supply
supply_ability_a = {}
supply_ability_b = {}
supply_ability_c = {}

# save_list
supply_ability_a_list = []
supply_ability_b_list = []
supply_ability_c_list = []

for supply_one in supply_list:
    if supply_one[1] == 'A':
        tmpSupply = getSupply(supply_one[2:242])
        supply_ability_a[supply_one[0]] = tmpSupply
        supply_ability_a_list.append([supply_one[0], tmpSupply])
    if supply_one[1] == 'B':
        tmpSupply = getSupply(supply_one[2:242])
        supply_ability_b[supply_one[0]] = tmpSupply
        supply_ability_b_list.append([supply_one[0], tmpSupply])
    if supply_one[1] == 'C':
        tmpSupply = getSupply(supply_one[2:242])
        supply_ability_c[supply_one[0]] = tmpSupply
        supply_ability_c_list.append([supply_one[0], tmpSupply])

supply_ability_a_list.sort(key=lambda k: k[1], reverse=True)
supply_ability_b_list.sort(key=lambda k: k[1], reverse=True)
supply_ability_c_list.sort(key=lambda k: k[1], reverse=True)

with open('stableWithProvider_New.csv', encoding='utf-8-sig') as f:
    swpn = list(csv.reader(f))

for one in swpn:
    for supply in supply_ability_a_list:
        if supply[0] == one[0]:
            swpn[swpn.index(one)].append(supply[1])
    for supply in supply_ability_b_list:
        if supply[0] == one[0]:
            swpn[swpn.index(one)].append(supply[1])
    for supply in supply_ability_c_list:
        if supply[0] == one[0]:
            swpn[swpn.index(one)].append(supply[1])


with open('stableWithAvgProvider_New.csv', 'w', encoding='utf-8-sig', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(swpn)

# with open('supply_ability_a_avg.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     wt = csv.writer(f)
#     wt.writerows(supply_ability_a_list)
#
# with open('supply_ability_b_avg.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     wt = csv.writer(f)
#     wt.writerows(supply_ability_b_list)
#
# with open('supply_ability_c_avg.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     wt = csv.writer(f)
#     wt.writerows(supply_ability_c_list)
