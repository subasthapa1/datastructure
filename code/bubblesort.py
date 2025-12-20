class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def performsort(self):
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.arr

arr = [4,2,6,3,5,9,8,7,1,10,15]
ob1 = BubbleSort(arr)
print(ob1.performsort())