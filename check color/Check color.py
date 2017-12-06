# -*- coding: utf8 -*-

reader=open('color.txt','r')
word=reader.read()
keyw = ['title="Heliconia"']

for i in word.split():
    for j in keyw:
        if i == j:
            print('Done')





