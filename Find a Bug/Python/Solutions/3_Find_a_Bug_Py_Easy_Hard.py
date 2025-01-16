class Counter: # Třída, která má 2 metody.
    def __init__(self): # 1. metoda (spustí se sama při vytvoření třídy díky použití __init__)
        # Inicializace počítadla na 0
        self.count = 0

    def increment(self): #2. metoda (spustí se až když se vyvolá)
        # Zvyšujeme hodnotu počítadla o 1
        self.count += 1

# Vytváření instance třídy Counter a následné uložení do proměnné c1.
c1 = Counter()

# Vytváření další proměnnou c2, která bude odkazovat na stejnou instanci jako c1.
c2 = c1

# Níže opravit chybu
c2.increment() # Použijte metodu increment na c2, abyste zvýšili počítadlo o jeden. Tím dosáhneme výsledku.
# Výše opravit chybu

# Vytiskněte hodnotu počítadla z c1 a ověřte, že se zvýšila.
print("c2: " + str(c2.count)) # Očekávaný výsledek: c2: 1