void zadacha25()
{   
    //Взаимодействие с пользователем и ввод
    Console.WriteLine("Задача 25");
    Console.WriteLine("Введите число");
    int num1 = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите степень возведения");
    int num2 = Convert.ToInt32(Console.ReadLine());
    int result = 1;

    //Цикл с вычислением произведения
    for (int i = 1; i <= num2; i++)
    {
        result = result * num1;
    }

    //Вывод результата
    Console.WriteLine($"{num1} в степени {num2} равно {result}"); 
    Console.WriteLine();
}


//________________________________________________________________________________

void zadacha27()
{   
    //Взаимодействие с пользователем и ввод
    Console.WriteLine("Задача 27");
    Console.WriteLine("Введите число");
    int num = Convert.ToInt32(Console.ReadLine());
    int current = num;
    int result = 0;

    //Цикл с вычислением суммы
    while (num > 0)
    {
        result = result + num % 10;
        num = num / 10;
    }

    //вывод Результата
    Console.WriteLine($"Сумма цифр в числе {current} равна {result}"); 
    Console.WriteLine();
}


//_______________________________________________________________________


void zadacha29()
{   
    //Объявление переменных
    Console.WriteLine("Задача 29");
    Random random = new Random();
    int size = 8;
    int[] numbers = new int[size];
    
    //Вызов методов, форматирование вывода
    FillArray(numbers);
    Console.WriteLine("Исходный массив: ");
    PrintArray(numbers);
    SelectionSort(numbers);
    Console.WriteLine();
    Console.WriteLine("Отсортированный массив: ");
    PrintArray(numbers);

}

//Метод наполнения массива
void FillArray(int[] num)
{
    Random random = new Random();
    for (int i = 0; i < num.Length; i++)
    {
        num[i] = random.Next(-100, 100);
    }
}

//Метод вывода массива
void PrintArray(int[] num)
{
   for (int i = 0; i < num.Length; i++)
    {
        Console.Write(num[i] + "  ");
    } 
}

//Метод сортировки массива
void SelectionSort(int[] num)
{
    for (int i = 0; i < num.Length - 1; i++)
    {
        int minPosition = i;

        for (int j = i+1; j < num.Length; j++)
        {
            // Abs для сортировки по модулю
            if(Math.Abs(num[j]) < Math.Abs(num[minPosition]))
            {
                 minPosition = j;
            }     
        }

        int temporary = num[i];
        num[i] = num[minPosition];
        num[minPosition] = temporary;
    }
    Console.WriteLine();
}


zadacha25();
zadacha27();
zadacha29();