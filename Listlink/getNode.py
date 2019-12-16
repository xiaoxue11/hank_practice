# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 23:31:22 2019

@author: 29132
"""


# !/bin/python3
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


def getNode(head, position_from_tail):
    if not head:
        return head
    p = head
    l = 0
    while p:
        l += 1
        p = p.next
    pos = l - position_from_tail - 1
    p = head
    k = 0
    while p and k != pos:
        p = p.next
        k += 1
    return p.data


if __name__ == '__main__':
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        position = int(input())
        result = getNode(llist.head, position)
    print(result)
