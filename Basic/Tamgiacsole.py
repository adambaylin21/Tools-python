while True:
    a = int(input('Hay nhap so le \n'))
    if a % 2 != 0:
        break
space = ('')
while a >= 1:
    i = 1
    while i <= a:
        print (a,end='')
        i += 1
    print ()
    space += (' ')
    print (space,end='')
    a -= 2
