void zadacha31()
{
    int size = 12;
    int[] numbers = new int[size];
    FillArray(numbers);
    PrintArray(numbers);
    Console.WriteLine(GetSummPositive(numbers));
    Console.WriteLine(GetSummNegative(numbers));
}

int GetSummPositive(int[] numbers)
{
    int sum = 0;
    for (int i = 0; i < numbers.Length; i++)
    {
        if (numbers[i] > 0)
            sum += numbers[i];
    }
    return sum;
}

int GetSummNegative(int[] numbers)
{
    int sum = 0;
    for (int i = 0; i < numbers.Length; i++)
    {
        if (numbers[i] < 0)
            sum += numbers[i];
    }
    return sum;
}


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

void PrintArray(int[] numbers)
{
    Console.WriteLine("Вывод массива");
    for (int i = 0; i < numbers.Length; i++)
    {

        Console.Write(numbers[i] + "  ");
    }
    Console.WriteLine();
}
//zadacha31();

//____________________________________________________________________________

void zadacha32()
{
    int size = 12;
    int[] numbers = new int[size];
    FillArray(numbers, -100, 100);
    PrintArray(numbers);
    ChangeArray(numbers);
    PrintArray(numbers);
}

void ChangeArray(int[] numbers)
{
    for (int i = 0; i < numbers.Length; i++)
    {
        numbers[i] *= -1;
    }
}
//zadacha32();

void zadacha33()
{
    Console.WriteLine("Введите число для поиска в массиве");
    int check = Convert.ToInt32(Console.ReadLine());
    int size = 10;
    int[] numbers = new int[size];
    FillArray(numbers);
    CheckArray(numbers, check);
    PrintArray(numbers);
}

void CheckArray(int[] numbers, int check)
{
    bool flag = false;
    for (int i = 0; !flag && i < numbers.Length; i++)
    {
        if (check == numbers[i])
        {
            flag = true;
        }
    }

    // int i = 0;
    // while(!flag && i < numbers.Length)
    // {
    //     if (check == numbers[i])
    //     {
    //         flag = true;
    //     }
    //     i++;
    // }


    if (flag)
        Console.WriteLine("Находится");
    else
        Console.WriteLine("Не находится");
}
//zadacha33();


void zadacha34()
{
    int size = 10;
    int[] numbers = new int[size];
    FillArray(numbers);
    CheckNumbers(numbers);
    PrintArray(numbers);


    void CheckNumbers(int[] numbers)
    {
        int count = 0;
        for (int i = 0; i < numbers.Length; i++)
        {
            if (numbers[i] <= 99 && numbers[i] >= 10)
            {
                count++;
            }
        }
        Console.WriteLine($"В массиве {count} подходящих элементов");
    }

}
//zadacha34();

void zadacha37()
{
    int size = 10;
    int[] numbers = new int[size];
    FillArray(numbers);
    PrintArray(numbers);

    int maxIndex = size - 1;
    for (int i = 0; i < size / 2; i++)
    {
        Console.WriteLine($"{numbers[i]} * {numbers[maxIndex - i]} = {numbers[i] * numbers[maxIndex - i]}");
    }
    Console.WriteLine();
}
zadacha37();