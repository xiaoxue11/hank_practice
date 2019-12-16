
import math
import os
import random
import re
import sys


def minimum_bribes(q):
    p = [i-1 for i in q]
    steps = 0
    for i, v in enumerate(p):
        if (v-i) > 2:
            print('Too chaotic')
        for j in range(max(0, v-1), i):
            if q[j] > v:
                steps += 1
    return steps


if __name__ == '__main__':
    a = [2, 1, 5, 3, 4]
    print(minimum_bribes(a))