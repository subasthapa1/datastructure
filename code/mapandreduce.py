"""
    Map function applies a given function to each element of an iterable (list, tuple, set, etc.)
            and returns a map object (iterator) syntax map(function, iterable,..)
    Filter ilter() function is used to extract elements from an iterable (like a list, tuple or set)
           that satisfy a given condition. Syntax filter(function, iterable)
    Reduce
"""

# Filter
def return_only_even(a):
    return a % 2 == 0

a= range(0,20)

even_list = filter(return_only_even, a)

print(list(even_list))


# Map function
even_list_new = map(return_only_even, a)
print(list(even_list_new))

fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res))
