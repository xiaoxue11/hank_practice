"""
Created on :  11:59 AM
Author : Xue Zhang
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    number = int(input())
    print(fibonacci(number))
