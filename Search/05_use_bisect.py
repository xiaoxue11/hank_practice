"""
Created on :  11:15 PM
Author : Xue Zhang
"""

import bisect

if __name__ == '__main__':
    li = [1, 2, 3, 5, 7]
    print(bisect.bisect(li, 2))
    print(bisect.bisect_left(li, 2))
    print(bisect.bisect_right(li, 2))
