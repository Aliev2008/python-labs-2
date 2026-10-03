# Вхідні дані для змішування кольорів
color1 = "blue"
color2 = "red"

# Перевіряємо допустимість введених кольорів (red, green, blue)
valid_colors = ["red", "green", "blue"]

if color1 not in valid_colors or color2 not in valid_colors:
    print("Повідомлення про відсутність такої палітри")
elif color1 == color2:
    print("Повідомлення про відсутність такої палітри")
# Змішування червоного та зеленого -> жовтий
elif (color1 == "red" and color2 == "green") or (color1 == "green" and color2 == "red"):
    print("Yellow")
# Змішування синього і зеленого -> блакитний
elif (color1 == "blue" and color2 == "green") or (color1 == "green" and color2 == "blue"):
    print("Cyan")
# Змішування синього і червоного -> пурпуровий (Magenta)
elif (color1 == "blue" and color2 == "red") or (color1 == "red" and color2 == "blue"):
    print("Magenta")