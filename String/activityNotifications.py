# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:37:32 2019

@author: 29132
"""

def activityNotifications(expenditure, d):
    notice=0
    for i in range(d,len(expenditure)):
        res=[]
        for j in range(i-d,i):
            res.append(expenditure[j])
            res.sort()
        if d%2==0:
            median=(res[d//2-1]+res[d//2])
        else:
            median=res[d//2]*2
        if expenditure[i]>=median:
            notice+=1
    return notice
expenditure=[10,20,30,40,50]
d=3     
result=activityNotifications(expenditure, d) 


#%%=========================
def get_median(counts, mids):
    res = []
    for mid in mids:
        gone = 0
        for i, v in enumerate(counts):
            gone += v
            if gone >= mid:
                res.append(i)
                break
    return sum(res) / len(res)
def activityNotifications(expenditure, d):
    alerts = 0
    counts = [0] * 201
    if d % 2 == 1:
        mids = [d // 2 + 1]
    else:
        mids = [d // 2, d // 2 + 1]
    for v in expenditure[:d]:
        counts[v] += 1
    for i, exp in enumerate(expenditure[d:]):
        median = get_median(counts, mids)
        if exp >= 2 * median:
            alerts += 1  
        old_value = expenditure[i]
        counts[old_value] -= 1
        counts[exp] += 1
    return alerts      


        