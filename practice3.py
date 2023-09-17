# here i am practing basic python skills

# declare variables
a = 10
b = 9

print("The value of a is ", a)
print("The address of a is ", id(a))
print("The address of b is ", id(b))

print("Value of a is " + str(a) + " its address is " + str(id(a)))

# operators in Python
# arithmatic operators
add = a + b
print("the sum is ", add)
sub = a - b
print("Subtraction is ", sub)
div = a / b
print("The division is ", div)
multiply = a * b
print("The multiplication is ", multiply)
mod = a % b
print("The modulus is ", mod)
floor = a // b
print("the floor division is ", floor)

# comparison operators
great = a > b
print("a is greater than b: ", great)
less = a < b
print("a is less than b: ", less)
gore = a >= b
print("a is greater than or equal to b: ", gore)
lore = a <= b
print("a is less than or equal to: ", lore)

# logical operators
c = 0
d = -1

if(a > 10 and c >= 0):
    print("I am Arfan")
elif(a >= 10 or c >= 0):
    print("My name is Shah")
else:
    print("I am no one")

# membership operators
lst = [1, 2, 3, 4, 5]

print("1 is in the list: ", 1 not in lst)

e = 1
f = 1

print(e is not f)


# bitwise operators
num1 = 10
num2 = 8

print("Bitwise or of two numbers is ", num1 ^ num2)


# list
lst = [1, 2, 'arfan', 3.3]

lst[2] = 'shah'
print(lst)

tupl = (1, 2, 'arfan', 3.3)

print(tupl[1])

# dicationary 
dic = {'arfan': 5, 'shah': 4}
dic['arfan'] = 56
print(dic['arfan'])

sett = {1, 2, 3, 4, 4, 5, 5, 6}
#sett[1] = 10
print(sett)

# eval function in user input
n = eval(input("Enter the first name: "))
m = eval(input("Enter second name: "))

print(n+m)
    
