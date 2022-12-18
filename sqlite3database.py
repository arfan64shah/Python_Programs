import sqlite3
import pandas as pd

dataset = pd.read_csv('diabetes.csv')

#create an empty database
conn = sqlite3.connect('diabetes.db')
print(dataset)

create_sql = '''create table if not exists diabetes(Pregnancies INTEGER, Glucose INTEGER, BloodPressure INTEGER, SkinThicknesss INTEGER,
                Insulin INTEGER, BMI REAL, Age INTEGER, Outcome INTEGER)'''
cur = conn.cursor()

cur.execute(create_sql)

#now put data into diabetes from the diabetes.csv
for row in dataset.itertuples():
    insert_sql = f'''insert into diabetes(Pregnancies, Glucose, BloodPressure, SkinThicknesss, Insulin, BMI,
                     Age, Outcome) values({row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]})'''
    cur.execute(insert_sql)

conn.commit()
