import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

red_wine=pd.read_csv("winequality-red.csv", sep=";")
white_wine=pd.read_csv("winequality-white.csv",sep=";")
print red_wine.head()
print red_wine.shape
print "\n\nImprimiendo los datos del vino blanco\n\n"
print white_wine.head()
print white_wine.shape
print "\n\nAxis=0 imprime de horizontal, Axis=1 imprime de manera vertical\n\n"
wine_data=pd.concat([red_wine,white_wine],axis=0)
print wine_data.shape
print wine_data.head()
print "\n\nMaking the dataset with scrambel functions\n\n"
data1=wine_data.head(10)
data2=wine_data[300:310]
data3=wine_data[400:410]
data_scrambel=pd.concat([data1,data2],axis=0)
print data_scrambel

