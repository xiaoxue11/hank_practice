"""
Created on :  9:42 AM
Author : Xue Zhang
"""
from collections import deque, defaultdict


class Graph1:
    def __init__(self, nodes):
        self.graph = {}
        for k in range(nodes):
            self.graph[k] = []

    def connect(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def bfs_graph(self, start, end):
        visited = []
        q = deque()
        q.append((start, 0))
        while q:
            start, step = q.popleft()
            if start == end:
                return step
            neighbors = self.graph[start]
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append((neighbor, step+6))
                    visited.append(neighbor)
        return -1

    def find_all_distances(self, start):
        result = []
        nodes = [k for k in self.graph if k != start]
        for node in nodes:
            result.append(self.bfs_graph(start, node))
        print(" ".join(str(val) for val in result))


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.g = defaultdict(list)
        self.w = 6

    def connect(self, start, end):
        self.g[start].append(end)
        self.g[end].append(start)

    def find_all_distances(self, start):
        dist = [-1 for _ in range(self.nodes)]
        visited = []
        dist[start] = 0
        visited.append(start)
        q = deque()
        q.append(start)
        while q:
            current = q.popleft()
            for node in self.g[current]:
                if node not in visited:
                    dist[node] = dist[current] + self.w
                    q.append(node)
                    visited.append(node)
        del dist[start]
        print(*dist)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)
        for j in range(m):
            x, y = [int(x) for x in input().split()]
            graph.connect(x - 1, y - 1)
        print(graph.g)
        s = int(input())
        graph.find_all_distances(s - 1)
