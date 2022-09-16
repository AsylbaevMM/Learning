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

