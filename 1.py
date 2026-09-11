# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Addition
print("Addition =", num1 + num2)

# Subtraction
print("Subtraction =", num1 - num2)

# Multiplication
print("Multiplication =", num1 * num2)

# Division
if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Division is not possible because you cannot divide by zero.")