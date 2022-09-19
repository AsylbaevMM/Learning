void zadacha2()
{
    //Ввод значений
Console.WriteLine("Введите первое число");
int num1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите второе число");
int num2 = Convert.ToInt32(Console.ReadLine());

// Сравнение и вывод
if (num1 > num2)          
{
    Console.WriteLine($"max={num1}, min={num2}");
}
else 
{
    Console.WriteLine($"max={num2}, min={num1}");
}

}


void zadacha6()
{
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
}

zadacha2();
zadacha6();
