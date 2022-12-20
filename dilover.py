import pandas as pd
import numpy as np
import bs4
import requests
import sqlite3
from time import time
from unicodedata import name
from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime

app = Dash(__name__)
con = sqlite3.connect("hr")
df = pd.read_sql_query('select * from jobs;', con)
employees = pd.read_sql_query("select * from employees;", con)
jobs = pd.read_sql_query("select * from jobs;", con)


job_titles = jobs['job_title']
job_counts = [len(employees[employees['job_id'] == i]) for i in jobs['job_id']]


def getPercentiles():
    """Return a dictionary with percentiles from website"""

    result = {10: [],
              25: [],
              75: [],
              90: []}


    url = 'https://www.itjobswatch.co.uk/jobs/uk/sqlite.do'
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')


    table = soup.find('table', class_='summary')
    rows = table.find_all('tr')
    for i in rows:
        if "<td>10<sup>th</sup> Percentile</td>" in str(i):
            for b in i.find_all('td', class_='fig'):
                if str(b.text[1:]) != "":
                    result[10].append(int(b.text[1:].replace(",", "")))
                else:
                    result[10].append(None)
        if "<td>25<sup>th</sup> Percentile</td>" in str(i):
            for b in i.find_all('td', class_='fig'):
                if str(b.text[1:]) != "":
                    result[25].append(int(b.text[1:].replace(",", "")))
                else:
                    result[25].append(None)
        if "<td>75<sup>th</sup> Percentile</td>" in str(i):
            for b in i.find_all('td', class_='fig'):
                if str(b.text[1:]) != "":
                    result[75].append(int(b.text[1:].replace(",", "")))
                else:
                    result[75].append(None)
        if "<td>90<sup>th</sup> Percentile</td>" in str(i):
            for b in i.find_all('td', class_='fig'):
                if str(b.text[1:]) != "":
                    result[90].append(int(b.text[1:].replace(",", "")))
                else:
                    result[90].append(None)


    return result


def part_a():
    fig = px.bar(x=job_titles, y=job_counts)
    fig.update_layout(
        title="Count of Jobs",
        xaxis_title="Names",
        yaxis_title="Counts",
        legend_title="Job Title",
        xaxis=dict(
            tickmode='array',
            tickvals=[i for i in range(len(job_titles))],
            ticktext=job_titles,
            tickangle=90
        )
    )


    return fig


def part_c():
    percentiles = getPercentiles()
    avg_salary = employees['salary'].mean()
    year = [2020, 2021, 2022]


    fig = go.Figure()


    fig.add_trace(go.Scatter(x=year, y=[
                  avg_salary for i in year], name='Average Salary', line=dict(color="#000000")))


    for i in percentiles:
        fig.add_trace(go.Scatter(
            x=year, y=percentiles[i], name=f'{i}th Percentile', line=dict(color="#30f216")))


    return fig


app.layout = html.Div([
    html.H1("Final Exam", style={'text-align': 'center', "color": "white",
            "font-weight": "bold", "font-size": "48px"}, className="topName"),


    html.Div([


        html.P("AAAAAAAAAAAAA",
               style={'text-align': 'left', "padding": "10px", "font-size": "30px"}),


        html.Div(children=[
            dcc.Dropdown(
                options=job_titles,
                value='all',
                id="input1",
                multi=True),
        ],
            className="dropdown1"),

        dcc.Graph(id="output1",
                  figure=part_c()),

    ], className="mainDiv")
])


if __name__ == '__main__':
    app.run_server(debug=True)