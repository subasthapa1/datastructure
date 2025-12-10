"""
Implementing queue. In queue, first in will be out first. The order is FIFO(First-In-First-Out)

"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isempty():
            print("Nothing to remove. Please first add some elements before removing them.")
        else:
            self.queue.pop(0)

    def peek(self):
        if self.isempty():
            print("Nothing to show. Please first add some elements before displaying them.")
        else:
            self.queue.pop(0)

    def isempty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.queue == 0:
            print("No element in Queue")
        return self.queue[0]
    def size(self):
        return len(self.queue)


# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("Is the Queue Empty? ", myQueue.isempty())
print("Size of a Queue: ", myQueue.size())