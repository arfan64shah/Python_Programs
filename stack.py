# program to show stack
# select a function
l = []
while True:
    operation = int(input('''
                      1: Append Element
                      2: Pop Element
                      3: Peek Element
                      4: Display Stack
                      5: Exit
                      
                      Select the operation: '''))
    if(operation == 1):
        element = input("Enter element to be added: ")
        l.append(element)
        print(l)
    elif(operation == 2):
        if(len(l) == 0):
            print("Stack is empty!")
        else:
            p = l.pop()
            print("Element removed is ", p)
            print(l)
    elif(operation == 3):
        if(len(l) == 0):
            print("Stack is empty!")
        else:
            print("The last element in stack is ", l[-1])
    elif(operation == 4):
        print("Full stack: ", l)
    elif(operation == 5):
        break
    else:
        print("Please select a correct operation!")