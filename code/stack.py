""""
Implementation of stack.
push: Push element to the stack
pop: Remove item from the stack
peek: Return first item from the stack
Check if stack is empty or not.

"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isempty():
            print("No items in a stack. Can\'t perform pop. Please add items in it.")
        else:
            self.stack.pop()
            print("Successfully removed item from the stack.")

    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self):
        if self.isempty():
            print("Stack is empty. No items in it.")
        else:
            topitem = self.stack[-1]
            return f"Now new item on top is: {topitem}"

    def size(self):
        return len(self.stack)


myStack = Stack()
myStack.push("S")
print(myStack.stack)
myStack.push("U")
print(myStack.stack)
myStack.push("R")
print(myStack.stack)
myStack.push("Y")
print(myStack.stack)
myStack.push("A")
print(myStack.stack)
myStack.push("N")

myStack.pop()
myStack.push("D")
print(myStack.size())

print(myStack.peek())

print(myStack.stack)
print(myStack.size())