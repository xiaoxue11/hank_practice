"""
Created on :  10:04 AM
Author : Xue Zhang
"""


def valid(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def longest_palindrome(s):
    """暴力求解方法"""
    n = len(s)
    max_len = 1
    for i in range(n-1):
        for j in range(i+1, n):
            if j-i+1 > max_len and valid(s, i, j):
                max_len = j-i+1
    return max_len


def longest_palindrome1(s):
    """Manacher  初级方法"""
    new_s = '#' + '#'.join(s) + '#'
    n = len(new_s)
    p = [0] * n
    max_length = 1
    ret = ''
    for i in range(len(new_s)):
        left = i - 1
        right = i + 1
        while left >= 0 and right < n:
            if new_s[left] != new_s[right]:
                break
            left -= 1
            right += 1
            p[i] += 1
        if p[i] > max_length:
            max_length = p[i]
            start = (i - p[i])//2
            end = (i + p[i])//2
            ret = s[start:end]
    return max_length, ret


def longest_palindrome2(s):
    """动态规划方法"""
    n = len(s)
    dp = [[0]*n for j in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for j in range(n):
        for i in reversed(range(j)):
            if j - i == 1:
                if s[j] == s[i]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 0
            else:
                if s[j] == s[i]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = dp[i+1][j-1]
    max_length = 1
    start = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                start = i
    res = s[start: start+max_length]
    return max_length, res


def longest_palindrome3(s):
    """马拉车算法的改进版"""
    new_s = '#' + '#'.join(s) + '#'
    n = len(new_s)
    max_right = 0
    center = 0
    max_length = 1
    start = 0
    p = [0] * n
    for i in range(n):
        if i < max_right:
            mirror = 2 * center - i
            p[i] = min(max_right-i, p[mirror])
        left = i-(1 + p[i])
        right = i + (1+p[i])
        while left >= 0 and right < n and new_s[left] == new_s[right]:
            p[i] += 1
            left -= 1
            right += 1
        if i + p[i] > max_right:
            max_right = i + p[i]
            center = i
        if p[i] > max_length:
            max_length = p[i]
            start = (i-max_length)//2
    return max_length, s[start:start+max_length]


if __name__ == '__main__':
    string = 'babad'
    print(longest_palindrome1(string))
    print(longest_palindrome2(string))
    print(longest_palindrome3(string))




