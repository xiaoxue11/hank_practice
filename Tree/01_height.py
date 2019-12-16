"""
Created on :  10:53 PM
Author : Xue Zhang
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height1(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return max(left, right) + 1


def height(root):
    if root is None:
        return 0
    q = [root]
    length = 0
    while q:
        temp = []
        for node in q:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        q = temp
        length += 1
    return length - 1


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.create(arr[i])
    print(height(tree.root))
