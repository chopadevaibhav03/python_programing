n = 10
t1 = 0
t2 = 1
nextTerm = t1+t2
i = 0
print(t1, t2, sep=", ", end=", ")
for i in range(2, n):
    print(nextTerm, end=", ")
    t1 = t2
    t2 = nextTerm
    nextTerm = t1+t2
