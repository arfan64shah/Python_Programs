basic_amount = float(input("Enter initial amount: "))
percentage = float(input("Enter interest percentage: "))
time = float(input("Time after which you wanna find the interest: "))
n = float(input("Number of times interest is compounded per time period: ")) 

rate = percentage/100

final_amount = basic_amount * (1 + rate/n) ** (n*time)

print("Final amount is: ", final_amount)