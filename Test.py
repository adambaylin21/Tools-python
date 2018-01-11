import random
numList = []
for i in range(100):
    numList.append(random.randint(1,1000))

print(numList)
for i in range(1,len(numList)):
    j = i
    while j > 0:
        if numList[j] < numList[j - 1]:
            temp = numList[j-1]
            numList[j-1] = numList[j]
            numList[j] = temp
        j -= 1
print(numList)