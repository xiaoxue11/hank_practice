"""
Created on :  4:06 PM
Author : Xue Zhang
"""


# def find(arr, a, b):
#     if arr[a] == arr[b]:
#         return True
#     else:
#         return False
#
#
# def union(arr, a, b):
#     temp = arr[a]
#     for i in range(n):
#         if arr[i] == temp:
#             arr[a] = arr[b]
#     return arr

def root1(arr, i):
    while arr[i] != i:
        print(arr[i])
        print(i)
        i = arr[i]
    return i


def root(arr, i):
    while arr[i] != i:
        arr[i] = arr[arr[i]]
        i = arr[i]
    return i


def union(arr, a, b):
    root_a = root(arr, a)
    root_b = root(arr, b)
    arr[root_a] = root_b
    return arr


def weighted_union(arr, s, a, b):
    root_a = root(arr, a)
    root_b = root(arr, b)
    print(root_a)
    print(root_b)
    if s[root_a] < s[root_b]:
        arr[root_a] = arr[root_b]
        s[root_b] += s[root_a]
    else:
        arr[root_b] = arr[root_a]
        s[root_a] += s[root_b]
    return arr, s


def find(a, b):
    if root(a) == root(b):
        return True
    else:
        return False


if __name__ == '__main__':
    n = 10
    array = [i for i in range(n)]
    size = [1 for _ in range(n)]
    print(weighted_union(array, size, 0, 1))
    print(weighted_union(array, size, 1, 2))
    print(weighted_union(array, size, 3, 2))

