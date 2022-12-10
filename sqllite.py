import sqlite3

conn = sqlite3.connect("myDatabase.db")

#create table
# conn.execute('''
#         Create table students (
#             st_id INT AUTO_INCREMENT PRIMARY KEY,
#             st_name VARCHAR(50),
#             st_class VARCHAR(20),
#             st_email VARCHAR(50),
#             st_gender VARCHAR(20)
#         )

#     ''')

print("Enter student's id: ")
id = input()

print("Enter student's name: ")
name = input()

print("Enter student's class: ")
clas = input()

print("Enter student's email: ")
email = input()

print("Enter student's gender: ")
gender = input()

insert = '''
        insert into students (st_id, st_name, st_class, st_email, st_gender)
        values (''' + id + ''', ' ''' + name + ''' ', ' ''' + clas + ''' ', ' ''' + email + ''' ', ' ''' + gender + ''' ')'''

conn.execute(insert)
conn.commit()
conn.close()

