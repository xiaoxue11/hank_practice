"""
Created on :  10:51 PM
Author : Xue Zhang
"""


def select_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # print(min_index)
    return arr


if __name__ == '__main__':
    s = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(select_sort(s))
