import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


n=10000

df=pd.DataFrame(

	{
		"A":np.random.randn(n),
		"B":1.5+2.5*np.random.randn(n),
		"C":np.random.uniform(5,32,n)

	}
)

data=pd.read_csv("Customer Churn Model.txt")
print data.head()
columns_names=data.columns.values.tolist()
n2=len(columns_names)

df2=pd.DataFrame(

	{
		"columns_list":columns_names,
		"A":np.random.randn(n2),
                "B":1.5+2.5*np.random.randn(n2)
	}
)

print df2

print "\n\nEmpalmes de DataFrames con otros\n\n"

df3=pd.DataFrame(

        {
                "columns_list":columns_names,
                "A":np.random.randn(n2),
                "B":1.5+2.5*np.random.randn(n2) 
        },index=range(42,42+n2)
)

print df3
