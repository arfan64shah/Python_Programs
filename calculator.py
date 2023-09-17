# Build a simple calculator using python
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
print('''
      Select operation accordingly:
      Add: 1
      Subtract: 2
      Multiply: 3
      Divide: 4
      Floor Division: 5
      Modulus: 6
      
      ''')
operation = eval(input("Select the operation: "))

if (operation == 1):
    print("The sum of the enetered numbers is ", num1 + num2)
elif(operation == 2):
    print("Subtraction of entered numbers is ", num1 - num2)
elif(operation == 3):
    print("Multiplication of entered numbers is ", num1 * num2)
elif(operation == 4):
    print("DIvision of entered numbers is ", num1 / num2)
elif(operation == 5):
    print("Floor division of entered numbers is ", num1 // num2)
elif(operation == 6):
    print("Modulus of entered numbers is ", num1 % num2)
else:
    print("Please select a valid operation!")
    
