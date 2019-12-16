import math
import os
import random
import re
import sys
import time


def minimum_swaps(arr):
    steps = 0
    p = [i-1 for i in arr]
    pos = {v: k for k, v in enumerate(p)}
    for i, v in enumerate(p):
        if v != i:
            p[i], p[pos[i]] = p[pos[i]], p[i]
            pos[i], pos[v] = pos[v], pos[i]
            steps += 1
    return steps


if __name__ == '__main__':
    a = [4, 3, 1, 2]
    b = [2, 3, 4, 1, 5]
    t1 = time.time()
    print(minimum_swaps(a))
    t2 = time.time()
    print(t2-t1)