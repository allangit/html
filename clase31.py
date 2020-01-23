


#MANIPULACION DE DATOS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("titanic3.csv")
print df.head(20)
print "Describiendo la forma del dataset columna y fila\n\n"
print df.shape
print "\nDescriendo las variables categoricas\n\n"
print df.columns.values
print "\nImpriendo los ultimos valores\n\n"
print df.tail()
print "\n\n"
print df.describe()
print "\n\nDescriendo la forma de las variables si float int etc"
print df.dtypes
print "\n\nImprimiendo los valores desconocidos de cierta columna del dataset\n\n"

print pd.isnull(df["body"])

#BORRADO DE VALORES
#axis=0 borra fila
#axis=1 borra columna

print "\n\nBorra la fila si todas las columnas tienen valores na\n\n"
print df.dropna(axis=0, how="all")
print "\nBorra si alguna de las colmunas tienen alguin valor NaN\n"
df2=df.dropna(axis=0, how="any")
print df2
print "\n\nComputo de valores faltantes\n\n"
df3=df.fillna(0)
print df3
print "\n\nSegundo metodo para tratar los valores NaN\n\n"
df4=df.fillna("desconocido")
print df4
print "\n\nTambien se pueden aplicar a columnas especificas la limpieza de datos\n"
df5=df["body"].fillna(0)
print df5
df6=df["home.dest"].fillna(0)
print df6.tail()
df7=df["age"].fillna(df["age"].mean())
print "\n\n Los valores promedios de las edades son las siguientes\n\n"
print df7

