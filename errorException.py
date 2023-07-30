try:
    def divide(a, b):
        print(a / b)
    divide(1, 0)
except ZeroDivisionError:
    print("You cannot divide by zero! please use another number")