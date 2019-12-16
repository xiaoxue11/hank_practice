# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:30:55 2019

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


def find_merge_node(head1, head2):
    p1 = head1
    p2 = head2
    while p1 != p2:
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next
        if p1 != p2:
            if p1 is None:
                p1 = head2
            if p2 is None:
                p2 = head1
    return p1.data


fptr = open('text.txt', 'w')
tests = int(input())
for tests_itr in range(tests):
    index = int(input())
    llist1_count = int(input())
    llist1 = SinglyLinkedList()
    for _ in range(llist1_count):
        llist1_item = int(input())
        llist1.insert_node(llist1_item)
    llist2_count = int(input())
    llist2 = SinglyLinkedList()
    for _ in range(llist2_count):
        llist2_item = int(input())
        llist2.insert_node(llist2_item)
    ptr1 = llist1.head;
    ptr2 = llist2.head;
    for i in range(llist1_count):
        if i < index:
            ptr1 = ptr1.next
    for i in range(llist2_count):
        if i != llist2_count - 1:
            ptr2 = ptr2.next
    ptr2.next = ptr1
    result = findMergeNode(llist1.head, llist2.head)
    fptr.write(str(result) + '\n')
fptr.close()
