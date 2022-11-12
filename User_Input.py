num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def sum():
    sum = num1 + num2
    return sum

def subtract():
    subtract = num1 - num2
    return subtract

def multiply():
    multiply = num1 * num2
    return multiply

def division():
    division = num1/num2
    return division

desire = int(input("Enter\n1 for sum\n2 for difference\n3 for multiplication\n4 for division\n"))

if(desire == 1):
    print("Sum is ", sum())
elif(desire == 2):
    print("Difference is ", subtract())
elif(desire == 3):
    print("Multiplication is ", multiply())
elif(desire == 4):
    print("Division is ", division())
else:
    print("Invalid Input. Please select numbers from 1 to 4")