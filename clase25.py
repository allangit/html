

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=open("Customer Churn Model.csv","r")
cols=df.readline().strip().split(",")
ncols=len(cols)
print cols
print ncols

#construyendo diccionario

counter=0
main_dict={}

for col in cols:

	main_dict[col]=[]

print main_dict

for line in df:

	values=line.strip().split(",")
	for i in range(ncols):

		main_dict[cols[i]].append(values[i])

	counter+=1

print counter,ncols



df3=pd.DataFrame(main_dict)

print df3.head()
print df3.columns.values


