from input_data import input_data_main
from output_data import output_data_main
from writer import writer_main
from reader import reader_main

def choice():
    answer = input('Что бы ввести новую запись нажмите Enter\nЧто бы найти запись введите фамилию, имя или телефон >>> ')
    if answer == '':
        var = input('Какой формат ввода предпочитаете? Для ввода в одну строку введите 1, для пошагового ввода введите 2 >>> ')
        while var not in ['1', '2']:
            var = input('Вы ввели некорректное значение. Для ввода данных в одну строку введите 1, для пошагового ввода введите 2 >>> ')
        input_data_main(int(var))
    else:
        output_data_main(reader_main(answer))


choice()