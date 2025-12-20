import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str_(self):
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq.is_empty())
    pq.put("Eat", 2)
    pq.put("Sleep", 3)
    pq.put("Drink", 1)
    pq.put("Walk", 4)

    print("-------------After putting element into priority queue----------")
    print(pq.is_empty())
    print(pq.get())
    print(pq.__str__())
    print(pq.elements)
