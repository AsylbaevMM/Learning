Console.WriteLine("Введите положительное число");
int num1 = Convert.ToInt32(Console.ReadLine());
num1 = Math.Abs(num1); //Защита от бесконечного цикла
int i = 2;
while (i <= num1)
{
    Console.Write($"{i}, ");
    i = i + 2;
}