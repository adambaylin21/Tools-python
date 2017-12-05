# -*- coding: utf8 -*-

color = ['','#464646','#fff','#123654']
choise = ['Den','Trang','Linh tinh']

stt = 1
for i in choise:
    print (str(i),'- %d' %(stt))
    stt += 1

choised = []
choised = input ('Hãy nhập dãy màu bạn chọn? \n')

rendercl = []
for i in choised:
    try:
        if int(i):
            rendercl.append(color[int(i)])
    except TypeError:
        pass
    except ValueError:
        pass
    except IndexError:
        pass

print (rendercl)




