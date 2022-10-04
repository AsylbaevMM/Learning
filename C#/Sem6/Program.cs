void  FillArray(int[] numbers,
                int minValue = 0,
                int maxValue = 9)
{
    int size = numbers.Length;
    Random random = new Random();
    for (int i = 0; i < size; i++)
    {
        numbers[i] = random.Next(minValue, maxValue);
    }
}

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

void ReverseArray(int[] numbers)
{
    int size = numbers.Length;
    int maxIndex = size - 1;
    for (int i = 0; i < size/2; i++)
    {
        // int temp = numbers[i];
        // numbers[i] = numbers[maxIndex - i];
        // numbers[maxIndex - i] = temp;
        (numbers[i], numbers[maxIndex - i]) = (numbers[maxIndex - i], numbers[i]);
    }
}

void zadacha39()
{
    int size = 10;
    int[] numbers = new int[size];
    FillArray(numbers, -10, 10);
    PrintArray(numbers);
    ReverseArray(numbers);
    PrintArray(numbers);
}

//zadacha39();

void zadacha40()
{
    Console.WriteLine("Введите длину стороны А");
    int A = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите длину стороны B");
    int B = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите длину стороны C");
    int C = Convert.ToInt32(Console.ReadLine());
    if (A < (B + C) && B < (A + C) && C < (A + B))
    {
        Console.WriteLine("Треугольник существует");
    }
    else
    {
        Console.WriteLine("Треугольник не существует");
    }
}

//zadacha40();

void zadacha42()
{
    Console.WriteLine("Введите число");
    int number = Convert.ToInt32(Console.ReadLine());
    string result = "";
    int temp;
    //int num = 
    while (number > 0)
    {
        result =  number%2 + result;
        number /= 2;                                                                                   
    }
    
    Console.WriteLine(result);
}
//zadacha42();

void zadacha42a()
{
    int number = 43;
    string result = Convert.ToString(number, 2);
    Console.WriteLine(result);
}
//zadacha42a();


void zadacha44()
{
    Console.WriteLine("Введите число");
    int size = Convert.ToInt32(Console.ReadLine());
    int a = 0;
    int b = 1;
    int[] numbers = new int[size];
    numbers[0] = a;
    numbers[1] = b;
    for (int i = 2;  i < numbers.Length; i++)
    {
        numbers[i] = numbers[i-2] + numbers[i -1];
    }
    PrintArray(numbers);
}
//zadacha44();


void zadacha45()
{
    int size = 10;
    int[] numbers1 = new int[size];
    int[] numbers2 = new int[size];

    FillArray(numbers1);
    for (int i = 0; i < numbers2.Length; i++)
    {
        numbers2[i] = numbers1[i];
    }
    PrintArray(numbers1);
    PrintArray(numbers2);
}
zadacha45();


