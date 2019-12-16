# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:32:12 2019

@author: 29132
"""


# Complete the dynamicArray function below.
def dynamic_array(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    res = []
    for i in range(len(queries)):
        q = queries[i]
        flag = q[0]
        x = q[1]
        y = q[2]
        if flag == 1:
            index = (x ^ lastAnswer) % n
            seqList[index].append(y)
        if flag == 2:
            index = (x ^ lastAnswer) % n
            lastAnswer = seqList[index][y % len(seqList[index])]
            print(lastAnswer)
            res.append(lastAnswer)
    return res


if __name__ == '__main__':
    nq = input().rstrip().split()
    n = int(nq[0])
    q = int(nq[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamic_array(n, queries)
    print(result)
