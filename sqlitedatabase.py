import sqlite3

db = sqlite3.connect("citizenship.db")

#create a table
# db.execute('''
# create table citizenship(
#     c_nic INT PRIMARY KEY,
#     c_fname VARCHAR(50),
#     c_lname VARCHAR(50),
#     c_fathername varchar(50),
#     c_city varchar(50),
#     c_province varchar(50),
#     c_district varchar(50) 
# )

# ''')
#enter data into database
print("Enter nic number: ")
nic = input()

print("Enter first name: ")
fname = input()

print("Enter last name: ")
lname = input()

print("Enter father's name: ")
fatherName = input()

print("Enter name of city: ")
city = input()

print("Enter province name: ")
province = input()

print("Enter name of district: ")
district = input()

db.execute('''
insert into citizenship(c_nic, c_fname, c_lname, c_fathername, c_city, c_province, c_district)
values(''' + nic + ''', ' ''' + fname + ''' ', ' ''' + lname + ''' ', ' ''' + fatherName + ''' ', ' ''' + city + ''' ', ' ''' + province + ''' ', ' ''' + district +
''' ')'''
)

db.commit()
db.close()