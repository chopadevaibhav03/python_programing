# create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
# adding items in a specific index
tuplex = tuplex[:3] + (15, 20, 25) + tuplex[-3:]
print(tuplex)
