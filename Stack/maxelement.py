# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:19:25 2019

@author: 29132
"""
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
n=int(input())
queries=[]
for _ in range(n):
    queries.append(list(map(int, input().rstrip().split())))
stack=Stack()
for i in range(len(queries)):
    flag=queries[i][0]
    if flag==1:
        stack.push(queries[i][1])
    if flag==2:
        stack.pop()
    if flag==3:
        print(max(stack.items))

items = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        items.append(max(nums[1], items[-1]))
    elif nums[0] == 2:
        items.pop()
    else:
        print(items[-1])