# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:31:23 2019

@author: 29132
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:15:09 2019

@author: 29132
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 00:07:40 2019

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
def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)

def insertNodeAtPosition(head, data, position):
    if position==0:
        p=head
        head=SinglyLinkedListNode(data)
        head.next=p
        return head
    p=head
    count=1
    while(count!=position) and p.next:
        count+=1
        p=p.next
    if count==position and p.next!=None:
        q=p.next
        p.next=SinglyLinkedListNode(data)
        p.next.next=q
    elif count==position and p.next==None:
        p.next=SinglyLinkedListNode(data)
    return head
        
fptr=open('test.txt','w')
llist_count = int(input())
llist = SinglyLinkedList()
for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)
data = int(input())
position = int(input())
llist_head = insertNodeAtPosition(llist.head, data, position)
print_singly_linked_list(llist_head, ' ', fptr)
fptr.write('\n')
fptr.close()
