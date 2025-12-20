"""
Implementing binary search algorithm.
List passed to the function should be sorted.
Element to find in a list should be passed to the function.

"""
class BinarySearch:
    def __init__(self, arr, element):
        self.arr = arr
        self.elementtosearch = element
    def performbinarysearch(self):
        low_index = 0
        high_index = int(len(self.arr)) - 1

        while low_index <= high_index:
            mid = (low_index + high_index)//2
            if self.arr[mid] == self.elementtosearch:
                return f"element found at index {mid}"
            elif self.elementtosearch > self.arr[mid]:
                low_index = mid + 1

            else:
                high_index = mid - 1

        return f"Element not found in a list"


arr = [0,1,2,3,4,5,6,7,8,9,10]
ob1 = BinarySearch(arr, 10)
print(ob1.performbinarysearch())



