def fibonaci(x: int):
    if x < 2:
        return 1
    else:
        return fibonaci(x-1) + fibonaci(x-2)
    print(fibonaci)
def tinhn (y):
    for i in range(y):
        print(fibonaci(i), end=' ')

def fib(x: int):
    a, b = 0,1
    while a < x :
        print (a, end =' ')
        a,b = b ,a + b
fib (100000000)
print ()
tinhn (10)



