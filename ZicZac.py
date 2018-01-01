soduong = int(input('Nhap so duong \n'))
sodiem = int(input('Nhap so diem \n'))
j= 0
i = 0
for i in range(0, i <= soduong):
    for j in range(0, j <= sodiem):
        k = j % (2*soduong)
        a = ' '
        if k == i or k == 2*soduong -i:
            a = '*'
        print (a)
    print ()