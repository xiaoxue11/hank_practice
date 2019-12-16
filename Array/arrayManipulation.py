# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:00:31 2019

@author: 29132
"""


def array_manipulation(n, queries):
    arr = [0] * n
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        for j in range(a - 1, b):
            arr[j] += k
    return max(arr)


def array_manipulation1(n, queries):
    array = [0] * (n + 1)
    max_value = 0
    running_count = 0
    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
    return max_value


if __name__ == '__main__':
    num1 = 5
    q = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    print(array_manipulation(num1, q))
