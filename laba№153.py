# Вхідні дані: координати точок (x, y)
# Перша пара: x = 2, y = -4 (очікується IV чверть)
# Друга пара: x = -4, y = 3 (очікується II чверть)

points = [
    (2, -4),
    (-4, 3)
]

for x, y in points:
    # Використовуємо конструкцію розгалуження для визначення чверті
    if x > 0 and y > 0:
        print("I")
    elif x < 0 and y > 0:
        print("II")
    elif x < 0 and y < 0:
        print("III")
    elif x > 0 and y < 0:
        print("IV")