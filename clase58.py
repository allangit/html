import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



df=pd.read_csv("Customer Churn Model.txt")
print df.shape
n=len(df)

a=np.random.randn(n)

check=(a<=0.8)
training=df[check]
testing=df[~check]
print len(training), len(testing)

print "\n\nDesarrollando con la biblioteca sklearn train_test_split\n\n"

train,test=train_test_split(df, test_size=0.2)
print len(train), len(test)

