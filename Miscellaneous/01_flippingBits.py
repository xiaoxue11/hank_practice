"""
Created on :  9:39 AM
Author : Xue Zhang
"""


def flipping_bits(n):
    max_value = 4294967295
    return max_value - n


if __name__ == '__main__':
    a = 2
    result = flipping_bits(a)
    print(result)