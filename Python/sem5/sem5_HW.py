
def delete_abv():
    with open('with_abv.txt', 'r', encoding='UTF-8') as input_file:
        words = input_file.read().split()

    new_words = [i for i in words if 'абв' not in i.lower()]
    new_text = ' '.join(new_words)
    with open('without_abv.txt', 'w', encoding='UTF-8') as output_file:
        print(new_text, file=output_file)


def candy():
    from random import randint

    def again():        # Функция  для перезапуска игры
        restart = input(
            'Для перезапуска игры введите "1", для отмены введите "0" >>>')
        if restart == '1':
            candy()
        else:
            print('Спаибо за игру!')
            exit()

    def two_players():    # Игра для двух игроков
        player, second_player = input(
            "Имя первого игрока >>> "), input("Имя второго игрока >>> ")
        for i in range(randint(1, 10)):   # Жеребьевка, кто будет первый ходить
            player, second_player = second_player, player
        candy_count = 2021
        while candy_count > 0:    # Сам цикл игры
            num = input(
                f'На столе {candy_count} конфет. Ходит {player}. Сколько конфет он берет? >>> ')
            if not num.isdigit() or 1 > int(num) or int(num) > 28 or int(num) > candy_count:   # Проверка на корректность ввода
                while not num.isdigit() or 1 > int(num) or int(num) > 28 or int(num) > candy_count:
                    num = input(
                        f'{player.capitalize()} ввел неверное значение. Так сколько конфет он берет? >>> ')
            candy_count -= int(num)
            print(
                f'{player.capitalize()} забрал {num} конфет, на столе осталось {candy_count} конфет.')
            print()
            player, second_player = second_player, player
        # Вывод победителя
        print(f'Последним ходил {second_player}, поздравляем с победой!')
        print()
        again()     # Вызов функции для перезапуска игры

    def one_player_smartbot():  # Игра с умным  ботом (если бот ходит первым, игрок обречен)
        import time
        player, second_player = input("Имя игрока >>> "), 'Конфетный бот'
        for i in range(randint(1, 10)):      # Жеребьевка, кто будет первый ходить
            player, second_player = second_player, player
        candy_count = 2021
        while candy_count > 0:
            if player != 'Конфетный бот':     # Ход игрока
                num = input(
                    f'На столе {candy_count} конфет. Ходит {player}. Сколько конфет он берет? >>> ')
                if not num.isdigit() or 1 > int(num) or int(num) > 28 or int(num) > candy_count:
                    while not num.isdigit() or 1 > int(num) or int(num) > 28 or int(num) > candy_count:
                        num = input(
                            f'{player.capitalize()} ввел неверное значение. Так сколько конфет он берет? >>> ')
                candy_count -= int(num)
                print(
                    f'{player.capitalize()} забрал {num} конфет, на столе осталось {candy_count} конфет.')
                print()
                player, second_player = second_player, player
            else:                  # Ход бота
                print(
                    f'На столе {candy_count} конфет. Ходит конфетный бот. Сколько конфет он берет?')
                time.sleep(0.5)
                if candy_count % 29 != 0:    # если остаток от деления оставшегося количества конфет на 29 больше нуля, бот заберет этот остаток
                    num = candy_count % 29
                else:                        # Иначе возьмет рандомное числонадеясь на ошибку игрока
                    num = randint(1, 28)
                candy_count -= num
                print(
                    f'Конфетный бот забрал {num} конфет, на столе осталось {candy_count} конфет.')
                print()
                player, second_player = second_player, player
        # Вывод победителя
        print(f'Последним ходил {second_player}, поздравляем с победой!')
        print()
        again()     # Вызов функции для перезапуска игры

    def one_player_dumbbot():    # Игра с неумным ботом
        import time
        player, second_player = input("Имя игрока >>> "), 'Конфетный бот'
        for i in range(randint(1, 10)):
            player, second_player = second_player, player
        candy_count = 2021
        while candy_count > 0:
            if player != 'Конфетный бот':    # Ход игрока
                num = input(
                    f'На столе {candy_count} конфет. Ходит {player}. Сколько конфет он берет? >>> ')
                if not num.isdigit() or 1 > int(num) or int(num) > 28 or int(num) > candy_count:
                    while not num.isdigit() or 1 > int(num) or int(num) > 28 or int(num) > candy_count:
                        num = input(
                            f'{player.capitalize()} ввел неверное значение. Так сколько конфет он берет? >>> ')
                candy_count -= int(num)
                print(
                    f'{player.capitalize()} забрал {num} конфет, на столе осталось {candy_count} конфет.')
                print()
                player, second_player = second_player, player
            else:    # ход бота
                print(
                    f'На столе {candy_count} конфет. Ходит конфетный бот. Сколько конфет он берет?')
                time.sleep(0.5)
                num = randint(1, 28)     # Тут бот берет просто рандомные числа
                candy_count -= num
                print(
                    f'Конфетный бот забрал {num} конфет, на столе осталось {candy_count} конфет.')
                print()
                player, second_player = second_player, player
        # Вывод победителя
        print(f'Последним ходил {second_player}, поздравляем с победой!')
        print()
        again()   # Вызов функции для перезапуска игры

    def smart_or_dumb():     # Выбор продвинутости бота
        ask = int(input(
            'Для игры с простым ботом введите "0", для игры с умным ботом введите "1" >>> '))
        vars = {0: one_player_dumbbot, 1: one_player_smartbot}
        vars[ask]()

    def solo_or_coop():   # Выбор типа игры (1 или 2 игрока)
        ask = int(input(
            'Для игры с ботом введите "0", для игры с другим игроком введите "1" >>> '))
        vars = {0: smart_or_dumb, 1: two_players}
        vars[ask]()

    solo_or_coop()  # запуск игры с момента выбора количества игроков


