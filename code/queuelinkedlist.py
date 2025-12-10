class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            print("Queue is empty!")
        if self.front is None:
            self.rear = None
            print("Can't perform deletion in a queue. No elements is a queue.")
            return
        temp = self.front
        self.front = temp.next
        self.length -= 1
        return temp.value

    def peek(self):
        if self.front is None:
            return "Queue is empty. Nothing to display."
        return self.front.value

    def printallnodesinaqueue(self):
        temp = self.front
        while temp:
            print(temp.value, "->")
            temp = temp.next

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
print(myQueue.peek())
myQueue.enqueue('B')
print(myQueue.peek())
myQueue.enqueue('C')
myQueue.dequeue()
print(myQueue.peek())
myQueue.printallnodesinaqueue()
