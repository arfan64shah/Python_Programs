#take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#write a function for addition
def add(num1, num2):
    sum = num1 + num2
    return sum

#write function for subtraction
def subtract(num1, num2):
    subtract = num1 - num2
    return subtract

#write a function for multoplication
def multiply(num1, num2):
    multiply = num1 * num2
    return multiply

#write a function for division
def divide(num1, num2):
    divide = num1 / num2
    return divide

#write function for modulus
def modulus(num1, num2):
    modulus = num1 % num2
    return modulus

#take input from user either the user wants to add, subtract, multiply, divide, or modulus
operation = input("Enter operation to be performed: ")
if (operation == "addition" or operation == "add"):
    print("The addition of the entered numbers is ", add(num1, num2))
elif (operation == "subtraction" or operation == "subtract"):
    print("The subtraction of the entered numbers is ", subtract(num1, num2))
elif (operation == "multiplication" or operation == "multiply"):
    print("The multiplication of the entered numbers is ", multiply(num1, num2))
elif (operation == "division" or operation == "divide"):
    print("The division of the entered numbers is ", divide(num1, num2))
else:
    print("The modulus of the entered number is ", modulus(num1, num2))