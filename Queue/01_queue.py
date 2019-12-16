"""
Created on :  2:35 PM
Author : Xue Zhang
"""


class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def is_empty(self):
        return not self.__items

    def size(self):
        return len(self.__items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.is_empty())
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)



