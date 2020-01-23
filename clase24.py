
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df=pd.read_csv("Customer Churn Model.txt")
print df.head()
print df.columns.values

df2=pd.read_csv("Customer Churn Columns.csv")
print df2.head()


data_cols=df2["Column_Names"].tolist()
print data_cols


