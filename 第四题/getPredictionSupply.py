# -*- coding: utf-8 -*-
# @Time : 2021/9/11 22:05
# @Author : Leviathan_Sei
# @File : getPredictionSupply.py
# @Python : 3.7


import csv


def get24Week(Test_list):
    ans = []
    for i in range(24):
        tmp = (sum(Test_list)/len(Test_list))
        ans.append(tmp)
        Test_list.append(tmp)
    return ans

def get24Week2(Test_list):
    ans = []
    for i in range(24):
        first = 0
        k = 0.5
        on = 0
        for test in reversed(Test_list):
            first += k*pow((1-k), on)*test
            # print(test, first)
            on += 1
        print(first)
        Test_list.append(first)
        ans.append(first)
    # for i in range(24):
    #     tmp = k*pow((1-k), on)*Test_list[-1]
    #     ans.append(tmp)
    #     Test_list.append(tmp)
    return ans


with open('测试.csv', encoding='utf-8-sig') as f:
    supply = list(csv.reader(f))

prediction = []

for one in supply:
    prediction.append([one[0], one[1]]+get24Week2(list(map(int,one[2:]))))


with open('prediction_supply2.csv', 'w', encoding='utf-8', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(prediction)

