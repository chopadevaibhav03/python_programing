l = []
l2 = []
# iterating till the range
for i in range(0, 6):
    l.append(int(input('Enter digit :')))  # adding the element

for i in l:
    if(i not in l2):
        l2.append(i)
    else:
        print("DUPLICATES")
        exit()
