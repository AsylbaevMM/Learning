//Не принимают, не возвращают
void Method1() 
{
    Console.WriteLine("Автор ...");
}
//Method1();

// Только принимают
void Method2(string msg)
{
    Console.WriteLine(msg);
}
//Method2("Текст сообщения");

void Method21(string msg, int count)
{
    int i = 0;
    while (i < count)
    {
        Console.WriteLine(msg);
        i++;
    }
}
//Method21("текст", 12);
//Method21(msg: "текст", count: 12);


//Ничего не принмают, что-то возвращают
int Method3()
{

    return DateTime.Now.Year;
}

int year = Method3();
//Console.WriteLine(year);

//Принимают, возвращают
string Method4(int count, string text)
{
    int i = 0;
    string result = String.Empty; //Создаем пустую строку
    while (i < count)
    {
        result = result + text;
        i++;
    }
    return result;
}

string res = Method4(10, "пример");
Console.WriteLine(res);






