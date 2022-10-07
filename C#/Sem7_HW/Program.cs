

void FillArray(int[,] numbers)
{
    //int[ , ] numbers = new int[rows, columns];
    Random random = new Random();
    int rows = numbers.GetLength(0);
    int columns = numbers.GetLength(1);


    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            numbers[i, j] = random.Next(-10, 10);
        }
    }
}

void FillArrayDouble(double[,] numbers)
{
    //int[ , ] numbers = new int[rows, columns];
    Random random = new Random();
    int rows = numbers.GetLength(0);
    int columns = numbers.GetLength(1);
    
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            numbers[i, j] = Math.Round((random.Next(-100, 100) + random.NextDouble()), 1);
        }
    }
}

void PrintArray(int[,] numbers)
{
    int rows = numbers.GetLength(0);
    int columns = numbers.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            Console.Write(numbers[i, j] + "\t");
        }
        Console.WriteLine();
    }
}

void PrintArrayDouble(double[,] numbers)
{
    int rows = numbers.GetLength(0);
    int columns = numbers.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            Console.Write(numbers[i, j] + "\t");
        }
        Console.WriteLine();
    }
}

void zadacha47()
{
    Console.WriteLine("Задача 47");
    Console.WriteLine("Введите количество строк");
    int rows = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите количество столбцов");
    int columns = Convert.ToInt32(Console.ReadLine());
    double[,] numbers = new double[rows, columns];
    FillArrayDouble(numbers);
    PrintArrayDouble(numbers);
    Console.WriteLine();
}

void Zadacha50()
{
    Console.WriteLine("Задача 50");
    Random random = new Random();
    int rows = random.Next(5, 10);
    int columns = random.Next(5, 10);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");
    FillArray(numbers);
    PrintArray(numbers);
    Console.WriteLine("Введите индекс строки");
    int row = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите индекс столбца");
    int column = Convert.ToInt32(Console.ReadLine());

    if (row < rows && column < columns)
    {
        Console.WriteLine($"Значение элемента с индексом [{row},{column}] равно {numbers[row, column]} ");
    }
    else
    {
        Console.WriteLine("Элемент не найден");
    }
    Console.WriteLine();
}

void Zadacha52()
{
    Console.WriteLine("Задача 52");
    Random random = new Random();
    int rows = random.Next(5, 10);
    int columns = random.Next(5, 10);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");
    FillArray(numbers);
    PrintArray(numbers);

    for (int j = 0; j < columns; j++)
    {        
        double sum = 0;
        for (int i = 0; i < rows; i++)
        {
            sum = numbers[i,j] + sum;
        }
        Console.WriteLine($"Среднее арифметическое {j+1} столбца = {Math.Round(sum/(rows), 2)}");
    }
    Console.WriteLine();
}


zadacha47();
Zadacha50();
Zadacha52();