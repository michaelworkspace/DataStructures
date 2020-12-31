""" 
A Stack data structure implementation in Python.
@author: Michael Le
"""


class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def inspect(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items

    def __str__(self):
        return str(self.items)

    def get_size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    print(stack)
    stack.push('Apple')
    print(stack)
    stack.pop()
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.is_empty())
    stack.push(5)
    print(stack)
    print(stack.is_empty())
    stack.push(False)
    print(stack)
    print(stack.get_size())
    print(stack)
    print(stack.inspect())
    print(stack.pop())
    print(stack)
    stack.push(4)
    stack.push(True)
    print(stack)
