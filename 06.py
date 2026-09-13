#wapp to define a method dosum(num) to find out he sum of the digit of num and return it.

def dosum(num):
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    return sum


num = int(input("Enter a number: "))

result = dosum(num)

print("Sum of digits =", result)
