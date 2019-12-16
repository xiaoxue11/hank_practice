"""
Created on :  9:55 PM
Author : Xue Zhang
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    result = []

    def in_order(node):
        nonlocal result
        if node is None:
            return
        in_order(node.left)
        result.append(node.data)
        in_order(node.right)

    if root is None:
        return False
    in_order(root)
    n = len(result)
    for i in range(n):
        for j in range(i+1, n):
            if result[i] >= result[j]:
                return False
    return True


if __name__ == '__main__':
    a = Node(4)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(5)
    g = Node(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    print(checkBST(a))


