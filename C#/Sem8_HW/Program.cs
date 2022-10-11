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




void Zadacha54()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");

    FillArray(numbers);
    PrintArray(numbers);

    for (int i = 0; i < rows; i++)
    {

        for (int j = 0; j < columns; j++)
        {
            for (int k = j + 1; k < columns; k++)
            {
                if (numbers[i, k] < numbers[i, j])
                {
                    (numbers[i, k], numbers[i, j]) = (numbers[i, j], numbers[i, k]);
                }
            }
        }
    }

    Console.WriteLine();
    PrintArray(numbers);

}


void Zadacha56()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");

    FillArray(numbers);
    PrintArray(numbers);
    int max_sum = 0;
    int i_max_sum = 0;
    Console.WriteLine();

    for (int i = 0; i < rows; i++)
    {
        int sum = 0;
        for (int j = 0; j < columns; j++)
        {
            sum = sum + numbers[i, j];
        }
        if (sum > max_sum)
        {
            max_sum = sum;
            i_max_sum = i;
        }
        Console.WriteLine($"Сумма элементов {i + 1} столбца равна {sum} ");
    }
    Console.WriteLine();
    Console.WriteLine($"Максимальная сумма принадлежит {i_max_sum + 1} строке и равна {max_sum}");
    Console.WriteLine();

}

void Zadacha58()
{
    int rows = 4;
    int columns = 4;
    int[,] numbers = new int[rows, columns];
    int value = 1;
    int start_row = 0;
    int start_column = 0;
    
    int j = 0;
    for (int i = start_row; i < columns; )
    {
        
        while ((i, j) != (start_row + 1, start_column))
        {
            numbers[i, j] = value;
            value++;
            if (i == start_row && j != columns - 1) { j++; }
            else if (i != rows - 1 && j == columns - 1) { i++; }
            else if (i == rows - 1 && j != start_column) { j--; }
            else if (i != start_row + 1   && j == start_column) { i--; }
            numbers[i, j] = value;
                     
        }

      

        start_row++;
        start_column++;
        columns--;
        rows--;
    }


    PrintArray(numbers);
}


void Extra()
{   
   
    Console.WriteLine("Введите количество строк матрицы А");
    int rowsA = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите количество столбцов матрицы А");
    int columnsA = Convert.ToInt32(Console.ReadLine());
    int[,] matrixA = new int[rowsA, columnsA];
    
    Console.WriteLine("Введите количество строк матрицы Б");
    int rowsB = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите количество столбцов матрицы Б");
    int columnsB = Convert.ToInt32(Console.ReadLine());
    int[,] matrixB = new int[rowsB, columnsB];

    Console.WriteLine();

    Console.WriteLine($"Матрица А. Строк:{rowsA}, Столбцов:{columnsA}");
    FillArray(matrixA);
    PrintArray(matrixA);

    Console.WriteLine();

    Console.WriteLine($"Матрица Б. Строк:{rowsB}, Столбцов:{columnsB}");
    FillArray(matrixB);
    PrintArray(matrixB);

    Console.WriteLine();

    if(columnsA == rowsB)
    {
        int[,] resultMatrix = new int[rowsA, columnsB];
        
         for (int i = 0; i < rowsA; i++)
            {

                for (int j = 0; j < columnsB; j++)
                {
                    int sum = 0;
                    for(int m = 0; m < columnsA; m++)
                    {
                        
                        sum = sum + matrixA[i,m]*matrixB[m,j];
                        
                    }
                    resultMatrix[i,j]=sum;
                }
            }
        Console.WriteLine("Произведение матрицы:");    
        PrintArray(resultMatrix);    
    }
    else
    {
        Console.WriteLine("Умножение матриц невозможно");
    }

}






//Zadacha54();
//Zadacha56();
//Zadacha58();
//Extra();




