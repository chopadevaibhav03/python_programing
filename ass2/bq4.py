str = input("Enter a sentence : ")
dict = {}
words = str.split()
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(dict)
