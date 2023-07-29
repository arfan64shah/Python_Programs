amount = float(input("Enter initial amount: "))
percentage = float(input("Enter interest percentage: "))
time = float(input("Time after which you wanna find the interest: "))

rate = percentage/100

interest = amount * rate * time

print("Interest is: ", interest)

final_amount = amount + interest

print("Final amount is: ", final_amount)
