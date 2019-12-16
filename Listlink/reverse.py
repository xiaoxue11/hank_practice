# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:36:33 2019
@author: 29132
"""


class SinglyLinkedListNode:
    """create single link list"""
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

def reverse(head):
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
    return head
    
fptr = open('text', 'w')
tests = int(input())
for tests_itr in range(tests):
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
        llist1 = reverse(llist.head)
    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')
fptr.close()
