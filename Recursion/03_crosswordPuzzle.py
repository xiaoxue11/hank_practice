"""
Created on :  3:20 PM
Author : Xue Zhang
"""

import sys


class CrosswordPuzzle:
    def __init__(self, crossword):
        self.board = crossword

    def print_board(self):
        for row in self.board:
            print(''.join(row))

    def possible_directions(self, word):
        length = len(word)
        for i in range(10):
            for j in range(10):
                properSlotH = True
                properSlotV = True
                for k in range(length):
                    # Horizontal direction, axis marked as 0:
                    if j < 10 - length + 1:
                        if self.board[i][j + k] not in ['-', word[k]]:
                            properSlotH = False

                    # Vertival direction, axis marked as 1:
                    if i < 10 - length + 1:
                        if self.board[i + k][j] not in ['-', word[k]]:
                            properSlotV = False
                if properSlotH and j < 10 - length + 1:
                    yield i, j, 0
                if properSlotV and i < 10 - length + 1:
                    yield i, j, 1

    def move(self, word, startLocation):
        i, j, axis = startLocation
        length = len(word)
        if axis == 0:
            for k in range(length):
                self.board[i][j + k] = word[k]
        else:
            for k in range(length):
                self.board[i + k][j] = word[k]

    def rollback(self, word, startLocation):
        i, j, axis = startLocation
        length = len(word)
        if axis == 0:
            for k in range(length):
                self.board[i][j + k] = '-'
        else:
            for k in range(length):
                self.board[i + k][j] = '-'

    def solve(self, words):
        global solved
        if len(words) == 0:
            if not solved:
                self.print_board()
            solved = True
            return

        word = words.pop()

        for direction in self.possible_directions(word):
            self.move(word, direction)
            self.solve(words)
            self.rollback(word, direction)
        words.append(word)


if __name__ == '__main__':
    grid = []
    for _ in range(10):
        grid_item = list(input())
        grid.append(grid_item)
    words = str(input()).split(";")
    solved = False
    s = CrosswordPuzzle(grid)
    s.solve(words)
    print(s.board)
