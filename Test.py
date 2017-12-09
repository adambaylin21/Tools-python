clrender = ['#fcfcfc','#ffe9ba','#ffb2c4','#d6d7d9','#8cb4e8']
renderhex = ''
for i in clrender:
    css = '<div class="tn4" style="background-color: %s "></div>' % (i)
    renderhex = renderhex + css
print (renderhex)

html = """Ahihi"""
post = open(u'output.html','w')
print (html)
post.write(html)