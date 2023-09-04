


n, c, d = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

while c:
    # уменьшаем минимальное число, пока не станет меньше нуля
    while c and not [i for i in nums if i < 0]: 
        nums[nums.index(min(nums))] -= d
        c -= 1
    # увеличиваем минимальное положительное число, это в произведении с отрицательным даст наименшее возможное число
    if c:
        nums[nums.index(min([i for i in nums if i > 0]))] += d
        c -= 1
print(*nums)