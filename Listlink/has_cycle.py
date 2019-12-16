# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:59:25 2019

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


def has_cycle(head):
    if head is None:
        return 0
    p = head
    q = head.next
    while q:
        if q == p:
            return 1
        else:
            q = q.next
            if not q:
                return 0
            else:
                q = q.next
                p = p.next
    return 0


if __name__ == '__main__':
    fptr = open('text.txt', 'w')
    tests = int(input())
    for tests_itr in range(tests):
        index = int(input())
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        extra = SinglyLinkedListNode(-1);
        temp = llist.head;
        for i in range(llist_count):
            if i == index:
                extra = temp
            if i != llist_count - 1:
                temp = temp.next
            temp.next = extra
        result = has_cycle(llist.head)
        fptr.write(str(int(result)) + '\n')
        fptr.write('\n')
    fptr.close()
