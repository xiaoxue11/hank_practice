"""
Created on :  10:26 PM
Author : Xue Zhang
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        count = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
        if 0 == count:
            break
    return arr


def bubble_sort1(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    s = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    ret = bubble_sort(s)
    print(ret)
    res = bubble_sort1(s)
    print(res)