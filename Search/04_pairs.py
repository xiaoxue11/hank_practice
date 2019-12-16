"""
Created on :  9:47 AM
Author : Xue Zhang
"""


def pairs(k, arr):
    # d = {}
    # count = 0
    # for v in arr:
    #     if v > k:
    #         d[v] = v - k
    #     else:
    #         d[v] = k - v
    # for key, value in d.items():
    #     if key in arr and value in arr and key != value:
    #         count += 1
    # return count
    return len(set([x + k for x in arr]).intersection(set(arr)))


if __name__ == '__main__':
    a = [1, 5, 3, 4, 2]
    target = 2
    result = pairs(target, a)
    print(result)
