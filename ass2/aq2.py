str = input('Enter a string : ')
dict = {}
for c in str:
    keys = dict.keys()
    if c in keys:
        dict[c] += 1
    else:
        dict[c] = 1

print(dict)
