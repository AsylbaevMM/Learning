

def check_string(data):   
    if data:       # <---------------- Пустые строки интерпретируются Python'ом как False, непустые как True
        return f"Успешный ввод строки '{data}'"
    raise ValueError('Пустые строки недопустимы!!') #  <------ Выбрасываем исключение, если строка пустая

try:
    print(check_string(input("Введите что угодно >>>  ")))
except Exception as e:  #  <------------ Ловим сообщение исключения
    print(e)    
