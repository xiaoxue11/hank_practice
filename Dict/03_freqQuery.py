"""
Created on :  2:51 PM
Author : Xue Zhang
"""

import math
import os
import random
import re
import sys
from collections import Counter
import time


def num_to_dict(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i,0) + 1
    return d


def freq_query(p):
    li = []
    result = []
    for i in range(len(p)):
        if p[i][0] == 1:
            li.append(p[i][1])
        elif p[i][0] == 2:
            if p[i][1] in li:
                li.remove(p[i][1])
        elif p[i][0] == 3:
            d = num_to_dict(li)
            if p[i][1] in d.values():
                result.append(1)
            else:
                result.append(0)
    return result


def freq_query1(p):
    d = {}
    result = []
    for i in range(len(p)):
        op, data = p[i][0], p[i][1]
        if op == 1:
            d[data] = d.get(data, 0) + 1
        elif op == 2:
            if data in d:
                d[data] = d.get(data) - 1
                d[data] = 0 if d[data] < 0 else d[data]
        else:
            print(d.values())
            freq = Counter(d.values())
            print(freq)
            result.append(1 if data in freq else 0)
    return result


def freq_query2(queries):
    freq = Counter()
    cnt = Counter()
    result = []
    for op, data in queries:
        if op == 1:
            cnt[freq[data]] -= 1
            freq[data] += 1
            cnt[freq[data]] += 1
        elif op == 2:
            if freq[data] > 0:
                cnt[freq[data]] -= 1
                freq[data] -= 1
                cnt[freq[data]] += 1
        else:
            result.append(1 if cnt[data] > 0 else 0)
    return result


if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    print(freq_query2(queries))


