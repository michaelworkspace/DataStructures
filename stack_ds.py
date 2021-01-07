""" 
A Stack data structure implementation in Python.
@author Michael Le - https://youtube.com/michaelworkspace
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
#        if len(self.items) == 0:
#            return True
        return not self.items

    def get_size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    stack.push(1)
    stack.push('a')
    print(stack)
    print(stack.get_size())
    stack.pop()
    print(stack)
    stack.push(True)
    print(stack.peek())
    print(stack)
    print(stack.is_empty())
