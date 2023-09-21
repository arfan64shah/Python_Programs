# import random module
import random as rn

# take input from user
user_input = int(input("Enter a number between 0-100: "))

# take random input from computer
computer_input = rn.randint(0, 100)

if (user_input == computer_input):
    print("Computer guessed number is ", computer_input)
    print("wow! Your guess is correct!")
elif (user_input > computer_input):
    print("Computer guessed number is ", computer_input)
    print("Your guessed number is quite high!")
else:
    print("Computer guessed number is ", computer_input)
    print("Your guessed number is quite low!")