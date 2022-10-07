void PrintArray(int[] numbers)
{
    Console.WriteLine("Вывод массива:");
    int size = numbers.Length;
    for (int i = 0; i < size; i++)
    {
        Console.Write(numbers[i] + " ");
    }
    Console.WriteLine();
}



void zadacha41()
{
    //Взаимодействие с пользователем
    Console.WriteLine("Введите любое количество чисел");
    Console.WriteLine("После каждого числа нажимайте Enter");
    Console.WriteLine("После ввода всех чисел нажмите Enter два раза");

    // Объявление переменных
    int[] numbers = new int[0];
    int i = 0;
    int count = 0;
    int countless0 = 0;

    //Тут создаю рекурсию, выход из которой происходит при получении пустой строки(нажатии Enter без ввода)
    void input()
    {
        string temp = Console.ReadLine();
        if (temp == "") return;
        Array.Resize(ref numbers, numbers.Length + 1);
        numbers[i] = Int32.Parse(temp);
        //Array.Resize(ref numbers, numbers.Length + 1);
        i++;
        count++;
        if (Int32.Parse(temp) > 0) countless0++;
        input();

    }

    input();
    //Вывод результатов
    PrintArray(numbers);
    Console.WriteLine();
    Console.WriteLine($"Вы ввели {count} чисел, {countless0} из них больше нуля");
    Console.WriteLine();
}
zadacha41();



void zadacha43()
{
    //Взаиомдействие с пользователем
    Console.WriteLine("Введите параметр К1:");
    double K1 = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите параметр B1:");
    double B1 = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите параметр К2:");
    double K2 = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите параметр B2:");
    double B2 = Convert.ToInt32(Console.ReadLine());

    //Условия и вывод
    if (K1 - K2 != 0)
    {
    double X = Math.Round((B2 - B1) / (K1 - K2), 2);
    double Y = Math.Round(K1*X + B1, 2);
    Console.WriteLine($"Координаты точки пересечения прямых: {X} , {Y}");
    }
    else
    {
     Console.WriteLine("Прямые параллельны");   
    }
}


zadacha43();
