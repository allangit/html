import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("titanic3.csv")
print df[100:150]
print df.shape
print df.columns.values
