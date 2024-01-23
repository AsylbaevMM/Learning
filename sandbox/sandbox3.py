

from datetime import date

iters = int(input())
for i in range(iters):  
    try:
        obj = date(*[int(i) for i in input().split()[::-1]])
        print('YES')
    except:
        print('NO')
