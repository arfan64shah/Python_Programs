import sqlite3 as sq

db = sq.connect("infor.db")

#now create a table
db.execute('''
create table info(
    passport VARCHAR(20) primary key,
    cnic int,
    fname varchar(50),
    lname varchar(50),
    fatherName varchar(50),
    phoneNumber varchar(15)
)

''')

def enter():
    print("Enter passport number: ")
    passport = input()

    print("Enter cnic number: ")
    cnic = input()

    print("Enter first name: ")
    fname = input()

    print("Enter last name: ")
    lname = input()

    print("Enter father's name: ")
    fatherName = input()

    print("Enter phone number: ")
    phone = input()

    db.execute('''
    insert into info(passport, cnic, fname, lname, fatherName, phoneNumber)
    values(' ''' + passport + ''' ', ''' + cnic + ''', ' ''' + fname + ''' ', ' ''' + lname + ''' ', ' ''' + fatherName + ''' ', ' ''' + phone + ''' ')'''

    )
    db.commit()
    db.close()


def ask():
    print('''Do you want to add instances into table? 
    If yes then write yes in small letters
    If no write no: ''')
    ans = input()
    return ans

while(ask() == 'yes'):
    enter()
