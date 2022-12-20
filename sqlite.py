import sqlite3
import pandas as pd
import plotly.express as px

#read hr database using sqlite3
conn = sqlite3.connect("hr")



#answer for question2
jobNumbers = pd.read_sql_query("select job_id, COUNT(*) from employees group by job_id", conn)
print(jobNumbers)
fig = px.bar(jobNumbers, x='job_id', y='COUNT(*)')
fig.show()

#answer for question 3
salaryDiff = pd.read_sql_query("select max(salary)-min(salary) DIFFERENCE from employees", conn)
print(salaryDiff)

