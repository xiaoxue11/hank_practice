# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:12:09 2019

@author: 29132
"""


def getchar(s):
    d = {}
    for char in s:
        d[char] = d.get(char, 0) + 1
    return d


def two_strings(s1, s2):
    hash1 = getchar(s1)
    hash2 = getchar(s2)
    for i in hash1.keys():
        if i in hash2.keys():
            return 'YES'
        else:
            continue
    return 'NO'


a1 = 'hello, everyone'
a2 = 'The word is very beautiful'
res = two_strings(a1, a2)
print(res)
