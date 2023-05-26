from linkedlist import LinkedList, Node
import time
# создаем новый список
newlist = LinkedList()

# Заполняем нечетными значениями добавляя в конец
for i in range(1, 15, 2):
    newlist.addlast(Node(i))

# выводим результат
print('Заполнение в конец:')
print(newlist, '\n')


# Заполняем четными значениями добавляя в начало
for i in range(2, 15, 2):
    newlist.addfirst(Node(i))

# выводим результат
print('Заполнение в начало:')
print(newlist, '\n')


# Добавляем элемент после определенного значения
newlist.addafter(2, 'new')
print('Добавление элемента "new" после элемента "2"')
print(newlist, '\n')
print('Добавление элемента "new" после элемента "q"(элемент "q" не существует)')
newlist.addafter('q', 'new')
print()


# проверка наличия элемента
print("Есть ли элемент со значением '5':", newlist.contains(5))
print("Есть ли элемент со значением '25':", newlist.contains(25))
print()

# Удаление элемента
print('Удаления элемента "new":')
newlist.delete('new')
print(newlist, '\n')

# разворот списка
print('Разворот списка')
newlist.reverse()
print(newlist, '\n')

# вывод n-го элемента с конца списка (с использованием списка)
print("Третий элемент с конца списка:", newlist.nfromtail(3))

# вывод n-го элемента с конца списка (с использованием двух переменных)
print('Третий элемент с конца списка другим способом:', newlist.nfromtailother(3))


