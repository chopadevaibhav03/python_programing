# Write a Python function to multiply all the numbers in a list.
def multiply_list(*list):
    mul = 1
    for i in list:
        mul *= i
    return mul


print(multiply_list(8, 2, 3, -1, 7)) // -336
