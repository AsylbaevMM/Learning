//Zadacha24
//Задача 24: Напишите программу, которая принимает на вход число (А) и выдаёт сумму чисел от 1 до А.


void zadacha24()
{
    int number = 15;
    int sum = 0;
    for (int i = 1; i <= number; i++)
    {
        Console.Write($"{i} + ");
    }
    Console.Write("\b\b\b\b");

}
//zadacha24();

void zadacha26()
{
    int number = 1234322;
    int current = number;
    int count = 0;
    while (current > 0)
    {
        current = current / 10;
        count = count + 1;
    }
    Console.WriteLine($"Количество цифр в числе {number} = {count}");
}

//zadacha26();


void zadacha28()
{
    int number = 12;
    int result = 1;
    for (int i = 1; i <= number; i++)
    {
        result = result * i;
        i++;
    }
    Console.WriteLine($"Произведение чисел = {result}");

}
//zadacha28();

//Задача 30: Напишите программу, которая выводит массив из 8 элементов, 
// заполненный нулями и единицами в случайном порядке.
// [1,0,1,1,0,1,0,0]

void zadacha30()
{
    Random random = new Random();
    int size = random.Next(4, 10);
    int[] numbers = new int[size];
   
    // for (int i = 0; i < size; i++)
    // {
    //     numbers[i] = random.Next(0, 2);
    // }
    FillArray(numbers);
    PrintArray(numbers);

    // for (int i = 0; i < size; i++)
    // {
    //     Console.Write(numbers[i] + "  ");
    // }

    //Console.WriteLine(numbers[]);

}
void FillArray(int[] num)
{
    Random random = new Random();
    for (int i = 0; i < num.Length; i++)
    {
        num[i] = random.Next(0, 2);
    }
}
void PrintArray(int[] num)
{
   for (int i = 0; i < num.Length; i++)
    {
        Console.Write(num[i] + "  ");
    } 
}
//zadacha30();



