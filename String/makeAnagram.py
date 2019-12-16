# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:21:49 2019

@author: 29132
"""


def make_anagram(a, b):
    chars = a + b
    count = 0
    for char in chars:
        count += abs(a.count(char) - b.count(char))
    return count


if __name__ == '__main__':
    fptr = open('../../Hanker_rank/Interview/string_manipulation/text.txt', 'w')
    s1 = input()
    s2 = input()
    res = make_anagram(s1, s2)
    fptr.write(str(res) + '\n')
    fptr.close()
