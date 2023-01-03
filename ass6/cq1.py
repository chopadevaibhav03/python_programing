"""
1. Create an inner function to calculate the addition in the following way 
• Create an outer function that will accept two parameters a and b 
• Create an inner function inside an outer function that will calculate the addition of a and b. 
• At last, an outer function will add 5 into addition and return it.
"""


def add5(num): return num + 5


def outer_func(a, b):
    def add(a, b): return a + b
    return add5(add(a, b))


print(outer_func(5, 10))
