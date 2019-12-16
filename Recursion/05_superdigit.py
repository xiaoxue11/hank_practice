"""
Created on :  12:27 AM
Author : Xue Zhang
"""


def superDigit1(n, k):
    a = str(n) * k
    b = int(a)
    result = 0
    while b:
        result += b % 10
        b //= 10
    if result < 10:
        return result
    return superDigit(result, 1)


def super_digit(n, k):
    x = n * k % 9
    return x if x else 9


if __name__ == '__main__':
    val = 9875
    count = 4
    ans = super_digit(val, count)
    print(ans)
