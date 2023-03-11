import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/USER/Desktop/DATA & ANALYTICS/1.1 PROYECTO 1/datos_seguros.csv',sep=";")
#print(df)
DF=pd.DataFrame(df)
print(DF.head())
print(DF.shape)
print(DF.size)
print(DF.columns[:])

print(DF.iloc[0:10,:]) 
print(DF.iloc[-10:,:]) 
print(DF.isna(). sum(). sum()) #Nos permite saber la cantidad de datos nuos en todas las columnas

L=df.iloc[0:1000+1, :]
print(L)


