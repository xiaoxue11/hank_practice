"""
Created on :  11:41 AM
Author : Xue Zhang
"""
import bisect


def triplets1(a, b, c):
    count = 0
    for p in a:
        for q in b:
            for r in c:
                if p <= q and q >= r:
                    count += 1
    return count


def triplets2(a, b, c):
    count = 0
    new_a = sorted(set(a))
    new_b = sorted(set(b))
    new_c = sorted(set(c))
    for b_v in new_b:
        a_count = 0
        c_count = 0
        for a_v in new_a:
            if a_v <= b_v:
                a_count += 1
        for c_v in new_c:
            if c_v <= b_v:
                c_count += 1
        count += a_count * c_count
    return count


def triplets3(a, b, c):
    count = 0
    new_a = sorted(set(a))
    new_b = sorted(set(b))
    new_c = sorted(set(c))
    for b_v in new_b:
        a_count = binary_search(new_a, b_v) + 1
        c_count = binary_search(new_c, b_v) + 1
        count += a_count * c_count
    return count


def binary_search(li, value):
    if li is None:
        return
    index = -1
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if li[mid] <= value:
            index = mid
            low = mid + 1
        else:
            high = mid - 1
    return index


def triplets(a, b, c):
    new_a = sorted(set(a))
    new_b = sorted(set(b))
    new_c = sorted(set(c))
    return sum([bisect.bisect(new_a, x) * bisect.bisect(new_c, x) for x in new_b])


if __name__ == '__main__':
    arr1 = [1, 3, 5]
    arr2 = [2, 3]
    arr3 = [1, 2, 3]
    ret1 = triplets1(arr1, arr2, arr3)
    ret2 = triplets2(arr1, arr2, arr3)
    print(ret1)
    print(ret2)
    print(triplets(arr1, arr2, arr3))
    print(triplets3(arr1, arr2, arr3))