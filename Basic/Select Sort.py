import random
numList = []
for i in range(20):
    numList.append(random.randint(1,100))
print(numList)
for i in range(len(numList)-1):
    i_min = i
    for j in range(i + 1, len(numList)):
        if numList[j] > numList[i_min]:
            i_min = j
        temp = numList[i]
        numList[i] = numList [i_min]
        numList[i_min] = temp
print(numList)