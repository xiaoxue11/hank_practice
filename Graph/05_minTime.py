"""
Created on :  10:31 PM
Author : Xue Zhang
"""
from collections import defaultdict


def construct_graph(roads):
    g = defaultdict(list)
    for c1, c2, c in roads:
        g[c1].append(c2)
        g[c2].append(c1)
    return g


def minTime(roads, machines):
    pass


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    rs = []
    for _ in range(n - 1):
        rs.append(list(map(int, input().rstrip().split())))
    ms = []
    for _ in range(k):
        machines_item = int(input())
        ms.append(machines_item)
    # result = minTime(rs, ms)
    print(construct_graph(rs))