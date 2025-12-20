"""
Double end queue.Can be inserted or deleted from both sides.

"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue("A")
    print(q)
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    print(q.peek())

