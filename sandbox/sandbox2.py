

moments = int(input())
errors = [int(i) for i in input().split()]
periods = int(input())
for _ in range(periods):
    start, stop =[int(i) for i in input().split()]
    start -= 1
    result = "Yes"
    if len(errors[start:stop]) == 1:
        result = 'Yes'
    else:
        largest = max(errors[start:stop])
        smallest = min(errors[start:stop])
        for i in range(errors.index(largest), stop-1):
            if errors[i] < errors[i+1]:
                result = "No"
    print(result)