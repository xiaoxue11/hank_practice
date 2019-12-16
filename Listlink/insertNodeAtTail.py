# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:15:46 2019

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
def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)
def insertNodeAtTail(head, data):
    if head==None:
        head=SinglyLinkedListNode(data)
        return head
    p=head
    while p.next:
        p=p.next
    p.next=SinglyLinkedListNode(data)
    return head
fptr=open('test.txt','w')
llist_count = int(input())
llist = SinglyLinkedList()
for i in range(llist_count):
    llist_item = int(input())
    llist_head=insertNodeAtTail(llist.head, llist_item)
    llist.head=llist_head
print_singly_linked_list(llist.head, '\n', fptr)
fptr.write('\n')
fptr.close()

