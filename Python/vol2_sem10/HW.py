# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег



class ATM:
    def __init__(self):
        self._balance = 0
        self._move_count = 0
        self._in_process = False

    def check_move_count(self):
        self._move_count += 1
        if not self._move_count % 3:
            self._balance *= 1.03

    def cash_deposit(self, value):
        self.check_move_count()
        self._balance += value

    def cash_withdrawal(self, value):
        comission  = value * 0.015
        comission = max(30, comission)
        comission = min(600, comission)
        if self._balance >= value + comission:
            self.check_move_count()
            self._balance -= value + comission
        else:
            print('Недостаточно средств')

    def move(self):
        if self._balance > 5_000_000:
            self._balance *= 0.9
        while self._in_process:
            print(f"Текущий баланс: {self._balance}")
            print('''Доступные действия:
    1. Внести
    2. Снять
    3. Выход ''')
            choice = input('Введите действие >>> ')
            if choice in ['1', '2']:
                value = '10'
                while not value.isdigit() or int(value) % 50:
                    print( not value.isdigit(), bool(int(value) % 50))
                    value = input('Введите сумму кратную 50 >>> ')
                if choice == '1':
                    self.cash_deposit(int(value))
                else:
                    self.cash_withdrawal(int(value))
            elif choice == '3':
                self._in_process = False
            else:
                print('Некорректный ввод')

    def start(self):
        choice = input("Вы стоите у банкомата. Что бы вставить карту нажмите Enter, что бы уйти введите leave >>> ")
        while choice != 'leave':
            self._in_process = True
            self.move()
            choice = input("Вы стоите у банкомата. Что бы вставить карту нажмите Enter, что бы уйти введите leave >>> ")
        print('До новых встреч!')


atm = ATM()
atm.start()
