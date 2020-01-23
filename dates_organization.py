'platform to organize for pixels collected in the east or north direction'
import pandas as pd
import numpy as np

i = 1
date04 = []
date10 = []
date16 = []

while i < 51:
    
    cena = 'semFiltro ('+ str(i) + ').csv'
    date = pd.read_csv(cena, sep = ";")
    order_platform=tuple(date.head(1))
    lista =np.array(date[order_platform [1]].tolist())
    date04.append(lista[103])
    date10.append(lista[241])
    date16.append(lista[379])
    
    i = i + 1
seriesview =pd.DataFrame()
seriesview['year04'] = date04
seriesview['year10'] = date10
seriesview['year16'] = date16

seriesview.to_csv("seriesview.csv")
