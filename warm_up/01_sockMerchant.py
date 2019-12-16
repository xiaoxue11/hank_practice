import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sock_merchant(ar):
    """find how many pairs of socks"""
    d = {}
    d = d.fromkeys(arr, 0)
    print(d)
    for v in ar:
        d[v] = d.get(v, 0) + 1
    print(d)
    count = 0
    for v in d.values():
        count += v//2
    return count


if __name__ == '__main__':
    n = 9
    arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sock_merchant(n, arr))
