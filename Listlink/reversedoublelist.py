# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:53:36 2019

@author: 29132
"""

#!/bin/python3
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)
def reverse(head):
    if not (head or head.next):
        return head
    cur=head
    pre=None
    while cur.next:
        p=cur.next
        cur.next=pre
        cur.prev=p
        pre=cur
        cur=p
    cur.prev=None
    cur.next=pre
    return cur
        
        
    
    


