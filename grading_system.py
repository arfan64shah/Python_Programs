percentage = int(input("Enter your percentage: "))

if(percentage >= 90):
    print("Your grade is A")
elif((percentage >= 85) & (percentage < 90)):
    print("Your grade is A-")
elif((percentage >= 80) & (percentage < 85)):
    print("Your grade is B+")
elif((percentage >= 75) & (percentage < 80)):
    print("Your grade is B")
elif((percentage >= 70) & (percentage < 75)):
    print("Your grade is B-")
elif((percentage >= 65) & (percentage < 70)):
    print("Your grade is C+")
elif((percentage >= 60) & (percentage < 65)):
    print("Your grade is C")
elif((percentage >= 55) & (percentage < 60)):
    print("Your grade is C-")
elif((percentage >= 50) & (percentage < 55)):
    print("Your grade is D")
else:
    print("Your percentage is ", percentage)
