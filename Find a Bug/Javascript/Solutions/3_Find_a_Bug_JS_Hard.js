// Upravte kód k dosažení výsledku
function isEven(number) {
    //Poznámka operace number % 2 vrací zbytek po dělení čísla number číslem 2
    if ((number % 2) == 0) { // V podmínce je původně jen jedno = což slouží k přiřazení hodnoty ale ne k porovnaní, pro porovnání používáme == nebo === (== a === fungují podobně ale nejsou stejná!, zde bude fungovat obojí)
        return true; // Vrací true, pokud je číslo sudé
    } else {
        return false; // Vrací false, pokud je číslo liché
    }
}
console.log("Je sudé: " + isEven(4)); // Výsledný výstup = Je sudé: true
console.log("Je sudé: " + isEven(7)); // Výsledný výstup = Je sudé: false