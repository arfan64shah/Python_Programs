import sqlite3

#initiate database
db = sqlite3.connect("newdb.db")

db.execute('''
        create table meritList(
            std_id INT PRIMARY KEY,
            std_fname VARCHAR(50),
            std_lname VARCHAR(50),
            std_email VARCHAR(50),
            std_class varchar(50),
            std_rank int
        )
''')

#add instances to dataset
print("Eneter student's id: ")
id = input()

print("Enter student's first name: ")
fname = input()

print("Enter student's last name: ")
lname = input()

print("Enter student's email: ")
email = input()

print("Enter student's class: ")
clas = input()

print("Enter student's rank in class: ")
rank = input()

db.execute('''
        insert into meritList(std_id, std_fname, std_lname, std_email, std_class, std_rank)
        values(''' + id + ''', ' ''' + fname + ''' ', ' ''' + lname + ''' ', ' ''' + email + ''' ', ' ''' + clas + ''' ', ''' + rank + ''')'''
        
        
)

db.commit()
db.close()
