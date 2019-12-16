"""
Created on :  3:16 PM
Author : Xue Zhang
"""
from collections import deque, Counter


def construct_graph(graph_nodes, graph_from, graph_to):
    graph = {}
    for node in range(1, graph_nodes + 1):
        graph[node] = []
    for j in range(len(graph_from)):
        start = graph_from[j]
        end = graph_to[j]
        graph[start].append(end)
        graph[end].append(start)
    return graph


def bfs_graph(start, end, graph):
    q = deque()
    visited = []
    q.append((start, 0))
    while q:
        node, step = q.popleft()
        if node == end:
            return step
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                q.append((neighbor, step+1))
                visited.append(neighbor)
    return -1


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    d = Counter(ids)
    if d[val] < 2:
        return -1
    graph = construct_graph(graph_nodes, graph_from, graph_to)
    color_nodes = [k + 1 for k, v in enumerate(ids) if v == val]
    n = len(color_nodes)
    steps = []
    for j in range(n):
        for k in range(j+1, n):
            step = bfs_graph(color_nodes[j], color_nodes[k], graph)
            if step != -1:
                steps.append(step)
    return min(steps) if steps else -1


if __name__ == '__main__':
    nodes, edges = map(int, input().split())

    graph_start = [0] * edges

    graph_end = [0] * edges

    for i in range(edges):
        graph_start[i], graph_end[i] = map(int, input().split())

    colors = list(map(int, input().rstrip().split()))

    col = int(input())

    ans = findShortest(nodes, graph_start, graph_end, colors, col)

    print(ans)