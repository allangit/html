
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print "\n\nSimulacion del metodo de montecarlo:\n\n"
print "Generamos 2 numeros aleatorios entre 0 y 1\n"
print "Si valor < 1::Estamos dentro del circulo\n"
print "Si el valor > 1:Estamos fuera del circulo\n\n"

pi_avg=0
n=10000
pi_value_list=[]

for i in range(100):

	value=0
	x=np.random.uniform(0,1,n).tolist()
	y=np.random.uniform(0,1,n).tolist()

	for j in range(n):

		z=np.sqrt(x[j]*x[j]+y[j]*y[j])
		if z<1:

			value +=1

	float_value=float(value)
	pi_value=float_value*4/n
	pi_value_list.append(pi_value)
	pi_avg+=pi_value


pi=pi_avg/100
print pi_value_list;
plt.plot(pi_value_list)
plt.show()





