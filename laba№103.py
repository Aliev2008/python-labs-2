name1 = "Guido van Rossum"
name2 = "Dennis Ritchie"

# Порівнюємо імена в алфавітному порядку за допомогою конструкції розгалуження (if-else)
if name1 < name2:
    # Якщо перше ім'я йде раніше за алфавітом, виводимо його першим
    print(name1)
    print(name2)
else:
    # Інакше спочатку виводимо друге ім'я
    print(name2)
    print(name1)
