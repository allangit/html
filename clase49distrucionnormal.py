import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=np.random.randn(100)
x=range(1,101)
plt.xlabel("Datos:: Muestra")
plt.ylabel("Frencuencia::Magnitud(mA)")
plt.title("Corriente vs Cantidad de Muestra")
#plt.plot(x,data)
plt.hist(data)
plt.show()

