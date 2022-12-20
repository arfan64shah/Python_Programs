import pandas as pd
import sqlite3
#everyone has the same here , just change some parts:
conn = sqlite3.connect("hr")
jobs=pd.read_sql_query("select * from jobs;",conn)
jobs = jobs.iloc[1: , :]
jobs["difference"]=jobs['max_salary']-jobs['min_salary']
job=jobs[['job_title','difference']]
max_salary=job['difference'].max()



# first choice:
dcc.RangeSlider(0, max_salary, 1000, value=[0, max_salary],id="input3"),
dcc.Graph(id="output3")
])
@app.callback(

    Output('output3', 'figure'),
    Input('input3', 'value')
)
def update_output(value):
    minimum=value[0]
    maximum=value[-1]
    fig3 = go.Figure()
    fig3["layout"]["xaxis"]["title"] = "Job"
    fig3["layout"]["yaxis"]["title"] = "Difference between max and min"
    t = job[job["difference"]>=minimum][job["difference"]<=maximum]
    fig3.add_trace(go.Bar(x=t['job_title'], y=t['difference'],
    name='Job differences'))
    return fig3
