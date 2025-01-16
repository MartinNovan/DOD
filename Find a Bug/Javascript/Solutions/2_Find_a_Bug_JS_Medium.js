let numbers = [1, 2, 3]; // Pole s čísly 1, 2 a 3
// Chyba: Začínáme s i na 0, ale původní podmínka říká, že smyčka se má vykonávat, dokud je i větší délce pole. To znamená, že smyčka nikdy nezačne, protože 0 není větší nebo rovno 3 (délka pole).
for (let i = 0; i < numbers.length; i++) { //Nyní podmínka říká, že smyčka se má vykonávat, dokud je i menší délce pole. Momentálně se smyčka bude opakovat podle délky pole (neboli zde 3x)
    console.log(numbers[i]); // Tiskne aktuální číslo z pole
}

/* Výsledek jsou tyto čísla:
1
2
3
*/