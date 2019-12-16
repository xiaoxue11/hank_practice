"""
Created on :  11:05 AM
Author : Xue Zhang
"""
import bisect


def count_inversions1(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        b = arr[i+1:]
        b = sorted(b)
        b_index = binary_search(b, arr[i]) + 1
        count += b_index
    return count


def binary_search(li, value):
    low = 0
    high = len(li) - 1
    index = -1
    while low <= high:
        mid = low + (high-low)//2
        if li[mid] < value:
            index = mid
            low = mid + 1
        else:
            high = mid - 1
    return index


def count_inversions2(arr):
    count = len(arr)*(len(arr)-1)//2
    left = []
    for _, v in enumerate(arr):
        v_idx = bisect.bisect(left, v)
        count -= v_idx
        bisect.insort(left, v)
    return count


def count_inversions3(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        b = arr[i+1:]
        b = sorted(b)
        b_index = bisect.bisect_left(b, arr[i])
        count += b_index
    return count


def merge(a1, a2):
    swaps, i, j, result, m, n = 0, 0, 0, [], len(a1), len(a2)
    ra = result.append
    while i < m and j < n:
        if a1[i] <= a2[j]:
            ra(a1[i])
            i += 1
        else:
            ra(a2[j])
            j += 1
            swaps += m - i
    result += a1[i:]
    result += a2[j:]
    print(swaps, result)
    return swaps, result


def merge_sort(arr):
    n = len(arr)
    mid = n // 2
    if n > 1:
        left_swaps, left_result = merge_sort(arr[:mid])
        right_swaps, right_result = merge_sort(arr[mid:])
        m_swaps, result = merge(left_result, right_result)
        return m_swaps + left_swaps + right_swaps, result
    return 0, arr


if __name__ == '__main__':
    a = [2, 1, 3, 1, 2]
    ret = merge_sort(a)
    print(ret)
