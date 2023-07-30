#set a default user name and password
userName = "admin"
password = "admin"

#take user name and passpwrd from user 
user_name = input("Enter the user name: ")
passWord = input("Enter the password: ")

#now check if the user name and password are correct
if user_name == userName and passWord == password:
    print("Welcome to the system!")
else:
    print("Wrong user name or password!")

for x in user_name:
    print(x)

#we can check using or statement as well
if (user_name == userName) or (passWord == password):
    print("Welcome to our system!")
