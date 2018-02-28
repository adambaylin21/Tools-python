key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
codex = input('Hay nhap ky tu can ma hoa? \n')
coder = input ('Hay nhap ky can giai ma? \n')
def encoding(x,y):
    rendercode = ''
    for code in y:
        for ke in x:
            if code == ke:
                rendercode = rendercode + (x[ke])
        if code == ' ':
            rendercode = rendercode + (' ')
    return rendercode
key2 = key.values()
key3 = key.keys()
encoder = zip(key2,key3)
newcode = dict(encoder)
print('Ky tu da ma hoa la:',encoding(key,codex))
print('Ky tu duoc giai ma la:',encoding(newcode,coder))
