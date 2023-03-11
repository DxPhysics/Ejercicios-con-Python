import pandas as pd

def f(dicc):

    ingresos_en_S= pd.Series(dicc)

    min= ingresos_en_S.min()
    max= ingresos_en_S.max()
    med= ingresos_en_S.mean()

    return pd.Series([min, max, med])

IM= {"Luis": 14000, "Roberto": 11000, "Dania": 18000, "Carlos": 8000, "Estefano": 2000,"Pedro":40000,"Angel":7000}

print(round(f(IM)))