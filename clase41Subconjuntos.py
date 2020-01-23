





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Customer Churn Model.txt")
print df.head()

account_length=df["Account Length"]

print type(account_length)
Account_length2=df[["Account Length", "Phone", "Eve Charge", "Day Calls"]]
print Account_length2.head()

desired_columns=["Account Length", "Phone", "Eve Charge", "Day Calls"]
df2=df[desired_columns]
print df2.head()

#BORRADO DE COLUMNAS


desired_columns=["Account Length","Vmail Message","Day Calls"]
print desired_columns
print "\n\n"
all_columns_list=df.columns.values.tolist()
print all_columns_list

print "\n\nObteniendo las columnas complementarias del dataset\n"

sublist=[x for x in all_columns_list if x not in desired_columns]
print sublist
print "\n\n\nImprimiendo el dataset con las columnas faltantes"
df3=df[sublist]
print df3.head()


