def add_two_lists(a, b):
    c = []
    for n, m in zip(a, b):
        c.append(n + m)
    return c
 
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = add_two_lists(list1, list2)
 
print(list1)
print(list2)
print(list3)