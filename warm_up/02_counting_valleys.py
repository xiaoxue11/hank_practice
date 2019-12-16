import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def counting_valleys(s1):
    """find the num of valleys that the hiker experience"""
    d = {
        "U": 1,
        "D": -1,
    }
    current_sum = 0
    num = 0
    for c in s1:
        current_sum += d[c]
        if current_sum == 0 and c == 'U':
            num += 1
    return num


if __name__ == '__main__':
    s = 'DDUUDDUDUUUD'
    print(counting_valleys(s))