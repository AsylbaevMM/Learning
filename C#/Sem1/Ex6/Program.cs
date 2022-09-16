Console.WriteLine("Введите число");
int num1 = Convert.ToInt32(Console.ReadLine());
num1 = Math.Abs(num1); //Модуль
int num2 = -num1; 
while(num2<=num1)
{
    Console.Write($"{num2}, ");
    num2++;
}
