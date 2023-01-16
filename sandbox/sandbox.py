

def is_lucky_ticket(arg):
    if ' ' in arg:
        arg = arg.split()[-1]
    middle = len(arg)//2
    return sum([int(i) for i in arg[:middle]]) == sum([int(i) for i in arg[-middle:]])


print(is_lucky_ticket('A/5 21171'))