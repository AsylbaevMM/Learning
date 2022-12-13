from datetime import date
result = [0 for i in range(7)]
start = date(1, 1 , 13 )
stop = date(9999, 12, 13)

while start <= stop:
    try:
        result[start.weekday()] += 1
        if start.month < 12:
            start = start.replace(month=start.month+1)
        else:
            start = start.replace(year = start.year+1, month= 1)
    except:
        break
    
print(*result, sep = '\n')




