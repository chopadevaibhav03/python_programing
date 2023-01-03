# Python program to convert a tuple to a string.
tuplex = ('S', 'h', 'o', 'e', 'b')

# By Looping the tuple
str = ''
for char in tuplex:
    str = str + char
print(str)

# By using str.join() method
print(''.join(tuplex))
