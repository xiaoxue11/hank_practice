"""
Created on :  11:31 AM
Author : Xue Zhang
"""
import copy


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
        node = Node(value)
        q = [self.root]
        while q:
            cur_node = q.pop(0)
            if cur_node.data != -1:
                if cur_node.left is None:
                    cur_node.left = node
                    return
                else:
                    q.append(cur_node.left)
                if cur_node.right is None:
                    cur_node.right = node
                    return
                else:
                    q.append(cur_node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        if node.data != -1:
            print(node.data, end=' ')
        self.in_order(node.right)


def swap_every_k_unit(node, level, k):
    if node is None or (node.left.data == -1 and node.right.data == -1):
        return
    if (level + 1) % k == 0:
        # print(level)
        node.left, node.right = node.right, node.left
    swap_every_k_unit(node.left, level + 1, k)
    swap_every_k_unit(node.right, level + 1, k)


def swap_nodes(indexes, queries):
    new_values = [i for j in indexes for i in j]
    t = Tree()
    for i in new_values:
        t.add(i)
    t.in_order(t.root)
    for k in queries:
        swap_every_k_unit(t.root, 1, k)
        t.in_order(t.root)
        print('')


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
    swap_nodes(values, q1)
    # print(result)
    # print('\n'.join([' '.join(map(str, x)) for x in result]))
