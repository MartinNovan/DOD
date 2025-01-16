def find_maximum(numbers):
    # Tato funkce hledá největší číslo v seznamu čísel.
    
    # Inicializujeme proměnnou max_num na nejmenší možné číslo,
    # abychom mohli porovnávat s čísly v seznamu.
    # Pokud bychom nechali číslo na 0 tak žádné číslo v seznamu není větší což vede k nepoužitelnému kódu
    # Poznámka: číslo by se mohlo nastavit třeba i na -4 aby kód fungoval a je to také správné řešení, ale zde ukazujeme ideální, kdyby jsme seznal čísel neviděli
    max_num = float('-inf')  
    
    # Pro každé číslo v seznamu 'numbers' provedeme následující:
    for num in numbers:
        # Zkontrolujeme, zda je aktuální číslo (num) větší než max_num.
        if num > max_num:
            # Pokud ano, aktualizujeme max_num na toto číslo.
            max_num = num  # max_num nyní obsahuje větší číslo.
    
    # Po prozkoumání všech čísel vrátíme největší číslo, které jsme našli.
    return max_num  # Vrátí maximální číslo nalezené v seznamu.

# Zde testujeme funkci s příkladem, kde očekáváme, že vrátí -1,
# protože to je největší číslo v seznamu [-1, -2, -3].
print(find_maximum([-1, -2, -3])) # Očekávaný výsledek: -1