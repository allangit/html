




# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib2

response = pd.read_html("http://radiografia.conare.ac.cr/indicadores-de-empleo")

print response[0]
print response[0].columns.values
print response[0].describe()
print response[0][['Disciplina','% *Desempleo']]


#url="https://www.uned.ac.cr/ejecutiva/dependencias/direccion-financiera/oficina-de-tesoreria/aranceles/asignaturas-cuatrimestrales"

#response2=pd.read_html(url)
#print "\n\nImprimiendo los datos de la pagina web de la uned\n\n"
#print response2[0]
#print response2[0].columns.values

