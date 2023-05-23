from sys import stdin
import functools as ftl
n = int(input())
rates = []
for i in range(n):
    rates.append(int(input()))
min_rate = min(rates)
max_rate = max(rates)

bonuses = [500 for i in range(n)]

@ftl.lru_cache
def check(index, rates, bonuses):
    if index == 0 and ():
        if rates[0] > rates[1] and bonuses[0] <= bonuses[1]:
            return bonuses[1]+500

    elif index < len(rates)-1:
        if rates[index] > rates[index+1] and bonuses[index] <= bonuses[index+1]:
            return bonuses[index+1]+500
        elif rates[index] > rates[index-1] and bonuses[index] <= bonuses[index-1]:
            return bonuses[index-1]+500
        else:
            return bonuses[index]
    else:
        if rates[-1] > rates[-2] and bonuses[-1]<= bonuses[-2]:
            return bonuses[-2] +500
    return bonuses[index]

for i in range(min_rate, max_rate+1):
    for j in range(n):
        bonuses[j] = check(j, rates, bonuses) 


print(sum(bonuses))