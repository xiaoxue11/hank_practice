"""
Created on :  3:10 PM
Author : Xue Zhang
"""


def bfs(grid, mark, x, y):
    mark[x][y] = 1
    m, n = len(mark) - 1, len(mark[0]) - 1
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        new_x = dx[i] + x
        new_y = dy[i] + y
        if new_x < 0 or new_x > m or new_y < 0 or new_y > n:
            continue
        if mark[new_x][new_y] == 0 and grid[new_x][new_y] == 1:
            bfs(grid, mark, new_x, new_y)


def maxRegion(grid):
    regions = []
    mark = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if mark[i][j] == 0 and grid[i][j] == 1:
                bfs(grid, mark, i, j)
                region = sum([sum(ai) for ai in mark])
                regions.append(region)
    ans = list()
    ans.append(regions[0])
    for i in range(1, len(regions)):
        ans.append(regions[i] - regions[i-1])
    return max(ans)


if __name__ == '__main__':
    n1 = int(input())
    m1 = int(input())
    g = []
    for _ in range(n1):
        g.append(list(map(int, input().rstrip().split())))
    res = maxRegion(g)
    print(res)