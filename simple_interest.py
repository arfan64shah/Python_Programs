current_balance = int(input("Enter your current balance: "))
annual_interest = int(input("Enter annual interest rate: "))
time = int(input("Enter number of years: "))

#changing interest rate into decimal
interest_rate = annual_interest/100

final_balance = current_balance*(1+interest_rate*time)

interest = (current_balance*annual_interest*time)/100

print("Final amount is ", final_balance)
print("Interest is ", interest)