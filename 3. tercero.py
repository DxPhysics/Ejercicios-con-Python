import pandas as pd
import numpy as np
#d = {
    #'Mes':['Enero','Febrero','Marzo','Abril','Mayo'],
    #'Ventas':[30500,35600,28300,33900,42500],
    #'Gastos':[22000,23450,18100,35700,32450],
#df=pd.DataFrame(d)         #tmb se puede partir de una diccionario y convertirlo a DataFrame

df = pd.DataFrame({'Mes':['Enero','Febrero','Marzo','Abril','Mayo'],
    'Ventas':[30500,35600,28300,33900,42500],
    'Gastos':[22000,23450,18100,35700,32450]})
#print(df.to_string(index=False)) #para ocultar index en las filas
#print(df) #muestra el DataFrame con los datos ingresados

df['Columna 1']= round(((df['Gastos'])/(df['Ventas']))*100,3)
#print(df) # muestra la nueva columna añadida con el cálculo pedido

df['Columna 2']=['Meta superada'if i >=30000 else 'Meta No Superada'for i in df['Ventas']]

#df['Columna 3']=[df['Gastos']-(df['Gastos']) if df['Gastos']>df['Ventas'] else 'np.nan' for i in df['Ventas'] or df['Gastos']]
def f(row):
    if row['Gastos']>row['Ventas']:
     return  row['Gastos']-row['Ventas']
    else:
     return  np.nan
    
df['Columna 3'] = df.apply(f,axis=1)
print('-'*70)
print(df)
#print(df.loc[df['Mes'] == 'Febrero'].index[0])  #Esto nos permite saber el index de algún valor en un DataFrame
V=df.iloc[2:5, 1].sum()
G=df.iloc[1:4, 2].sum()
print('-'*70)
print('-Total de ventas de los últimos 3 meses:',V)
print('-Total de gastos de Febrero a Abril:',G)
print('-'*70)
