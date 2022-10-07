void zadacha46()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"{rows} {columns}");


    // for (int i = 0; i < rows; i++)
    // {
    //     for (int j = 0; j < columns; j++)
    //     {
    //         numbers[i, j] = random.Next(-10, 10);
    //     }
    // }

    // for (int i = 0; i < rows; i++)
    // {
    //     for (int j = 0; j < columns; j++)
    //     {
    //         Console.Write(numbers[i, j] + "\t");
    //     }
    //     Console.WriteLine();
    // }
    FillArray(numbers);
    PrintArray(numbers);

}

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

void PrintArray(int[,] numbers)
{
    int rows = numbers.GetLength(0);
    int columns = numbers.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            Console.Write(numbers[i, j] + "  ");
        }
        Console.WriteLine();
    }
}

//zadacha46();



void zadacha48()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"Строк:{rows}, Столбцов:{columns}");

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            numbers[i, j] = i + j;
        }
    }

    PrintArray(numbers);
}

//zadacha48();

void zadacha49()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = random.Next(4, 8);
    int[,] numbers = new int[rows, columns];
    Console.WriteLine($"{rows} {columns}");
    FillArray(numbers);
    PrintArray(numbers);
    for (int i = 0; i < rows; i += 2)
    {
        for (int j = 0; j < columns; j += 2)
        {
            numbers[i, j] = numbers[i, j] * numbers[i, j];
        }
    }
    Console.WriteLine();
    PrintArray(numbers);
}
//zadacha49();

void zadacha51()
{
    Random random = new Random();
    int rows = random.Next(4, 8);
    int columns = rows;
    int[,] numbers = new int[rows, columns];
    int sum = 0;
    Console.WriteLine($"{rows} {columns}");
    FillArray(numbers);
    PrintArray(numbers);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (i == j)
            {
                sum = sum + numbers[i, j];
            }
        }
    }
    Console.WriteLine(sum);

}
//zadacha51();

// Дан двумерный массив из двух строк и двадцати двух столбцов. В его пер-
// вой строке записано количество мячей, забитых футбольной командой в той 
// или иной игре, во второй — количество пропущенных мячей в этой же игре. 
// а) Для  каждой  проведенной  игры  напечатать  словесный  результат:  "выиг-
// рыш", "ничья" или "проигрыш".
// а) Для  каждой  проведенной  игры  напечатать  словесный  результат:  "выиг-
// рыш", "ничья" или "проигрыш". 
// б) Определить количество выигрышей данной команды. 
// в) Определить  количество  выигрышей  и  количество  проигрышей  данной  
// команды. 
// г) Определить количество выигрышей, количество ничьих и количество про-
// игрышей данной команды. 
// д) Определить,  в  скольких  играх  разность  забитых  и  пропущенных  мячей 
// была большей или равной трем. 
// е) Определить общее число очков, набранных командой (за выигрыш даются 
// 3 очка, за ничью — 1, за проигрыш — 0).

void FillArrayExtra(int [ , ] numbers, 
                        int minBalls = 0,
                        int maxBalls = 1)
{
    maxBalls++;
    Random random = new Random();
    int rows = numbers.GetLength(0);
    int columns = numbers.GetLength(1);


    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            numbers[i, j] = random.Next(minBalls, maxBalls);
        }
    }

}



void Extra()
{
    Random random = new Random();
    int rows = 2;
    int columns = 22;
    int[,] numbers = new int[rows, columns];
    int sum = 0;
    FillArrayExtra(numbers, 0, 10);
    PrintArray(numbers);
    Console.WriteLine ();
    int countWins = 0;
    int countLose = 0;
    int countDraw = 0;
     for (int i = 0; i < columns; i++)
    {
        Console.WriteLine($"Счет: {numbers[0, i]} : {numbers[1, i]} ");
        if(numbers[0, i] > numbers[1, i])
        {
            Console.WriteLine ("Победа");
            Console.WriteLine ();
            countWins++;
        }
        if(numbers[0, i] == numbers[1, i])
        {
            Console.WriteLine ("Ничья");
            Console.WriteLine ();
            countDraw++;
        }
        if(numbers[0, i] < numbers[1, i])
        {
            Console.WriteLine ("Поражение");
            Console.WriteLine ();
            countLose++;
        }

    }
    Console.WriteLine($"Побед: {countWins}, Поражений: {countLose}, Ничьих: {countDraw}");
    Console.WriteLine($"Общее количество очков: {countWins * 3 + countDraw}");
    Console.WriteLine ();

}
Extra();

// void WinOrLose(int [,] numbers)
// {
//     for (int i = 0; i < columns; i++)
//     {
//         Console.WriteLine($"Счет: {numbers[0, i]} : {numbers[0, i]} ");
//         if(numbers[0, i] > numbers[1, i])
//         {
//             Console.WriteLine ("Победа");
//         }
//     }

// }




