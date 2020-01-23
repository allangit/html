import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Customer Churn Model.txt")
print df.head()

print "\n\nGenera numeros Aleatorios entre 1-100\n\n"
number=np.random.randint(1,100)
print number
print "\n\nGenera numeros Aleatorios entre 0-1\n\n"
number2=np.random.random()
print number2

def  rand_int(n,a,b):

	x=[]
	for i in range(n):

		x.append(np.random.randint(a,b))
	return x

print rand_int(100,1,20)

