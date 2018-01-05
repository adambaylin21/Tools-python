import random, string
chu = string.ascii_letters
gioih = random.randint(5,10)
renderc = []
for i in range(0,gioih):
    renderc.append(random.choice(chu))
print('Day chu ngau nhien la',renderc)
sor = sorted(renderc)
print ('Day duoc sap xep la',sor)
finnal = []
a = len(sor)
for so in sor:
    finnal.append(sor[a-1])
    a -= 1
print ('Dao nguoc day ta duoc',finnal)
