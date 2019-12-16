"""
Created on :  11:39 PM
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


def lca(root, v1, v2):
    v1_path = []
    v2_path = []

    def pre_order(node, search, path, flag):
        nonlocal v1_path
        nonlocal v2_path
        if node is None:
            return
        if node.info == search:
            path.append(node)
            if flag:
                v1_path = path
            else:
                v2_path = path
        elif search < node.info:
            pre_order(node.left, search, path + [node], flag)
        else:
            pre_order(node.right, search, path + [node], flag)

    pre_order(root, v1, [], 1)
    pre_order(root, v2, [], 0)
    print(v1_path)
    print(v2_path)
    path_len = min(len(v1_path), len(v2_path))
    j = 0
    result = root
    while result and j < path_len:
        if v1_path[j] == v2_path[j]:
            result = v1_path[j]
            j += 1
        else:
            break
    return result


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.create(arr[i])
    v = list(map(int, input().split()))
    ans = lca(tree.root, v[0], v[1])
    print(ans.info)
