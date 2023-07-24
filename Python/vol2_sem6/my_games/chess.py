from itertools import combinations_with_replacement
from functools import lru_cache
from random import sample

_QUEEN_COUNT = 5 # Если использовать больше 5 ферзей, очень сложно рандомом найти рабочую комбинацию

@lru_cache       # использовал кеширование для ускорения работы
def _check(positions):
    for i in range(len(positions)):
        row_1, col_1 = positions[i]
        for j in range(i+1, len(positions)):
            row_2, col_2 = positions[j]
            if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                return False
    return True


def check_positions():
    positions = []
    for i in range(1, 9):
        pos = []
        while not(len(pos) == 2 and all(j.isdigit() and 0<int(j)<9 for j in pos)):
            pos = input(f'Введите позицию {i}-го ферзя в формате "n m" >>> ').split()
        positions.append(tuple(int(n) for n in pos))
    return _check(tuple(positions))

def _random_positions():
    possible_positions = list(combinations_with_replacement(range(1, 9), 2))
    return sample(possible_positions, _QUEEN_COUNT)

def _print_field(positions):
    place = [['▢' for i in range(8)] for j in range(8)]
    for piece in positions:
        place[piece[0]-1][piece[1]-1] = '▣'
    for i in place:
        print(*i, sep = ' ', end = '\n')
    print()    

def four_possible():
    result = []
    while len(result) < 4:
        positions = _random_positions()
        if _check(tuple(positions)) and positions not in result:
           result.append(positions)    
           _print_field(positions)
    return result

  
        




if __name__ == "__main__":
    four_possible()
