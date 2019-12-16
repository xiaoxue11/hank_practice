from collections import deque


def near_point(arr, x, y):
    points = []
    n = len(arr)

    i = x
    while i > 0:
        i -= 1
        if arr[i][y] == 'X':
            break
        points.append((i, y))

    i = x
    while i < n-1: 
        i += 1
        if arr[i][y] == 'X': 
            break
        points.append((i,y)) 

    i = y
    while i > 0:
        i -= 1
        if arr[x][i] == 'X':
            break
        points.append((x, i))

    i = y
    while i < n-1: 
        i += 1
        if arr[x][i] == 'X': 
            break
        points.append((x,i)) 

    return points



def minimum_moves(grid, start_x, start_y, goal_x, goal_y):
    n = len(grid)
    dist = [n * [float("inf")] for _ in range(n)]
    dist[start_x][start_y] = 0
    queue = deque([(start_x, start_y)])
    while queue:
        # print(queue)
        x0, y0 = queue.popleft()
        d = dist[x0][y0]
        if x0 == goal_x and y0 == goal_y:           
            break
        points = near_point(grid, x0, y0)

        for p in points:
            x, y = p
            if dist[x][y] == float("inf"):
                dist[x][y] = d + 1
                queue.append((x, y))
    return d



if __name__ == '__main__':

    # n = int(input())
    # grid = []
    # for _ in range(n):
    #     grid_item = input()
    #     grid.append(grid_item)

    # start_end = input().split()

    # start_x = int(start_end[0])

    # start_y = int(start_end[1])

    # goal_x = int(start_end[2])

    # goal_y = int(start_end[3])
    grid = ['...', '.X.', '...']
    start_x = 0
    start_y = 0
    goal_x = 1
    goal_y = 2

    result = minimum_moves(grid, start_x, start_y, goal_x, goal_y)
    print(result)
