import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3


URL = "https://www.itjobswatch.co.uk/jobs/uk/sqlite.do"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('table', attrs = {'class':'summary'})
table.find('form').decompose()
table_data = table.tbody.find_all("tr")
table = []
for i in table_data:
    row = []
    rrr = i.find_all("td")
    if len(rrr) == 0:
        rrr = i.find_all("th")
    for j in rrr:
        row.append(j.text)
    table.append(row)

hd = table[1]
hd[0] = "index"

df = pd.DataFrame(table)
df.drop(index=[0,1,2,3,4,5,6,7,10,11,14,15],axis=0,inplace=True)
df.columns = hd
df.set_index("index",inplace=True)
df.reset_index(inplace=True)
df['Same period 2021'] = df['Same period 2021'].str.replace('£','')
df['Same period 2021'] = df['Same period 2021'].str.replace(',','')
df['Same period 2021'] = df['Same period 2021'].str.replace('-','0').astype(float)
df['6 months to 19 Dec 2022'] = df['6 months to 19 Dec 2022'].str.replace('£','')
df['6 months to 19 Dec 2022'] = df['6 months to 19 Dec 2022'].str.replace(',','').astype(float)
df['Same period 2020'] = df['Same period 2020'].str.replace('£','')
df['Same period 2020'] = df['Same period 2020'].str.replace(',','').astype(float)

conn = sqlite3.connect("hr")
employees = pd.read_sql_query("select * from employees;", conn)
jobs = pd.read_sql_query("select * from jobs;", conn)



job_titles = jobs['job_title']
job_counts = [len(employees[employees['job_id'] == i]) for i in jobs['job_id']]

percentiles = df
avg_salary = employees['salary'].mean()
year = [2020, 2021, 2022]

fig4 = go.Figure()

fig4.add_trace(go.Scatter(x=year, y=[
                  avg_salary for i in year], name='Average Salary', line=dict(color="#000000")))
for i in percentiles:
        fig4.add_trace(go.Scatter(
            x=year, y=percentiles[i], name=f'{i}th Percentile', line=dict(color="#30f216")))

fig4.show()