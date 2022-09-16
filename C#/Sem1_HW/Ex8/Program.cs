//Ввод значения
Console.WriteLine("Введите положительное число");
int num1 = Convert.ToInt32(Console.ReadLine());

//Задание первого значения
int i = 2;

//Цикл проверки условия и вывода
while (i <= num1)
{
    Console.Write($"{i}, ");
    i = i + 2;
}