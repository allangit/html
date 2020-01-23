import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Customer Churn Model.txt")
print df.head()
print "\n\nGENERANDO UNA DISTRIBUCION UNIFORME EN PYTHON\n\n"

a=1
b=100
n=2000
data=np.random.uniform(a,b,n)

plt.hist(data)
plt.xlabel("datos")
plt.ylabel("frecuencia")
plt.show()
