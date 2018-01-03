soduong = int(input('Nhap so duong \n'))
sodiem = int(input('Nhap so diem \n'))
isPrinted = False
i = 0
j = 0
k = 1
while i < sodiem:
    j = 0
    while j < soduong*(sodiem - 1) + 1:
        k = 1
        while k <= soduong:
            if k % 2 !=0:
                if ((j+i) ==(sodiem -1)*k) or (j-i) == (sodiem-1)*k:
                    print('*',end='')
                    isPrinted = True
                    k = soduong + 1
            k +=1
        j+=1
        if not isPrinted:
            print(' ',end='')
        isPrinted = False
    print()
    i+=1
