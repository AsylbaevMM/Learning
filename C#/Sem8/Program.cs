void FillArray(int[,] numbers)
{

    Random random = new Random();
    int rows = numbers.GetLength(0);
    int columns = numbers.GetLength(1);


    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            numbers[i, j] = random.Next(-100, 100);
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


void zadacha53()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");

    FillArray(numbers);
    PrintArray(numbers);
    int max_i = numbers.GetLength(1);
    for (int j = 0; j < max_i; j++)
    {
        (numbers[0, j], numbers[numbers.GetLength(0) - 1, j]) = (numbers[numbers.GetLength(0) - 1, j], numbers[0, j]);
    }
    Console.WriteLine();
    PrintArray(numbers);
}




void zadacha55()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");
    FillArray(numbers);
    PrintArray(numbers);
    Console.WriteLine();
    if (rows == columns)
    {
        int max_i = numbers.GetLength(1);
        for (int i = 0; i < max_i; i++)
        {
            for (int j = i; j < max_i; j++)
            {
                (numbers[i, j], numbers[j, i]) = (numbers[j, i], numbers[i, j]);
            }
        }
        PrintArray(numbers);
    }
    else
    {
        Console.WriteLine("Задача невыполнима");
    }
}




void Zadacha57()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");
    FillArray(numbers);
    PrintArray(numbers);
    int[] counts = new int[10];

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            counts[numbers[i, j]]++;
        }
    }

    for (int i = 0; i < 10; i++)
    {
        Console.WriteLine($"Количество {i} в  массиве равно {counts[i]}");
    }

}

void Zadacha59()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");
    FillArray(numbers);
    PrintArray(numbers);
    int min = numbers[0, 0];
    int min_i = 0;
    int min_j = 0;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (numbers[i, j] < min)
            {
                min = numbers[i, j];
                min_i = i;
                min_j = j;
            }
        }
    }
    Console.WriteLine($"{min_i}, {min_j}, {numbers[min_i,min_j]} ");

    int[,] newArray = new int[rows - 1, columns - 1];

    int bias_i = 0;
    int bias_j = 0;
    for (int i = 0; i < rows - 1; i++)
    {
        
        if (i == min_i) bias_i++;
        bias_j = 0;
        for (int j = 0; j < columns - 1; j++)
        {
            if(j == min_j) bias_j++;
            newArray[i,j] = numbers[i + bias_i, j + bias_j];
        }
    }

    Console.WriteLine();
    PrintArray(newArray);

}
Zadacha59();















//zadacha53();
//zadacha55();
//Zadacha57();