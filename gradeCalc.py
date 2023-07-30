#obtained marks
obtained_marks = float(input("Enter the obtained marks: "))

#total marks
total_marks = float(input("Enter the total marks: "))

#obtained percentage
obtained_percentage = (obtained_marks/total_marks)*100

#grade
if (obtained_percentage >= 90 and obtained_percentage <= 100):
    print("Grade otained is A")
elif (obtained_percentage >= 85 and obtained_percentage <= 89):
    print("Grade obtained is A-")
elif (obtained_percentage >= 80 and obtained_percentage <= 84):
    print("Grade obtained is B+")
elif (obtained_percentage >= 75 and obtained_percentage <= 79):
    print("Grade obtained is B")
elif (obtained_percentage >= 70 and obtained_percentage <= 74):
    print("Grade obtained is B-")
elif (obtained_percentage >= 65 and obtained_percentage <= 69):
    print("Grade obtained is C+")
elif (obtained_percentage >= 60 and obtained_percentage <= 64):
    print("Grade obtained is C")
elif (obtained_percentage >= 55 and obtained_percentage <= 59):
    print("Grade obtained is C-")
elif (obtained_percentage >= 50 and obtained_percentage <= 54):
    print("Grade obtained is D")
else:
    print("Grade obtained is F")