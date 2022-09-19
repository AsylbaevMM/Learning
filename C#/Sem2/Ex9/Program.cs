void Zadacha9()
{
    Random random = new Random();
    int number = random.Next(10,100);
    Console.WriteLine(number);
    int tens = number / 10;
    int ones = number % 10;
    Console.WriteLine(tens);
    Console.WriteLine(ones);
}

void Zadacha11()
{
    Random random = new Random();
    int number = random.Next(100,1000);
    Console.WriteLine(number);
    int hundreds = number / 100;
    int ones = number % 10;
    int result = hundreds * 10 + ones;
    Console.WriteLine(result);
    

}


void Zadacha13()
{
    Console.WriteLine("Введите первое число");     
    int num1 = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите второе число");
    int num2 = Convert.ToInt32(Console.ReadLine()); 

    if (num2 % num1 == 0)
    {
        Console.WriteLine("Кратно");
    }
    else
    {
        Console.WriteLine($"Не кратно, остаток = {num2 % num1}");
    }

}

 
 
 void Zadacha14()
{
    Console.WriteLine("Введите число");     
    int num1 = Convert.ToInt32(Console.ReadLine());
     

    if (num1 % 7 == 0 && num1 % 23 == 0)
    {
        Console.WriteLine("Кратно");
    }
    else
    {
        Console.WriteLine("Не кратно");
    }

}


void Zadacha15()
{   
    int input()
    {
      Console.WriteLine("Введите первое число");     
      return Convert.ToInt32(Console.ReadLine());  
    }
         
    int num1 = input();
    int num2 = input(); 

    if (num1 == Math.Pow(num2, 2) || num2 == num1 * num1)
    {
        Console.WriteLine("Да");
    }
    else
    {
        Console.WriteLine("нет");
    }

}

Zadacha15();


