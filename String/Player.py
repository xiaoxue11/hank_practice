# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:52:15 2019

@author: 29132
"""
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def __repr__(self):
        pass
    def comparator(a, b):
        value=b.score-a.score
        if value==0:
            if a.name<b.name:
                return -1
            else: return 1
        return value         
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)   
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
            
                
            