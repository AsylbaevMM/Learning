



def fib_gen():
    num1 = 0
    num2 = 1  
    while True:
        yield num1
        num1, num2 = num2, num1 + num2
        
fibonacci = fib_gen()

for i in range(30):
    print(next(fibonacci))
