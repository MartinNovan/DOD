# Upravte kód ve vyznačeném rozmezí, použitím existujícího kódu, k dosažení výsledku
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c1 = Counter()
c2 = c1
# Níže opravit chybu

# Výše opravit chybu
print("c2: " + str(c2.count)) # Očekávaný výsledek: c2: 1