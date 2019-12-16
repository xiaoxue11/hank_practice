# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:42:33 2019

@author: 29132
"""
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
def sortedInsert(head, data):
    newnode=DoublyLinkedListNode(data)
    if not head:
        return newnode
    if head.data>data:
        p1=head
        head=newnode
        newnode.next=p1
        p1.prev=head
        return head
    p=head    
    while p.next:
        if p.data>=data:
            p1=p.prev
            p1.next=newnode
            newnode.pre=p1
            newnode.next=p
            p.prev=newnode
            return head
        else:
            p=p.next
    if p.data>=data:
            p1=p.prev
            p1.next=newnode
            newnode.pre=p1
            newnode.next=p
            p.prev=newnode
            return head
    else:
        p.next=newnode
        newnode.prev=p
        return head

    
            
            