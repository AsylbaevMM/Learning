Console.Write("Введите имя пользователя: ");
string username = Console.ReadLine();  

if(username.ToLower() == "маша") //ToLower делает нижний регистр

{
    Console.WriteLine("Ура, это же маша!");
}
else
{
   Console.Write("Привет, "); 
   Console.WriteLine(username);
}