import random
numList = []
for i in range(20):
    numList.append(random.randint(1,100))
print('Day ngau nhien la',numList)
for i in range(1,len(numList)):
    j = i
    while j > 0:
        if numList[j-1] > numList[j]:
            temp = numList[j - 1]
            numList[j - 1] = numList[j]
            numList[j] =temp
        j -= 1
print('Day da duoc sap xep',numList)