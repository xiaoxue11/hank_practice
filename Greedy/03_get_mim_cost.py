"""
Created on :  11:16 PM
Author : Xue Zhang
"""
from collections import deque


def get_minimum_cost(k, c):
    if len(c) <= k:
        return sum(c)
    c.sort()
    min_cost = 0
    count = k
    j = 1
    while c and count:
        min_cost += j * c.pop()
        count -= 1
        if count == 0:
            j += 1
            count = k
    return min_cost


if __name__ == '__main__':
    a = [2, 5, 6]
    k = 3
    print(get_minimum_cost(k, a))





