class MyQueue(object):
    def __init__(self):
        self.__items = []
    
    def peek(self):
        return self.__items[0]
        
    def pop(self):
        return self.__items.pop(0)
        
    def put(self, value):
        self.__items.append(value)
        

if __name__ == '__main__':
    queue = MyQueue()
    t = int(input())
    for line in range(t):
        values = map(int, input().split())
        values = list(values)
        print(values)
        if values[0] == 1:
            queue.put(values[1])        
        elif values[0] == 2:
            queue.pop()
        else:
            # print(queue)
            print(queue.peek())