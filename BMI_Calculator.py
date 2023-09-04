#take name of the person
name = input("Enter your name: ")
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

#calculation of BMI
bmi = weight/(height*height)*703

#write function for the situation of person
if bmi > 0:
    if bmi <= 18.4:
        print(name + ", you are underweight!")
    elif(bmi > 18.4 and bmi <= 24.9):
        print(name + ", your weight is normal!")
    elif(bmi > 24.9 and bmi <= 39.9):
        print(name + ", you are overweight")
    else:
        print(name + ", you are obese!")
else:
    print("Kindly fill with valid information!")