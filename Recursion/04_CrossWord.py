"""
Created on :  11:08 PM
Author : Xue Zhang
"""


import math
import os
import random
import re
import sys


def print_crossword(crossword):
    for row in crossword:
        print(''.join(row))


def get_possible_start(crossword, word):
    length = len(word)
    for i in range(10):
        for j in range(10):
            proper_h = True
            proper_v = True
            for k in range(length):
                if j < 10 - length + 1 and crossword[i][j+k] not in ['-', word[k]]:
                    proper_h = False
                if i < 10 - length + 1 and crossword[i+k][j] not in ['-', word[k]]:
                    proper_v = False
            if proper_h and j < 10 - length + 1:
                yield i, j, 0
            if proper_v and i < 10 - length + 1:
                yield i, j, 1


def fill_word(crossword, word, start_point):
    i, j, axis = start_point
    if axis == 0:
        for k in range(len(word)):
            crossword[i][j+k] = word[k]
    if axis == 1:
        for k in range(len(word)):
            crossword[i+k][j] = word[k]


def rollback_word(crossword, word, start_point):
    i, j, axis = start_point
    if axis == 0:
        for k in range(len(word)):
            crossword[i][j+k] = '-'
    if axis == 1:
        for k in range(len(word)):
            crossword[i+k][j] = '-'


def crossword_puzzle(crossword, words):
    global flag
    if len(words) == 0:
        if not flag:
            print_crossword(crossword)
        return
    word = words.pop()
    for start in get_possible_start(crossword, word):
        fill_word(crossword, word, start)
        crossword_puzzle(crossword, words)
        rollback_word(crossword, word, start)
    words.append(word)


if __name__ == '__main__':
    cw = []
    for _ in range(10):
        cw_item = list(input())
        cw.append(cw_item)
    # print(cw)
    ws = str(input()).split(";")
    # print_crossword(cw)
    flag = False
    crossword_puzzle(cw, ws)
    print(cw)


