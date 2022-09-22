

void zadacha17()
{
    Console.WriteLine("Задача 17");

    Random random = new Random();

    int x = random.Next(-10, 11);
    int y = random.Next(-10, 11);
    Console.WriteLine($"A{x}, {y}");
    CoordCheck(x, y);
}


void CoordCheck(int x, int y)
{
    if (x > 0 && y > 0)
    {
        Console.WriteLine($"a{x}, {y} Лежит в первой");
    }

    else if (x < 0 && y > 0)
    {
        Console.WriteLine($"a{x}, {y} Лежит во второй");
    }
    else if (x < 0 && y < 0)
    {
        Console.WriteLine($"a{x}, {y} Лежит в третьей");
    }
    else if (x > 0 && y < 0)
    {
        Console.WriteLine($"a{x}, {y} Лежит в четветрой");
    }
    else
    {
        Console.WriteLine($"a{x}, {y} Не относится ни к одной");
    }
}



void zadacha18()

{
    Console.WriteLine("Задача 18");
    Console.WriteLine("Введите четверть");
    int num = Convert.ToInt32(Console.ReadLine());
    Check(num);
}


void Check(int num)
{
    if (num == 1)
    {
        Console.WriteLine($"В первой четверти х в диапазоне (0; +∞), у в диапазоне (0; +∞)");
    }

    else if (num == 2)
    {
        Console.WriteLine($"Во второй четверти х в диапазоне (-∞; 0), у в диапазоне (0; +∞)");
    }
    else if (num == 3)
    {
        Console.WriteLine($"В третьей четверти х в диапазоне (-∞; 0), у в диапазоне (-∞; 0)");
    }
    else if (num == 4)
    {
        Console.WriteLine($"В четвертой четверти х в диапазоне (0; +∞), у в диапазоне (-∞; 0)");
    }
    else
    {
        Console.WriteLine($"Неверный ввод");
    }
}





void zadacha21()
{
    Console.WriteLine("Задача 21");

    Random random = new Random();

    int x1 = random.Next(0, 100);
    int y1 = random.Next(0, 100);
    int x2 = random.Next(0, 100);
    int y2 = random.Next(0, 100);

    Console.WriteLine($"A {x1}, {y1}");
    Console.WriteLine($"B {x2}, {y2}");
    Dist(x1, y1, x2, y2);
}


void Dist(int x1, int y1, int x2, int y2)
{

    Console.WriteLine($"Расстояние между точками = {Math.Sqrt(Math.Pow((x2 - x1), 2) + Math.Pow((y2 - y1), 2))}");


}


//zadacha21();
//zadacha18();
//zadacha17();



//Напишите программу, которая принимает на вход число (N) и выдаёт таблицу квадратов чисел от 1 до N.

void zadacha22()

{
    Console.WriteLine("Задача 22");
    Console.WriteLine("Введите число");
    int num = Convert.ToInt32(Console.ReadLine());
    result(num);
}

void result(int num)
{
    int i = 1;
    if (num > 1)
    {
        while (i <= num)
           {
             Console.WriteLine($"Квадрат числа {i} = {Math.Pow((i), 2)}");
           i++;
           }
    }
    else
    {
         while (num <= 1)
           {
             Console.WriteLine($"Квадрат числа {num} = {Math.Pow((num), 2)}");
           num++;
           }
    }

}

zadacha22();