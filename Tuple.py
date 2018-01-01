numList = [9, 3, 2, 5, 6, 8, 11]
t1 = []
t2 = []
for num in numList:
    if num <= 5:
        t1.append(num)
    if num > 5:
        t2.append(num)
def mimax(x):
    t3 = []
    for i in range(0,len(x)):
        t3.append(min(x))
        x.remove(min(x))
    return (t3)
t3 = mimax(t1)
t4 = mimax(t2)
resurl = (t3,t4)
print (resurl)