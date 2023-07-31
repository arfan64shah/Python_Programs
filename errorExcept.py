try:
    num1 = 20
    num2 = 0

    divide = num1 / num2
    print(divide)

except Exception as e:
    print(e)
finally:
    print("This is the code block which will be always executed!")