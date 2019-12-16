"""
Created on :  10:47 AM
Author : Xue Zhang
"""


def quick_sort(a, first, last):
    if first >= last:
        return
    mid_value = a[first]
    low = first
    high = last
    while low < high:
        while low < high and a[high] >= mid_value:
            high -= 1
        a[low] = a[high]
        while low < high and a[low] < mid_value:
            low += 1
        a[high] = a[low]
    a[low] = mid_value
    quick_sort(a, first, low-1)
    quick_sort(a, low+1, last)


if __name__ == '__main__':
    s = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('before sort: {}'.format(s))
    quick_sort(s, 0, len(s)-1)
    print('after sort: {}'.format(s))
