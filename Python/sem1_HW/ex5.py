a = [int(i) for i in input('Введите координаты точки А через пробел >>> ').split()]
b = [int(i) for i in input('Введите координаты точки Б через пробел >>> ').split()]
print(f'Расстояние между точками = {round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5, 2)}')