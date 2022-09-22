
void zadacha19()

{
    // Взаимодействие с пользователем и ввод
    Console.WriteLine("Задача 19");
    Console.WriteLine("Введите пятизначное число");
    int num = Convert.ToInt32(Console.ReadLine());

    if (Math.Abs(num) > 9999 && Math.Abs(num) < 100000)  // проверка на пятизначность
    {
        if (num / 10000 == num % 10 && num / 1000 % 10 == num % 100 / 10)  //проверка на равенство противостоящих чисел
        {
            Console.WriteLine("Число является палиндромом");   // вывод
        }
        else
        {
            Console.WriteLine("Число не является палиндромом");
        }
    }
    else
    {
        Console.WriteLine("Это не пятизначное число");
    }
}


//____________________________________________________________________________________


void zadacha21()
{
    Console.WriteLine("Задача 21");

    //Создание случайных точек
    Random random = new Random();   

    int x1 = random.Next(0, 100);
    int y1 = random.Next(0, 100);
    int z1 = random.Next(0, 100);
    int x2 = random.Next(0, 100);
    int y2 = random.Next(0, 100);
    int z2 = random.Next(0, 100);

    //Вывод координат точек
    Console.WriteLine($"A {x1}, {y1}, {z1}");
    Console.WriteLine($"B {x2}, {y2}, {z2}");
    
    //Функция для нахождения квадрата разности координат
    int sumsqr(int num1, int num2)
    {

    int result = Convert.ToInt32(Math.Pow((num1 - num2), 2));
    return result;
        
    }

    //Математика и вывод расстояния
    Console.WriteLine($"Расстояние между точками = {Math.Sqrt(sumsqr(x1, x2) + sumsqr(y1, y2) + sumsqr(z1, z2))}");

}


//______________________________________________________________________________________________


void zadacha23()

{   
    //Взаимодействие с пользователем и ввод
    Console.WriteLine("Задача 23");
    Console.WriteLine("Введите число");
    int num = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Число\tКуб"); //вывод заголовка таблицы
    result(num);
}

//проверка числа положительное/отрицательное, циклы и вывод
void result(int num)
{
    int i = 1;
    if (num > 1)
    {
            
        while (i <= num)
           {
             Console.WriteLine("{0}\t{1}", i, Math.Pow(i, 3));
           i++;
           }
    }
    else
    {
           while (i >= num)
           {
             Console.WriteLine("{0}\t{1}", i, Math.Pow(i, 3));
           i--;
           }
    }

}


zadacha19();
zadacha21();
zadacha23();