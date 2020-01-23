

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("titanic3.csv")
print df["sex"].head()

dummy_sex=pd.get_dummies(df["sex"],prefix="sex")
print dummy_sex.head()
columns_name=df.columns.values
print columns_name
df2=df.drop(["sex"],axis=1)
print df2.head()
print df2.columns.values
df3=pd.concat([df2,dummy_sex],axis=1)
print df3.head()


def create_dummy(df,var_name):

	dummy=pd.get_dummies(df[var_name],prefix=var_name)
	print dummy.head()
	columns_name=df.columns.values
	print columns_name
	df2=df.drop([var_name],axis=1)
	print df2.head()
	print df2.columns.values
	df3=pd.concat([df2,dummy],axis=1)
	return df3[:200]

print "\n\nIMPRIMIENDO LOS RESULTADOS DE LAS VARIABLES DUMMY\n\n"
print create_dummy(df,"body")
