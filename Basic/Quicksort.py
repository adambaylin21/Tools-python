import random
nList = []
for i in range(1000):
    nList.append(random.randint(1,1000))
print (nList)
def sosanh(list,left,right):
    x = list[left]
    i = left + 1
    j = right
    xtop = False
    while not xtop:
        while list[i] <= x and i <= j:
            i += 1
        while list[j] >= x and j >= i:
            j -= 1
        if j < i:
            xtop = True
        else:
            list[i],list[j] = list[j],list[i]
    list[left],list[j] = list [j],list[left]
    return j
    
def quicksort(list,left,right):
    if left < right:
        z = sosanh(list, left, right)
        quicksort(list,left,z-1)
        quicksort(list,z+1,right)

try:
    quicksort(nList,0,len(nList)-1)
except :
    pass
print(nList)