int[] array = { 12, 22, 34, 4, 5, 3, 2, 3, 44, 33, 3456 };

int n = array.Length;
int find = 3;

int index = 0;
 
while (index < n)
{
    if (array[index] == find)
    { 
        Console.WriteLine(index);
        break;   //Остановиться на первом элементе
    }
    index ++;
}