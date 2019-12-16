"""
Created on :  9:46 AM
Author : Xue Zhang
"""
import math


def primality(n):
    if n < 2:
        return 'Not prime'
    elif n == 2:
        return 'Prime'
    elif n % 2 == 0:
        return 'Not prime'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'


if __name__ == '__main__':
    a = 4
    result = primality(a)
    print(result)