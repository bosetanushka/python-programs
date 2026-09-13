#python progran to define a method factorial parameter and return the result after computing the 
#factorial the guven number.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial =", result)
