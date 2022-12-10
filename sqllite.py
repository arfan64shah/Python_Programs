import sqlite3

connect = sqlite3.connect("myDatabase.db")



insert = '''
        insert into students (st_id, st_name, st_class, st_email, st_gender)
        values ()

'''

connect.execute(insert)
connect.commit()
connect.close()

