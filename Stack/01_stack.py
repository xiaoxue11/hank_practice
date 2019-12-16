"""
Created on :  11:08 AM
Author : Xue Zhang
"""


class Stack:

    def __init__(self):
        """custom define container"""
        self.__items = []

    def push(self, item):
        """add item in stack"""
        self.__items.append(item)

    def pop(self):
        """pop item in container"""
        return self.__items.pop()

    def peek(self):
        """get the top element"""
        if self.__items:
            return self.__items[-1]
        else:
            return None

    def is_empty(self):
        """judge whether the list is None"""
        return not self.__items

    def size(self):
        return len(self.__items)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
