string text = "олупрвмл толыв. - лоыуар олырп, ыфклпо - "
            + "цау ца.ац кп цуас, ыралв- мцкопыват"
            + "укып уумыксро, влаоыс. каыо-цаьшщр";

string Replace(string text, char oldValue, char newValue)
{
    string result = String.Empty;

    int length = text.Length;
    for (int i = 0; i < length; i++)
    {
        if(text[i] == oldValue) result = result + $"{newValue}";
        else result = result + $"{text[i]}";
    }

    return result;
}

string newText = Replace(text, ' ', '_');
Console.WriteLine(newText);
Console.WriteLine();
newText = Replace(newText, 'с', 'С');
Console.WriteLine(newText);
Console.WriteLine();
newText = Replace(newText, 'к', 'К');
Console.WriteLine(newText);