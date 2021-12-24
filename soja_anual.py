import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data_soja = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=['indice_tiempo', 'superficie_cosechada_soja_ha'])

# EXTRAYENDO LOS DATOS DE LOS CAMPOS:
# Extraer los datos de la columna produccion_soja:
prod_soja = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["produccion_soja_t"])

# Superficie cosechada:
superficie_cosechada = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["superficie_cosechada_soja_ha"])

# Superficie sembrada:
superficie_sembrada = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["superficie_sembrada_soja_ha"])

# Rendimiento:
rendimiento = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["rendimiento_soja_kgxha"])

# Extraer los datos de la columna tiempo:
tiempo = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["indice_tiempo"])





# GRÁFICAS:
# Gráfica 1: producción vs tiempo:
plt.subplot(2, 1, 1)
plt.plot(tiempo, prod_soja)
plt.title("Producción de soja")
plt.xlabel("Año")
plt.ylabel("Producción [tn]")


# Grafico 2: superficie cosechada vs tiempo:
plt.subplot(2, 1, 2)
plt.plot(tiempo, superficie_cosechada)
plt.title("Superficie cosechada")
plt.xlabel("Año")
plt.ylabel("Superficie [ha]")


# genera espacio vertical entre los subplots para que no queden encimadas:
plt.tight_layout(h_pad=2.0) 



plt.show()