# import time
# def shffl(arg):
#     n = int(round(time.time()*1000) % len(arg))
#     for i in range(len(arg)):
#         arg[i], arg[i - n] = arg[i - n], arg[i]
#     return arg
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(lst)
# print(shffl(lst))



# lst = ['D21EQD3FRG', 'DFSE45RTYR6', 'AW324SF4D23C']

# print(True) if input() in ''.join(lst) else print(False)


# lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

# word = "asd"
# if lst.count(word) < 2:
#     print(-1)
# else:
#     lst[lst.index(word)] = word[1:]
# print(lst.index(word))

lst = [2, 3, 5, 9, 3]
# total = 0
# for i in range(len(lst)):
#     if i % 2 == 1:
#         total += lst[i]
# print(total)

print(sum(lst[1::2]))