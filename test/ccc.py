rows, columns = [int(i) for i in input().split()]
mtrx =[[0]*columns for _ in range(rows)]
value = 0
current_row = 0
current_column = 0
change_row = 0
change_column = 1
steps = columns
turn = 0
while value < rows*columns:
    mtrx[current_row][current_column] = value + 1
    value +=1
    steps -= 1
    if steps == 0:
        steps = rows*((turn +1)%2) + columns*(turn%2) - 1 - turn//2
        change_column, change_row = -change_row, change_column
        turn+=1
    current_row += change_row
    current_column += change_column


for i in range(rows):
    for j in range(columns):
        print(str(mtrx[i][j]).ljust(2), end = ' ')
    print()