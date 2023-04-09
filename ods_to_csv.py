import pandas as pd

data = pd.read_excel('Labels50.ods', engine='odf')


data.to_csv('Labels50.csv')