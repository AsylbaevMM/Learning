//Функция

int Power(int x)
{
        return x * x;
}
Console.WriteLine("Введите число");
int number = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(Power(number));
