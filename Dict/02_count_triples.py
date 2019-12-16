"""
Created on :  9:23 AM
Author : Xue Zhang
"""


def count_triples(s, r):
    nums = 0
    n = len(s)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if s[j] == s[i]*r and s[k] == s[j]*r:
                    nums += 1
    return nums


def count_triples1(s, r):
    count = 0
    d1 = {}
    d2 = {}
    for i in reversed(s):
        if i * r in d2:
            count += d2[i * r]
        if i * r in d1:
            d2[i] = d2.get(i, 0) + d1[i * r]
        d1[i] = d1.get(i, 0) + 1
    return count


if __name__ == '__main__':
    arr = [1, 5, 5, 25, 125]
    ratio = 5
    print(count_triples(arr, ratio))
    print(count_triples1(arr, ratio))



