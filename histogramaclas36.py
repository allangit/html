


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df=pd.read_csv("Customer Churn Model.txt")
print df.head()
#clase36 histogramas de frecuencias
print "\n\nHistogramas de Frecuencias\n\n"
plt.hist(df["Day Calls"])
plt.xlabel("Frecuencia")
plt.ylabel("Numero de llamadas")
plt.show()

