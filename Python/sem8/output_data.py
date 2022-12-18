def output_data_main(args):
    
    if args is None:
        print('Совпадения не найдены')
    
    else:

        choice = input('Выбирите формат вывода информации: 1. В одну строку, 2. В несколько строк >>> ')
        
        while choice not in '12':
            print('Вы ввели некорректное значение!')
            choice = input('Выбирите формат вывода информации: 1. В одну строку, 2. В несколько строк >>> ')
        
        if choice == '1':
            print(" ".join(args))
        if choice == '2':
            print("\n".join(args))

#output_data_main(['Иванов', 'Иван', '987654321', 'Текстовое описание'])