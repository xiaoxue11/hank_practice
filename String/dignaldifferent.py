# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:28:16 2019

@author: 29132
"""

def diagonalDifferent(arr):
    sum1=0
    sum2=0
    for i in range(len(arr)):
        sum1+=arr[i][i]
        sum2+=arr[i][len(arr)-i-1]
    return abs(sum1-sum2)

def plusMinus(arr):
    pos_num=0
    neg_num=0
    n=len(arr)
    for i in range(len(arr)):
        if arr[i]>0:
            pos_num+=1
        elif arr[i]<0:
            neg_num+=1
    pos_rate=pos_num/n
    neg_rate=neg_num/n
    print('{:.6f}'.format(pos_rate))
    print('{:.6f}'.format(neg_rate))
    print('{:.6f}'.format(1-pos_rate-neg_rate))
arr=[-4,3,-9,0,4,1]
plusMinus(arr)

def staircase(n):
    for i in range(1,n+1):
        print((n-i)*' '+i*'#')
staircase(7)
#%%======================
arr=[1,2,3,4,5]
sum_arr=0
for i in range(4):
    sum_arr+=arr[i]
sum_max=sum_arr
sum_min=sum_arr
for i in range(len(arr)):
    arr1=arr.copy()
    sum_arr1=0
    for j in range(len(arr)):
        if j==i:
            arr1[j]=0
        sum_arr1+=arr1[j]       
    if sum_arr1>sum_max:
        sum_max=sum_arr1
    elif sum_arr1< sum_min: 
        sum_min=sum_arr1
print(sum_min,sum_max)



    
            