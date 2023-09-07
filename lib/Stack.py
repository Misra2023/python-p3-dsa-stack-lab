class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek at an empty stack.")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.is_empty()

    def search(self, value):
        if value in self.stack:
            return self.stack.index(value)
        else:
            return -1

    def full(self):
        # Assuming the stack is unbounded (no predefined limit)
        return False
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # Output: 3
print(stack.size())  # Output: 3

stack.pop()

print(stack.search(2))  # Output: 0 (0-based index)
print(stack.is_empty())  # Output: False
print(stack.full())  # Output: False

