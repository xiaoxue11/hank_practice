# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:48:41 2019

@author: 29132
"""
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)
            
def insertNodeAtHead(head, data):
    if head==None:
        return SinglyLinkedListNode(data)
    p=head
    head=SinglyLinkedListNode(data)
    head.next=p
    return head
    
    
fptr=open('test.txt','w')
llist_count = int(input())
llist = SinglyLinkedList()
for i in range(llist_count):
    llist_item = int(input())
    llist_head=insertNodeAtHead(llist.head, llist_item)
    llist.head=llist_head
print_singly_linked_list(llist.head, '\n', fptr)
fptr.write('\n')
fptr.close()

