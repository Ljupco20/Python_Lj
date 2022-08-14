def multiplication_or_sum(num1, num2):
    num3 = num1 * num2
    if(num3 < 1000):
        return num3
    else:
        return num1 + num2


number1 = int(input("Enter first number "))
number2 = int(input("Enter second number"))
result = multiplication_or_sum(number1, number2)
print("The result is", result)
