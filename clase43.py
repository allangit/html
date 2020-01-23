import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Customer Churn Model.txt")
print df.head()
print df[1:25]
print "\n\n"
print df[10:25]
print "\n\n\n"
print df[330:]

#FILTRADO DE USUARIOS

df2=df[df["Day Mins"]>300]
print df2

#FILTRADOS POR USARIOS DE NY

df3=df[df["State"]=="NY"]
print df3

#CONDICIONES BOOLEANAS: AND OR, NOT

print "\n\nCONDICION USANDO LA SENTENCIA AND--> &\n\n"

df4=df[(df["State"]=="NY") & (df["Day Mins"]>300)]
print df4

print "\n\nUSANDO LA CONDICION DE OR---|\n\n"
df5=df[(df["State"]=="NY") | (df["Day Mins"]>300)]
print df5

print "\n\nESCOGIENDO EL CONJUNTO DE DATOS COMPARANDO ENTRE LAS COLUMNAS\n\n"

df6=df[(df["Day Calls"]) < (df["Night Calls"])]
print df6
print df6.shape

#FILTRADO POR COLUMNA Y FILA

print "FILTRADO POR COLUMNA Y FILA:: SE ESPECIFICA 1 COLUMNA DESPUES LA FILA\n\n"

subset_50=df[["Day Mins","Night Mins","Account Length"]][:50]
print subset_50
print subset_50.shape


#USANDO LAS SENTENCIAS LOC AND ILOC
print "\n\nUSANDO LA SENTENCIA LOC PARA AGRUPAR POR ETIQUETAS\n\n"
print "\n\nUSANDO LA SENTENCIA ILOC PARA SENTENCIAS POR INDICE\n\n"
df7=df.iloc[1:10, 3:6]
print df7
print "\n\nEscojiendo todas las filas y seleccionando de la columna 3 a la 6\n\n"
df8=df.iloc[: ,3:6]
print df8
print "\n\nEscojiendo todas las filas de la 3 a la 6 y seleccionando todas las columnas\n\n"
df9=df.iloc[3:6, :]
print df9
print "\n\nEscojiendo todas las filas y seleccionando las columnas que uno desea\n\n"
df10=df.iloc[:10,[2,4,5,7,8,10]]
print df10
print "\n\nUSANDO LA SENTENCIA LOC PARA AGRUPAR POR ETIQUETAS\n\n"
df11=df.loc[:100, ["Area Code","VMail Plan","Day Mins"]]
print df11

print "\n\nAgregando una columna al Dataset llamada Total Mins\n\n"
df["Total Mins"]=df["Day Mins"]+df["Night Mins"]+df["Eve Mins"]
print df.head()
print "\n\nAgregando una otra columna al Dataset llamada Total Calls\n\n"
df["Total Calls"]=df["Day Calls"]+df["Night Calls"]+df["Eve Calls"]
print df.head()
