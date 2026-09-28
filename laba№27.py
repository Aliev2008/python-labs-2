f = float(input("Enter the desired future value: "))
r = float(input("Enter the annual interest rate: "))
n = float(input("Enter the number of years the money will grow: "))

p = f / ((1 + r) ** n)

print(f"You will need to deposit this amount: {p:.2f}")