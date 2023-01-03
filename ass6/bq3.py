# Write a recursive function to calculate the sum of numbers from 0 to 10.

def sum_of_range(n):
    if n <= 0:
        return n
    else:
        return n + sum_of_range(n-1)


print(sum_of_range(10))
