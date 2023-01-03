str = input("Enter a string : ")
num_of_char = 0
num_of_digits = 0
for s in str:
    if s.isalpha():
        num_of_char += 1
    elif s.isdigit():
        num_of_digits += 1
print("Number of characters : ", num_of_char)
print("Number of digits : ", num_of_digits)
