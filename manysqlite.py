import sqlite3 as sq

conn = sq.connect("manydb.db")
cur = conn.cursor()

#create a table

# cur.execute('''
# create table customers(
#     c_id int primary key,
#     c_fname varchar(50),
#     c_lname varchar(50),
#     c_email varchar(50)
# )
    


# ''')

# many_data = [
#     (1, 'arfan', 'shah', 'arfan@gmail.com'),
#     (2, 'zulfiqar', 'azam', 'zulfiqar@gmail.com'),
#     (3, 'tajwar', 'ali', 'tajwar@gmail.com'),
#     (4, 'munner', 'abbas', 'munner@gmail.com')
# ]

# cur.executemany("insert into customers values(?, ?, ?, ?)", many_data)

cur.execute("select * from customers where c_lname like '%a%' ")
print(cur.fetchall())



conn.commit()
conn.close()