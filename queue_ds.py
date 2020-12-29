""" 
A Queue data structure implemention in Python.
"""


from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items

    def inspect(self):
        return self.items[0]

    def get_size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue('hello')
    q.enqueue('world')
    print(q)
    print(q.get_size())
    q.dequeue()
    print(q)
    print(repr(q))
    print(q.get_size())
    print(q.is_empty())
    print(q.inspect())
