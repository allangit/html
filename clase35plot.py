


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Customer Churn Model.txt")
print df.head()
print "\nDibujando con el scatter plot\n"
df.plot(kind="scatter",x="Day Mins", y="Day Charge")

figure,axs=plt.subplots(2,2, sharey=True, sharex=True)
df.plot(kind="scatter",x="Day Mins", y="Day Charge",ax=axs[0][0])
df.plot(kind="scatter",x="Night Mins", y="Night Charge",ax=axs[0][1])
df.plot(kind="scatter",x="Day Calls", y="Day Charge",ax=axs[1][0])
df.plot(kind="scatter",x="Night Calls", y="Night Charge",ax=axs[1][1])


#clase36 histogramas de frecuencias
print "\n\nHistogramas de Frecuencias\n\n"
plt.hist(df["Day Calls"])
plt.show()
