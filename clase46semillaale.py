import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Customer Churn Model.txt")
print df.head()


#ESTABLECIENDO UNA SEMILLA ALEATORIA
print "\n\nEl establecer una semilla aleatoria es buena para la reproductibilidad del experimento\n\n"
np.random.seed(2020)

for i in range(5):

	print np.random.random()


#QUITANDO LA SEMILLA ALEATORIA
print "\nCUANDO SE QUITA LA SEMILLA ALEATORIA NO SE TIENE LA REPRODUCTIBILIDAD DEL EXPERIMENTON\n"

