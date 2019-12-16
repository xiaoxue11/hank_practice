# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 00:07:40 2019

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


def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    p = head
    count = 1
    while count != position and p.next.next:
        count += 1
        p = p.next
    if count == position and p.next.next:
        p.next = p.next.next
    elif count == position and p.next.next is None:
        p.next = None
    return head


if __name__ == '__main__':
    fptr = open('test.txt', 'w')
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    pos = int(input())
    llist_head = delete_node(llist.head, pos)
    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')
    fptr.close()
