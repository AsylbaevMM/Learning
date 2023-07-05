a, b, c = int(input('Введите сторону а')), int(input('Введите сторону b')), int(input('Введите сторону c'))
if a + b < c or b + c < a or a + c < b:
    result = 'Треугольник не существует'
else:
    result = 'Треугольник существует'
    if a == b or b == c or c == a:
        result = 'Треугольник равнобедренный'
    if a == b == c:
        result = 'Треугольник равносторонний'
print(result)