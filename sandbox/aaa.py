def aaa(a,b, c):
    return a + b + c

def bbb( a, b, c):
    return a - b - c    

def ccc(func, a , b, c ):

    return func(a, b, c)


print(aaa(1,2,3))

print(bbb(1,2,3))

print(ccc(aaa, 4,2,1))





