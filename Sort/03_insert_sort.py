"""
Created on :  11:05 PM
Author : Xue Zhang
"""


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


if __name__ == '__main__':
    s = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insert_sort(s))
