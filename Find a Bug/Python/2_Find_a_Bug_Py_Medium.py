# Upravte stávající kód k dosažení výsledku
def find_maximum(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_maximum([-1, -2, -3])) # Očekávaný výsledek: -1
