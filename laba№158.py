# Вхідні дані: двоцифрові числа
numbers = [55, 19, 15]

for n in numbers:
    # Знаходимо десятки та одиниці числа
    tens = n // 10
    units = n % 10
    
    # Знаходимо суму цифр
    digit_sum = tens + units
    
    # Перевіряємо, чи є сума двоцифровим числом (тобто чи більша або дорівнює 10)
    if digit_sum >= 10:
        print("True")
    else:
        print("False")