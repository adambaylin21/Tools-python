# -*- coding: utf8 -*-

reader=open('color.txt','r')
word=reader.read()
clrender = []
namecl=['title="White"','title="Sand"','title="Light Pink"','title="Ash Grey"','title="Light Blue"','title="Azalea"','title="Sport Grey"','title="Daisy"','title="Lime"','title="Carolina Blue"','title="Heliconia"','title="Gold"','title="Orange"','title="Tennessee Orange"','title="Red"','title="Sapphire"','title="Electric Green"','title="Purple"','title="Royal"','title="Irish Green"','title="Dark Heather"','title="Maroon"','title="Navy"','title="Forest Green"','title="Black"']
hexcl =['#fcfcfc','#ffe9ba','#ffb2c4','#d6d7d9','#8cb4e8','#ff6dda','#999d9e','#f3fe2b','#79ff20','#5194bf','#8f1d59','#ffb502','#ff4902','#ff8400','#f30000','#0061c5','#00ac31','#490c95','#01298e','#008c35','#444545','#3b0018','#031037','#022d1b','#0b0b0b']

# for i in word.split():
#     for j in namecl:

j = 0
for i in (namecl):
    print (i,'%s' % hexcl[j] )
    j += 1






