"""
This python consists of list and dictionary comprehension practice code.

"""

# List comprehension
n = int(input("Enter the upper limit of number you would like to print for"))
list_odd = [x for x in range(n) if x%2==0] # Creating a list of even numbers
new_list = [x**2 for x in list_odd]
print("New list using list comprehension", new_list)

# Dictionary comprehension
lst = [x for x in range(n)]
square_list = [x**2 for x in range(n)]
dict_square = {k:v for (k,v) in zip(lst, square_list)}
print(dict_square)

new_dict = {x:x**2 for x in range(n) if x%2==0}
print("New dictionary:", new_dict)
