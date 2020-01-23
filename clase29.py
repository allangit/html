



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


titanic2=pd.read_excel("titanic3.xls", "titanic3")
print titanic2.head()
titanic2.to_csv("alan.csv")
titanic2.to_excel("alan.xls")
titanic2.to_json("alan.json")
