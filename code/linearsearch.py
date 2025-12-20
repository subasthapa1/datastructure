"""
Perform linear search operation in a list.
"""

import time
class LinearSearch:
    def __init__(self, arr, element):
        self.arr = arr
        self.elementtosearch = element

    def perform_linear_search(self):
        for i in range(int(len(self.arr))):
            if self.arr[i] == self.elementtosearch:
                return f"Element found at index {i}"
        return f"Element,{self.elementtosearch} not found. Please enter another number."

arr = [3,2,6,9,4,5,8,7,12,10,1]
ob1 = LinearSearch(arr, 4)
print(ob1.perform_linear_search())
