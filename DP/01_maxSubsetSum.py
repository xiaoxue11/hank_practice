"""
Created on :  10:09 PM
Author : Xue Zhang
"""


def max_subset_sum1(a):
    n = len(a)
    li = []
    for i in range(n):
        for j in range(i+2, n):
            while j+2 < n:
                li.append(tuple(a[i], a[j], a[j+2]))


def max_subset_sum(a):
    n = len(a)
    dp = [0] * (n+1)
    dp[1] = a[0]
    dp[2] = max(a[1], a[0])
    for i in range(2, n):
        dp[i+1] = max(max(dp[i-1], dp[i-2], 0) + a[i], dp[i])
    print(dp)


if __name__ == '__main__':
    arr = [3, 5, -7, 8, 10]
    max_subset_sum(arr)