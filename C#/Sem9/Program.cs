void PrintString(int N, int M)
{
    Console.Write(N + " ");
    if (N >= M) return;
    N++;
    PrintString(N, M);
}

void Zadacha63()
{
Console.WriteLine("Введите число N");                         
int N = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число M");                         
int M = Convert.ToInt32(Console.ReadLine());
PrintString(N, M);
}


int SumNum(int num, int sum = 0)
{
    if(num == 0) 
    {
        return sum;
    }
      
    sum = sum + num % 10;
    num = num/10;
    return SumNum(num, sum);
    
}

void Zadacha67()
{
Console.WriteLine("Введите число");                         
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(SumNum(num));
}




int Power(int A, int B, int i = 0, int result = 1)
{
    if(i >= B) 
    {
        return result;
    }
      
    result = result * A;
    i++;
    return Power(A, B, i, result);
    
}

void Zadacha69()
{
Console.WriteLine("Введите число A");                         
int A = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число B");                         
int B = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(Power(A, B));
}

Zadacha69();

















//Zadacha67();






