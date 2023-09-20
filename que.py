# write a program for queue
que = []

while(True):
    operation = int(input('''
                          
                          1: Append
                          2: Dequeue
                          3: Front element
                          4: Rear element
                          5: Display queue
                          6: Exit
                          Enter Required Operation from above: '''))
    if(operation == 1):
        el = input("Enter the element to be added: ")
        que.append(el)
        print("Queue: ", que)
    elif(operation == 2):
        del que[0]
        print("Queue: ", que)
    elif(operation == 3):
        if(len(que) == 0):
            print("Queue is empty!")
        else:
            print("The front element in the queue is ", que[-1])
    elif(operation == 4):
        if(len(que) == 0):
            print("Queue is empty!")
        else:
            print("The rear element in the queue is ", que[0])
    elif(operation == 5):
        print("Queue: ", que)
    elif(operation == 6):
        break
    else:
        print("Please select correct operation!")
        