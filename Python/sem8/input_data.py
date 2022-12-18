def input_data_main(format):
    if format == 1:
        last_name, first_name, phone_number, *comment = input(
            'Введите фамилию, имя, номер телефона и комментарий: ').split()
        comment = ' '.join(comment)
        return [last_name, first_name, phone_number, comment]
    if format == 2:
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        comment = input("Введите комментарий: ")
        return [last_name, first_name, phone_number, comment]


