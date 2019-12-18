"""
Created on :  11:31 AM
Author : Xue Zhang
"""
from collections import deque


class Node:
    """tree node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    """binary tree"""

    def __init__(self):
        self.root = Node(1)
        self.result = []

    def add(self, value):
        left, right = value
        node_left = Node(left) if left != -1 else None
        node_right = Node(right) if right != -1 else None
        q = deque()
        while q:
            cur_node = q.popleft()
            if cur_node:
                cur_node.left = node_left
                cur_node.right = node_right
            q.append(node_left)
            q.append(node_right)

def in_order(node, ret):
    if node is None:
        return
    in_order(node.left, ret)
    ret += [node.data]
    in_order(node.right, ret)


def swap_every_k_unit(node, level, k):
    if node is None or (node.left is None and node.right is None):
        return
    if level % k == 0:
        # print(level)
        node.left, node.right = node.right, node.left
    swap_every_k_unit(node.left, level + 1, k)
    swap_every_k_unit(node.right, level + 1, k)


def swap_nodes(indexes, queries):
    t = Tree()
    q = deque()
    q += [t.root]
    for index in indexes:
        left, right = index
        node_left = Node(left) if left != -1 else None
        node_right = Node(right) if right != -1 else None
        cur_node = q.popleft()
        cur_node.left = node_left
        cur_node.right = node_right
        if node_left:
            q.append(node_left)
        if node_right:
            q.append(node_right)
    ans = []
    in_order(t.root, ans)
    print(ans)
    results = []
    for k in queries:
        ans = []
        swap_every_k_unit(t.root, 1, k)
        in_order(t.root, ans)
        results.append(ans)
    return results



if __name__ == '__main__':
    n = int(input())
    values = []
    for _ in range(n):
        values.append(list(map(int, input().rstrip().split())))
    queries_count = int(input())
    q1 = []
    for _ in range(queries_count):
        queries_item = int(input())
        q1.append(queries_item)
    result = swap_nodes(values, q1)
    print(result)
    print('\n'.join([' '.join(map(str, x)) for x in result]))
