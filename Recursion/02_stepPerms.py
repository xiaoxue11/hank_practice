"""
Created on :  3:08 PM
Author : Xue Zhang
"""


def step_perms(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n] % (10**10 + 1)


if __name__ == '__main__':
    steps = [1, 3, 7]
    for step in steps:
        print(step_perms(step))
