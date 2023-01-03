sets = set()
sets.update({1, 2, 3, 4})
print(sets)

operator = input(
    "To add element to set input '+' to remove element from set input '-' : ")
if operator == '+':
    el = int(input('Enter element to add : '))
    sets.add(el)
elif operator == '-':
    el = int(input('Enter element to remove : '))
    sets.discard(el)
else:
    print('Invalid operator')

print(sets)
