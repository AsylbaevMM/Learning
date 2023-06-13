# Создайте класс исключения, который будет выбрасываться при делении на 0. 
#Исключение должно отображать понятное для пользователя сообщение об ошибке.
# Создайте класс исключений, которое будет возникать при обращении к пустому элементу в 
#массиве ссылочного типа. Исключение должно отображать понятное 
#для пользователя сообщение об ошибке
# Создайте класс исключения, которое будет возникать при попытке открыть несуществующий файл. 
#Исключение должно отображать понятное для пользователя сообщение об ошибке.


# class ZeroDivisionErr(Exception):
#     def __init__(self):
#         super().__init__('Деление на ноль запрещено')

    
# try:
#     d = 5 /0
# except ZeroDivisionError:
#     raise ZeroDivisionErr


# class ArrayError(Exception):
#     def __init__(self, index):
#         super().__init__(f'Несуществующий индекс: {index}')

    
# try:
#     arr = [1,2,3]
#     print(arr[4])
# except IndexError:
#     raise ArrayError(4)



class FileError(Exception):
    def __init__(self, index):
        super().__init__(f'Несуществующий файл: {index}')

    
try:
    link = 'qwerty'
    file = open(link, mode = 'r')
except FileNotFoundError:
    raise FileError(link)