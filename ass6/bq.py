# Write a generator function that reverses a given string.
def str_rev(string):
    index = len(string)
    rev = ''
    while index > 0:
        rev += string[index - 1]
        index -= 1
    return rev


def str_srev(string):
    return string[::-1]


print(str_rev('Shoeb'))
print(str_srev('Shoeb'))
