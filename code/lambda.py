"""
Lambda function defined without a name using lambda keyword.
Syntax lambda arguments : expression

"""
num = int(input("Enter a number"))
func = lambda x:x**2
print(func(num))

odd_even = lambda x : "Even" if x%2 == 0 else "Odd"
print(odd_even(num))

my_list = [1, 2, 3, 4, 5]
new_list = list(filter(lambda x: x % 2 != 0, my_list))
print(new_list)