def XO():
    from random import randint

    def print_playspace(space):
        n = 0
        for i in range(3):
            for j in range(3):
                print(space[n], end=' ')
                n += 1
            print()

    def check_winner(space, lit):
        
        flag = False
        for i in range(3):
            if space[i] == space[i+3] == space[i + 6] == lit:
                flag = True
        for i in range(0,7,3):
            if space[i] == space[i+1] == space[i + 2] == lit:
                flag = True
        if space[0] == space[4] == space[8] != '_' or space[2] == space[4] == space[6] == lit:
            flag = True
        return flag
    

    def two_players():
        
        playcpace = ['_', '_',  '_',  '_', '_',  '_',  '_',  '_', '_']
        player, second_player = input("Имя первого игрока >>> "), input("Имя второго игрока >>> ")
        print()
        for i in range(randint(1, 10)):   # Жеребьевка, кто будет первый ходить
            player, second_player = second_player, player
        print('''123  <<< поле выглядит так \n456\n789''')
        players_lit, second_players_lit = 'X', 'O'

        for i in range(9):
            choice = input(f'Ходит {player} и ставит {players_lit}. Выберите позицию >>> ')
            if not choice.isdigit() or 1 > int(choice) or 9 < int(choice):
                while not choice.isdigit() or 1 > int(choice) or 9 < int(choice):
                    choice = input(
                        f'{player} ввел неверное значение, введите корректную позицию >>> ')
            if playcpace[int(choice)-1] != '_':
                while playcpace[int(choice)-1] != '_':
                    choice = input(f'Эта позиция занята, выберите другую >>> ')
            playcpace[int(choice)-1] = players_lit
            print_playspace(playcpace)

            if check_winner(playcpace, players_lit):
                print(f'Выиграл {player}!')
                break
            player, second_player = second_player, player
            players_lit, second_players_lit = second_players_lit, players_lit
        if not check_winner(playcpace, players_lit):
            print("У вас ничья")

        restart = input("Реванш? 1 = Да, 0 = Нет") 
        if restart == '1':
            two_players()


    def single_player():
        import sys
        from random import randint

        VERTICAL_COORDINATS = ('a', 'b', 'c')
        EMPTY_CHAR = '_'
        AI_TURN = True
        USER_TURN = False
 
        def show_field(field):
            print(' ', '1', '2', '3')
            for y, v in enumerate(VERTICAL_COORDINATS):
                print(v, ' '.join(field[y]))


        def is_draw(field):
            count = 0
            for y in range(3):
                count += 1 if EMPTY_CHAR in field[y] else 0
            return count == 0


        def get_user_position(field):
            real_x, real_y = 0, 0
            while True:
                coordinats = input('Введите координаты хода >>> ').lower().strip(' ')
                y, x = tuple(coordinats)

                if int(x) not in (1, 2, 3) or y not in VERTICAL_COORDINATS:
                    print('Вы ввели некорректные координаты.')
                    continue

                real_x, real_y = int(x) - 1, VERTICAL_COORDINATS.index(y)
                if field[real_y][real_x] == EMPTY_CHAR:
                    break
                else:
                    print('Тут уже занято')

            return real_x, real_y


        def get_opponent_char(char):
            return '0' if char == 'x' else 'x'


        def is_win(char, field):
            opponent_char = get_opponent_char(char)
            # проверяем строки
            for y in range(3):
                if opponent_char not in field[y] and EMPTY_CHAR not in field[y]:
                    return True

            # проверяем колонки
            for x in range(3):
                col = [field[0][x], field[1][x], field[2][x]]
                if opponent_char not in col and EMPTY_CHAR not in col:
                    return True

            # проверяем диагонали
            diagonal = [field[0][0], field[1][1], field[2][2]]
            if opponent_char not in diagonal and EMPTY_CHAR not in diagonal:
                return True
            diagonal = [field[0][2], field[1][1], field[2][0]]
            if opponent_char not in diagonal and EMPTY_CHAR not in diagonal:
                return True

            return False


        def minimax(board, depth, is_ai_turn):
            if is_win(computer_char, board):
                return scores[computer_char]
            if is_win(user_char, board):
                return scores[user_char]
            if is_draw(board):
                return scores['draw']

            if is_ai_turn:
                # выбираем ход который нам выгодней
                best_score = - sys.maxsize
                for y in range(3):
                    for x in range(3):
                        if board[y][x] == EMPTY_CHAR:
                            board[y][x] = computer_char
                            score = minimax(board, depth + 1, USER_TURN)
                            board[y][x] = EMPTY_CHAR
                            best_score = max(best_score, score)
            else:
                # противник выбирает ход который нам не выгоден
                best_score = sys.maxsize
                for y in range(3):
                    for x in range(3):
                        if board[y][x] == EMPTY_CHAR:
                            board[y][x] = user_char
                            score = minimax(board, depth + 1, AI_TURN)
                            board[y][x] = EMPTY_CHAR
                            best_score = min(best_score, score)
            
            return best_score



        def get_computer_position(field):
            move = None
            best_score = -sys.maxsize
            board = [field[y].copy() for y in range(3)]
            for y in range(3):
                for x in range(3):
                    if board[y][x] == EMPTY_CHAR:
                        board[y][x] = computer_char
                        score = minimax(board, 0, USER_TURN)
                        board[y][x] = EMPTY_CHAR
                        if score > best_score:
                            best_score = score
                            move = (x, y)

            return move


        field = [[EMPTY_CHAR for x in range(3)] for y in range(3)        ]

        user_char = 'x'
        computer_char = '0'

        scores = {
            user_char: -100,
            computer_char: 100,
            'draw': 0
        }

        while True:
            show_field(field)
            if is_draw(field):
                print('У вас ничья')
                break
            print ("Ваш ход")
            x, y = get_user_position(field)
            field[y][x] = user_char
            if is_win(user_char, field):
                print('Вы выиграли')
                break
            
            print('Ход компьютера')
            move = get_computer_position(field)
            if move is not None:

                x, y = move
                field[y][x] = computer_char
                if is_win(computer_char, field):
                    print('Вы проиграли')
                    break

        show_field(field)
        
        restart = input("Реванш? 1 = Да, 0 = Нет") 
        if restart == '1':
            single_player()
    
    def how_many_players():
        count = input('Сколько игроков? (1/2)')
        if count == '1':
            single_player()
        elif count == '2':
            two_players()
        else:
            print('Ну нет, в эту игру играют только двое')
            how_many_players()

    how_many_players()            

