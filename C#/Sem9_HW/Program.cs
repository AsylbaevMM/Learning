void PrintString(int N, int i = 0)
{
    if (N <= i) return;
    Console.Write(N + " ");
    N--;
    PrintString(N, i);
}

void Zadacha64()
{
    Console.WriteLine("Введите число N");
    int N = Convert.ToInt32(Console.ReadLine());
    PrintString(N);
}

//_____________________________________________________________________

int Sum(int N, int M, int sum = 0)
{
    if (N > M) return sum;
    sum = sum + N;
    N++;
    return Sum(N, M, sum);
}

void Zadacha66()
{
    Console.WriteLine("Введите число N");
    int N = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите число M");
    int M = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine(Sum(N, M));

}

//_________________________________________________________________________

int Ackermann(int m, int n)
{
    if (m == 0)
    {
        return n + 1;
    }
    else if (m > 0 && n == 0)
    {
        return Ackermann(m - 1, 1);
    }
    
    return Ackermann(m - 1, Ackermann(m, n - 1));
    

}

void Zadacha68()
{
    Console.WriteLine("Введите число m");
    int m = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите число n");
    int n = Convert.ToInt32(Console.ReadLine());
    if (n >= 0 && m >= 0)
    {
        Console.WriteLine(Ackermann(m, n));
    }
    else
    {
        Console.WriteLine("неверные аргументы");
    }
}



Zadacha64();
Zadacha66();
Zadacha68();