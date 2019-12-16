# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:00:36 2019

@author: 29132
"""

def countSwaps(a):
    n=len(a)
    step=0
    for i in range(n):
        for j in range(n-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                step+=1
    print("Array is sorted in {} swaps.".format(step))
    print('First Element: {}'.format(min(a)))
    print('Last Element: {}'.format(max(a)))
a=[6,4,1]
countSwaps(a)