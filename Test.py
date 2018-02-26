import random
for i in range (10):
    name = 'Luxury'
    char = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    char2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    code = ('{0}-{1}{2}{3:04}'.format( name,char,char2,i))
    print (code)
