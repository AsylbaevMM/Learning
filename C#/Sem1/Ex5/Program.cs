Console.WriteLine("Введите число");
int value = Convert.ToInt32(Console.ReadLine());
if (value == 1)
{
    Console.WriteLine("Понедельник");
}
else if (value == 2)
{
    Console.WriteLine("Вторник");
}
else if (value == 3)
{
    Console.WriteLine("Среда");
}
else if (value == 4)
{
    Console.WriteLine("Четверг");
}
else if (value == 5)
{
    Console.WriteLine("Пятница");
}
else if (value == 6)
{
    Console.WriteLine("Суббота");
}
else if (value == 7)
{
    Console.WriteLine("Воскресенье");
}
else
// if (value > 7)
{
    Console.WriteLine("Нет такого дня недели");
}