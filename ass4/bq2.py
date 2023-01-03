set_a = set()
set_b = set()
set_a.update({1, 2, 3, 4})
set_a.update([4, 5, 6])
print(set_a | set_b)  # Union is performed using | operator.
print(set_a.union(set_b))
