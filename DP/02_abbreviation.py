"""
Created on :  11:51 PM
Author : Xue Zhang
"""


def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n + 1):
        for j in range(1, m + 1):
            if a[j - 1] == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif a[j - 1].upper() == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1]
            elif a[j - 1].islower():
                dp[i][j] = dp[i][j - 1]
    return "YES" if dp[n][m] else "NO"


if __name__ == '__main__':
    s1 = 'daBcd'
    s2 = 'ABC'
    print(abbreviation(s1, s2))

