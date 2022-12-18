#import required libraries
import sqlite3
import pandas as pd

#now read the data using pandas
dataset = pd.read_csv('heart.csv')
print(dataset)

#now create a databse in sqlite3 for the above dataset
conn = sqlite3.connect('heart.db')
create_dataset = '''

create table heart(age INTEGER, sex INTEGER, cp INTEGER, trestbps INTEGER, chol INTEGER, restecg INTEGER, thalach INTEGER, 
                    exang INTEGER, oldpeak REAL, slope INTEGER, ca INTEGER, thal INTEGER, target INTEGER)

'''
cur = conn.cursor()
cur.execute(create_dataset)

#now put the values in heart.csv into the heart.db or sqlite3 database
for row in dataset.itertuples():
    insert_dataset = f'''insert into heart(age, sex, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal, target)
                        values({row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]})
    
    '''
    cur.execute(insert_dataset)

conn.commit()
conn.close()