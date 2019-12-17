"""
Created on :  11:03 PM
Author : Xue Zhang
"""


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


def decodeHuff(root, s):
    node = root
    result = []
    for char in s:
        if char == '1':
            node = node.right
        elif char == '0':
            node = node.left
        if node.right is None and node.left is None:
            result.append(node.data)
            node = root
    print(''.join(result))


if __name__ == '__main__':
    a = Node(5, 'q')
    b = Node(2, 'q')
    c = Node(3, 'A')
    d = Node(1, 'B')
    e = Node(1, 'C')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    s1 = "1001011"
    print(decodeHuff(a, s1))
