""" 
A Stack data structure implementation in Python.
@Author Michael Le - https://youtube.com/michaelworkspace
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
#        if len(self.items) == 0:
#            return True
        return not self.items

    def get_size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    stack.push(1)
    stack.push(2)
    print(stack)
    print(stack.get_size())
    print(stack.pop())
    print(stack)
    stack.push(3)
    print(stack)
    print(stack.peek())
