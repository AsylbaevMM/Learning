



def squareList(num):
    while num > 0:
        yield num**2
        num -= 1

square = squareList(10)

for i in range(11):
    print(next(square))