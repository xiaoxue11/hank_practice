"""
Created on :  7:40 PM
Author : Xue Zhang
"""
import bisect


def decibinary_numbers1(n):
    result = 0
    v, c = pre_computer()
    l = bisect.bisect(c, n-1)-1
    value = l - 0
    offset = (n-1) - c[l]
    for i in range(19, 0, -1):
        power = 1 << i
        for digit in range(10):
            v1 = value - digit*power
            if offset < v[v1][i-1]:
                result += digit
                value -= power*digit
                break
            offset -= v[v1][i-1]
        result *= 10
    result += value
    return result


def decibinary_numbers(x):
    dp = dict()
    dp[0] = [0]
    count = 1
    i = 1
    while count < x:
        dp[i] = []
        for v in dp[i-1]:
            dp[i].append(v + 1)
            j = 10
            while v != 0 and (v % 10 + 1 == 2):
                new_v = (v // 10 + 1) * j
                dp[i].append(new_v)
                v //= 10
                j *= 10
        count += len(dp[i])
        i += 1
    print(count)
    return dp


def pre_computer():
    dmax = 300000
    digits = 10
    powers = 20
    v = dict()
    c = list()
    for i in range(dmax):
        v[i] = [0] * powers
        c.append(0)
    for i in range(dmax):
        v[i][0] = i < digits
        for j in range(1, powers):
            for k in range(digits):
                value = i - k * (1 << j)
                if value < 0:
                    break
                v[i][j] += v[value][j - 1]
    for i in range(1, dmax):
        c[i] = v[i - 1][powers - 1] + c[i - 1]
    return v, c


# def decibinary_numbers2(x):
#     result = 0
#     digits = 10
#     powers = 20
#     v = dict()
#     c = [0]
#     i = 0
#     l = bisect.bisect(c, x - 1) - 1
#     while l > c[-1]:
#         v[i] = [0] * powers
#         v[i][0] = i < digits
#         for j in range(1, powers):
#             for k in range(digits):
#                 value = i - k * (1 << j)
#                 if value < 0:
#                     break
#                 v[i][j] += v[value][j - 1]
#         if i > 1:
#             c.append(v[i - 1][powers - 1] + c[i - 1])
#         i += 1
#     value = l
#     offset = (x - 1) - c[l]
#     for i in range(19, 0, -1):
#         power = 1 << i
#         for digit in range(10):
#             v1 = value - digit * power
#             if offset < v[v1][i - 1]:
#                 result += digit
#                 value -= power * digit
#                 break
#             offset -= v[v1][i - 1]
#         result *= 10
#     result += value
#     return result


if __name__ == '__main__':
    ret = decibinary_numbers1(3)
    ret1 = decibinary_numbers(60)
    vector, c_value = pre_computer()
    # print(vector)
    # print(c_value)
    print('The result value is: {}'.format(ret))

