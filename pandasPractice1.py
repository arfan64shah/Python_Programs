import pandas as pd   #Import the module pandas, of course you have installed it
import numpy as np
import requests  #this library is for downloading from internet
#Please note that the pd.DataFrame  has a capital D  and a capital F 

#create a dataframe from lists
df1=pd.DataFrame([[1,2,3,4,5,"blabla"],[32,11,45,23],[None,None,15,32.5]])   #criar um objeto dtaframe a partir duma listas
# Any missing data is replaced by Nan 
print(df1)