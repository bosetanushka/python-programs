#wapp to define a method is prime(num) to check whether  the number is prime or not.

def isprime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if isprime(num):
    print("The number is Prime")
else:
    print("The number is Not Prime")
