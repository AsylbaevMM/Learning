

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return str(self.value)
    
    def __eq__(self, other):
        return str(self.value) == str(other)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # метод добавления в начало
    def addfirst(self, node):
        node = Node(node)
        if self.head is not None:
            node.next = self.head
            self.head.previous = node
            self.head = node
        else:
            self.head = self.tail = node

    # Метод добавления в конец
    def addlast(self, node):
        node = Node(node)
        if self.tail is not None:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    # Метод добавления элемента полсе заданного значения addafter(искомое значение, новый элемент)
    def addafter(self, checkvalue, node):
        node = Node(node)
        currentnode = self.head
        while not currentnode is None and currentnode.value != checkvalue:
            currentnode = currentnode.next
        if currentnode is not None and currentnode.value == checkvalue:
            node.next = currentnode.next
            node.previous = currentnode
            currentnode.next = node
        else:
            print('Элемент не найден')

    # Метод проверки нахождения какого-то значения в списке
    def contains(self, value):
        currentnode = self.head
        while currentnode is not None:
            if currentnode.value == value:
                return True
            currentnode = currentnode.next
        return False
    
    # Метод удаления значения
    def delete(self, value):
        currentnode = self.head
        while currentnode is not None and currentnode.value != value:
            currentnode = currentnode.next
        if currentnode is not None and currentnode.value == value:
            currentnode.next.previous = currentnode.previous        
            currentnode.previous.next = currentnode.next

    # Магический метод для вывода всего списка через print()
    def __repr__(self):   
        result = []
        currentnode = self.head
        while currentnode is not None:
            result.append(str(currentnode.value))
            currentnode = currentnode.next
        if result:
            return ' '.join(result)
        return 'None'
    
    # метод разворота списка
    def reverse(self):
        currentnode = self.head
        while currentnode is not None:
            currentnode.next, currentnode.previous = currentnode.previous, currentnode.next
            currentnode = currentnode.previous
        self.head, self.tail = self.tail, self.head

    # метод поиска n-го элемента с конца списка, используется список для хранения n элементов
    def nfromtail(self, n):
        temp = [None for i in range(n)]  # Заполняем список n объектами типа None
        currentnode = self.head
        while currentnode is not None:  # Итерируемся до конца связного списка
            temp.append(currentnode.value) # Добавляем в конец хранящего списка элемент
            del temp[0]                     # Удаляем первый
            currentnode = currentnode.next 
        return temp[0]                     # возвращаем первый элемент
    
    # метод поиска n-го элемента с конца списка, используется переменная checknode, которая проходит по списку на n элементов впереди
    def nfromtailother(self, n):
        checknode = self.head
        currentnode = self.head
        for _ in range(n):
            checknode = checknode.next
        while checknode is not None:
            currentnode = currentnode.next
            checknode = checknode.next
        return currentnode