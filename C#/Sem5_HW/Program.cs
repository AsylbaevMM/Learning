
// Метод наполнения массива целыми числами
void FillArray(int[] numbers,
                int minValue = 0,
                int maxValue = 200)
{
    maxValue++;
    Random random = new Random();
    for (int i = 0; i < numbers.Length; i++)
    {
        numbers[i] = random.Next(minValue, maxValue);
    }
}

// Метод наполнения массива вещественными числами
void FillArrayDouble(double[] numbers,
                int minValue = 0,
                int maxValue = 200)
{
    maxValue++;
    Random random = new Random();
    for (int i = 0; i < numbers.Length; i++)
    {
        numbers[i] = Math.Round((random.Next(minValue, maxValue) + random.NextDouble()), 2);
        //Ниже предыдущие варианты создания случайных чисел, к которым я пришел
        //numbers[i] =  Convert.ToDouble(random.Next(minValue, maxValue)) / 100;  
        //numbers[i] = random.Next(minValue * 100, maxValue * 100) / 100.0; 
        
    }
}

// Метод вывода массива
void PrintArray(int[] numbers)
{
    Console.WriteLine("Массив:");
    for (int i = 0; i < numbers.Length; i++)
    {

        Console.Write(numbers[i] + "  ");
    }
    Console.WriteLine();
    Console.WriteLine();
}

// Метод вывода массива вещественных числел
void PrintArrayDouble(double[] numbers)
{
    Console.WriteLine("Массив:");
    for (int i = 0; i < numbers.Length; i++)
    {

        Console.Write(numbers[i] + "  ");
    }
    Console.WriteLine();
    Console.WriteLine();
}



// Метод подсчета и вывода количества четных элементов в массиве
void CountEven(int[] numbers)
{
    int count = 0;
    for (int i = 0; i < numbers.Length; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            count++;
        }

    }
    Console.WriteLine($"Количество четных элементов в массиве равно {count}");
    Console.WriteLine();
}

//Метод подсчета и вывода суммы нечетных элементов массива
void SumOdd(int[] numbers)
{
    int sum = 0;
    for (int i = 1; i < numbers.Length; i += 2)
    {
        sum = sum + numbers[i];
    }
    Console.WriteLine($"Сумма элементов c нечетным индексом в массиве равна {sum}");
    Console.WriteLine();
}

//Метод сортировки массива вещественных чисел
void SelectionSort(double[] numbers)
{
    for (int i = 0; i < numbers.Length - 1; i++)
    {
        int minPosition = i;

        for (int j = i+1; j < numbers.Length; j++)
        {
            // Abs для сортировки по модулю
            if(numbers[j] < numbers[minPosition])
            {
                 minPosition = j;
            }     
        }

        double temp = numbers[i];
        numbers[i] = numbers[minPosition];
        numbers[minPosition] = temp;
    }
    Console.WriteLine("Сортировка...");
    Console.WriteLine();
}




void zadacha34()
{
    Console.WriteLine("Задача 34");
    Console.WriteLine("Введите Размер массива");
    int size = Convert.ToInt32(Console.ReadLine()); 
    Console.WriteLine();
    int[] numbers = new int[size];
    FillArray(numbers, 100, 999);
    PrintArray(numbers);
    CountEven(numbers);
}

void zadacha36()
{
    Console.WriteLine("Задача 36");
    Console.WriteLine("Введите Размер массива");
    int size = Convert.ToInt32(Console.ReadLine()); 
    Console.WriteLine();
    int[] numbers = new int[size];
    FillArray(numbers, -10, 10);
    PrintArray(numbers);
    SumOdd(numbers);
}

void zadacha38()
{
    Console.WriteLine("Задача 38");
    Console.WriteLine("Введите Размер массива");
    int size = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine();
    double[] numbers = new double[size];
    FillArrayDouble(numbers, -100, 100);
    PrintArrayDouble(numbers);
    SelectionSort(numbers);
    PrintArrayDouble(numbers);
    Console.WriteLine($"max = {numbers[^1]}, min = {numbers[0]}, difference = {numbers[^1] - numbers[0]}");
    Console.WriteLine();
}


zadacha34();
zadacha36();
zadacha38();