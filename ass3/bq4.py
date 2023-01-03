tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
l = []
# tuple.count(el) return the number of times element appears in the tuple.
for el in tuplex:
    if el not in l:
        l.append(el)
        repeated_times = tuplex.count(el)
        if repeated_times > 1:
            print(el, 'has repeated ', repeated_times, ' times')
