# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:20:50 2019

@author: 29132
"""


# !/bin/python3

def matching_strings(strings, queries):
    res = [0 for i in range(len(queries))]
    for i in range(len(queries)):
        res[i] = strings.count(queries[i])
    return res


if __name__ == '__main__':
    strings_count = int(input())
    s = []
    for _ in range(strings_count):
        strings_item = input()
        s.append(strings_item)
    queries_count = int(input())
    q = []
    for _ in range(queries_count):
        queries_item = input()
        q.append(queries_item)
    ret = matching_strings(s, q)
    print('\n'.join(map(str, ret)))
