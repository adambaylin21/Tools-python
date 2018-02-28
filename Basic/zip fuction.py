x = [9, 2, 3, 2, 1, 2]
y = [4, 5, 6, 7, 12, 15]
new = []
ziped = zip (x,y)
for i in ziped:
    if (sum(i)) <= 10:
        new.append(i)
print (new)