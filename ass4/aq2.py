# Write a python program to remove and return an arbitrary set element.Raise KeyErrorif the set is empty
sets = set()
sets.update({1, 2, 3, 4})
print(sets)
el_to_remove = int(input('Enter an element to remove: '))
sets.remove(el_to_remove)
print(sets)