def RLE():
    def coder():
        
        with open('input.txt', 'r') as input_file:
            data = input_file.read()
        
        result = ''
        position = 0
        
        while position < len(data):
            char = data[position]
            count = 0
            while position < len(data) and data[position] == char:
                count += 1
                position += 1
            result += f'{count}:{char}<sp>'
        
        with open('output.txt', 'w') as output_file:
            print(result[:-4], file = output_file)
        print("Кодирование выполнено, посмотрите результат в файле 'output.txt'")
    
    def decoder():
        with open('input.txt', 'r', encoding ='UTF-8' ) as input_file, open('output.txt', 'w') as output_file:
            data = input_file.read().split('<sp>')
            for i in data:
                print(int(i[:i.index(':')])*i[i.index(':')+1:], end = '', file = output_file)
            print("Декодирование выполнено, посмотрите результат в файле 'output.txt'")
    def choice():
        ch = input("Кодируем(0) или декодируем?(1) >>> " )
        if ch == '0':
            coder()
        elif ch =='1':
            decoder()
        else:
            print("Эти функции доступны только по платной подписке за $499.99 в месяц")   
            choice()
    choice() 


def HW_start():
    choice = input('Что запускаем? 1: анти-абв; 2: конфетки; 3: Крестики-нолики; 4: кодировщик >>> ')
    if choice == '1':
        delete_abv()
    elif choice == '2':
        candy()
    elif choice == '3':
        XO()
    elif choice == '4':
        RLE()
    else:
        print('Неверный ввод')

HW_start()


