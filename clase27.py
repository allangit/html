

import pandas as pd
import numpy as np
import matplotlib.pyplot
import csv
import urllib2


#leer datos url externa clase28

medals_url="http://winterolympicsmedals.com/medals.csv"

df=pd.read_csv(medals_url)
print df.head()

df2=urllib2.urlopen(medals_url)
print df2.read()


df3=csv.reader(df2)

print df3
