import time
from math import factorial
def get_the_fastest_func(funcs, arg = None):
    res= {}
    for i in funcs:
        start_time = time.perf_counter()

        i(arg)

        end_time = time.perf_counter()
        result_time = end_time - start_time
        res[result_time] = i
        
        
    return res[min(res)]

def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable)  


funcs = [for_and_append, list_comprehension, list_function]

print(get_the_fastest_func(funcs, range(100_000)))