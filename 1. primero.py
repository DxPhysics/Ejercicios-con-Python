import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/USER/Desktop/DATA & ANALYTICS/1.1 PROYECTO 1/Avocado_Sales/Avocado.csv',sep=",")

DF=pd.DataFrame(df)
#with pd.option_context("display.min_rows", 1, "display.max_rows", 700, "display.max_columns", 1, 'display.max_colwidth', 14):
#print(DF.head()) #imprime o muestra los primeros 5 filas y columnas por defecto
#print(DF.shape) # Nos indica las dimensiones del DataFrame
#print(DF.size)

#print('Las ventas de los últimos 5 días son:', DF.tail()) #No colocar

L=DF.sort_values(by=['Date'])
print(L)

#print(DF.columns.get_indexer(['region'])) #Esto nos permite saber el index de alguna COLUMNA de un DataFrame


print(DF.pivot_table(index = ['region'], aggfunc ='size'))  #nos muestra cuantas veces se repite cada valor o elemento de una columna 'region'
print(DF['region'].value_counts()['Albany']) #nos muestra cuantas veces se repite un valor en especifico ('Albany')de una columna 'region'


# with pd.option_context("display.min_rows", 1, "display.max_rows", 27324, "display.max_columns", 1, 'display.max_colwidth', 14): #esto nos permite mostrar un intervalo de filas y columnas

print(DF.pivot_table(index = ['Date'], aggfunc ='size')) #nos muestra cuantas veces se repite cada valor o elemento de una columna 'Date'
#print(DF['Date'].value_counts()['2019-12-01']) #nos muestra cuantas veces se repite un valor en especifico ('2019-12-01')de una columna 'Date'
#print(DF.loc[DF['Date'] == '2019-11-03'].index[0]) #Nos da el index de algún valor en específico de alguna fila (como se repite nos muestra el que aparece por primera vez de forma ascendente)  

print (DF.loc[(DF['Date'] == '2019-11-03') & (DF['region'] =='Albany')])
print (DF.loc[(DF['Date'] == '2019-11-10') & (DF['region'] =='Albany')])
print (DF.loc[(DF['Date'] == '2019-11-17') & (DF['region'] =='Albany')])
print (DF.loc[(DF['Date'] == '2019-11-24') & (DF['region'] =='Albany')])
print (DF.loc[(DF['Date'] == '2019-12-01') & (DF['region'] =='Albany')])


Ventas=[DF.iloc[248,2],DF.iloc[249,2],DF.iloc[250,2],DF.iloc[251,2],DF.iloc[252,2]]
Dias=['2019-11-03','2019-11-10' ,'2019-11-17' ,'2019-11-24' ,'2019-12-01']
N_de_Unidades=[15055.38,14787.0,13310.0,14415.0,15065.0]
Precio_Unitario=[1.16,1.14,1.11,1.16,1.15]

DF1=pd.DataFrame({'Producto':['Palta convencional','Palta convencional','Palta convencional','Palta convencional','Palta convencional'],
    '            Ventas_Totales':Ventas,
                        'Fechas':Dias,
                        'N_de_Unidades':N_de_Unidades,
                        'Precio_Unitario':Precio_Unitario
                        })
print(DF1)
# desc=((DF1[Precio_Unitario])*(5)/(100))

# CAL= [i-(desc) for i in Precio_Unitario]
# print(CAL)

#print(DF.iloc[248:252+1,-540])
#print(df.columns.get_indexer(['region']))
