"""
Created on :  10:12 PM
Author : Xue Zhang
"""


def min_absolute_difference(arr):
    result = []
    arr.sort()
    for i in range(len(arr)-1):
        result.append(abs(arr[i]-arr[i+1]))
    return min(result)


if __name__ == '__main__':
    a = [3, -7, 0]
    b = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    c = [1, -3, 71, 68, 17]
    d = [-2, 2, 4]
    print(min_absolute_difference(a))
    print(min_absolute_difference(b))
    print(min_absolute_difference(c))
    print(min_absolute_difference(d))