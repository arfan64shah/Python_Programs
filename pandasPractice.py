import pandas as pd   #Importar o modulo pandas, Nao esquece de installar o modulo
import numpy as np
#Note pd.Series  has a capital S 

serie1=pd.Series([6,2,3,4,5,6])   #Series from a list

print(serie1)
print(type(serie1)) #Check the type to understand the difference

horas=[2,3,1,7,4,5,6]  # From a list but with index that we want
serie2=pd.Series(horas,index=["Segunda","terca","quarta","quinta","sexta","Sabado","Domingo"])
print(serie2)

horas=[2,3,1,7,4,5,6]
indice=["Segunda","terca","quarta","quinta","sexta","Sabado","Domingo"]
serie2=pd.Series(horas,index=indice)
print(serie2)

dicio = {'Mon': 33, 'Tue': 19, 'Wed': 15, 'Thu': 89, 'Fri': 11, 'Sat': 9,"Sun":10}
serie3=pd.Series(dicio)
print(serie3)

dados=np.random.randint(10,50,5)   # array from numpy
indice=["um","dois","tres","quatro","cinco"]
serie4=pd.Series(dados,index=indice)
print(serie4)