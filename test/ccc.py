#Формируем первый  и втророй список из членов
data1 = '2x^5 + 4x^4 + 5x^2 + 10x + 88 = 0'

left1 = data1[:data1.index('=')]
lst1 =  left1.split(" + ")
#print(lst1)
# left2 = data2[:data2.index('=')]
# lst2 =  left2.split(" + ")
#print(lst2)


#Создаем списки для степеней и коэффициентов для 2х уравнений
#тут проверку на степен 1 и 0 для одного и другого уравнения
eq_a1 = []
eq_n1 = []
for i in range(len(lst1)):
    if lst1[i][(lst1[i].index('x')+1):] == '':
        b = lst1[i][:lst1[i].index('x')]
        print(b)
        break

    if lst1[i].isdigit(): 
         
        print(lst1[i])
        

    n1 = lst1[i][(lst1[i].index('^')+1):]
    a1 = lst1[i][:lst1[i].index('x')]
    eq_n1.append(n1)
    eq_a1.append(a1)
eq_n1.append(-1)
print(eq_n1)
print(eq_a1)
print(b)
# print(c)