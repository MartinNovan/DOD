// Opravte kód pro dosažení výsledku
List<int> numberList = new List<int>(){1,2,3}; 
for (int i = numberList.Count - 1; i >= 0; i--) 
{
    if (numberList[i] = 2)
    {
        numberList.RemoveAt(i); // Odstranění prvku na indexu i
    }
}
Console.WriteLine(string.Join(", ", numberList)); // Požadovaný výstup: 1, 3