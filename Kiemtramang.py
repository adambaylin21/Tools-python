a = []
b = []
i = 0
while i <= 100:
    if i % 3 == 0:
        a.append(i)
    if i % 5 == 0:
        b.append(i)
    i += 1
print(a)
print(b)