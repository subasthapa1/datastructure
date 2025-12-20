"""
Implementation of stack.
push: Push element to the stack
pop: Remove item from the stack
peek: Return first item from the stack
Check if stack is empty or not.

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("No items in a stack. Can\'t perform pop. Please add items in it.")
        else:
            self.items.pop()
            print("Successfully removed item from the stack.")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            print("Stack is empty. No items in it.")
        else:
            topitem = self.items[-1]
            return f"Now new item on top is: {topitem}"

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push("S")
    print(s.items)
    s.push("U")
    print(s.items)
    s.push("R")
    print(s.items)
    s.push("Y")
    print(s.items)
    s.push("A")
    print(s.items)
    s.push("N")

    s.pop()
    s.push("D")
    print(s.size())

    print(s.peek())

    print(s.items)
    print(s.size())
    print(s.__str__())
