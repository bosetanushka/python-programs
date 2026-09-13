#wapp to define a method checkarmstrong (num) that will return true if the num  is armstrong and return false if not.


def checkarmstrong(num):
    original = num
    digits = len(str(num))
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if sum == original:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if checkarmstrong(num):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
