# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:37:14 2019

@author: 29132
"""

#!/bin/python3
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
def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')
            
def reversePrint(head):
    if head==None:
        return 
    pre=None
    cur=head
    while cur.next:
        p=cur.next
        cur.next=pre
        pre=cur
        cur=p
    cur.next=pre
    head=cur
    p=head
    while p:
        print(p.data)
        p=p.next
        
tests = int(input())
for tests_itr in range(tests):
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    reversePrint(llist.head)
