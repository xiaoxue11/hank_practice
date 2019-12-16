"""
Created on :  12:23 AM
Author : Xue Zhang
"""


def max_min(k, arr):
    arr.sort()
    print(arr)
    min_gap = arr[k-1] - arr[0]
    for i in range(n-k+1):
        value = arr[i+k-1] - arr[i]
        print(value)
        if min_gap > value:
            min_gap = value
    return min_gap


if __name__ == '__main__':
    n = int(input())
    num = int(input())
    a = []
    for _ in range(n):
        a_item = int(input())
        a.append(a_item)
    result = max_min(num, a)
    print('The value is {}'.format(result))

