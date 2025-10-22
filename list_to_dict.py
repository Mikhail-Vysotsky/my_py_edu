en = ['one', 'two', 'three', 'four']
ru = ['один', 'два', 'три', 'четыре']
d = {}
d2 = {}

for i in range(len(en)):
    d[en[i]] = ru[i]

for e, r in zip(en, ru):
    d2[e] = r


print(d)
print(d2)