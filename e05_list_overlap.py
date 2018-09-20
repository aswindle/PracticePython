import random
a_size = random.randint(0,10)
b_size = random.randint(0,10)
a = []
b = []
overlap = []
for x in range(0, a_size):
    a.append(random.randint(0,20))
for x in range(0, b_size):
    b.append(random.randint(0,20))
print(a)
print(b)
if a_size <= b_size:
    for i in range(0, a_size):
        if (a[i] in b) and (a[i] not in overlap):
            overlap.append(a[i])
else:
    for j in range(0, b_size):
        if (b[j] in a) and (b[j] not in overlap):
            overlap.append(b[j])
print(overlap)