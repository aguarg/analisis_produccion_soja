import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#=========================================
# ÍNIDICE
# 1- EXTRAYENDO LOS DATOS DE LOS CAMPOS
# 2- TRATAMIENTO ESTADÍSTICO DE LOS DATOS
# 3- GRÁFICAS
#=========================================



#========================================================================================================================
# 1- EXTRAYENDO LOS DATOS DE LOS CAMPOS:
# Extraer los datos de todos los campos:
data_soja = pd.read_csv("soja-anual.csv", header=0, sep=",")


# Extraer los datos de la columna produccion_soja:
prod_soja = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["produccion_soja_t"])

# Extraer los datos de la columna Superficie cosechada:
superficie_cosechada = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["superficie_cosechada_soja_ha"])

# Extraer los datos de la columna Superficie sembrada:
superficie_sembrada = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["superficie_sembrada_soja_ha"])

# Extraer los datos de la columna Rendimiento:
rendimiento = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["rendimiento_soja_kgxha"])

# Extraer los datos de la columna tiempo:
tiempo = pd.read_csv("soja-anual.csv", header=0, sep=",", usecols=["indice_tiempo"])






#=========================================================================================================================
# 2- TRATAMIENTO ESTADÍSTICO:










#=========================================================================================================================
# 3- GRÁFICAS:
# Gráfica 1: producción vs tiempo:
plt.subplot(2, 2, 1)
plt.plot(tiempo, prod_soja, color="orange")
plt.title("Producción de soja [tn/año]")
plt.xlabel("Año")
plt.ylabel("Producción [tn]")


# Grafico 2: superficie cosechada vs tiempo:
plt.subplot(2, 2, 2)
plt.plot(tiempo, superficie_cosechada)
plt.title("Superficie cosechada [ha]")
plt.xlabel("Año")
plt.ylabel("Superficie [ha]")


# Gráfico 3: superficie sembrada vs tiempo:
plt.subplot(2, 2, 3)
plt.plot(tiempo, superficie_sembrada, color="green")
plt.title("Superficie sembrada [ha]")
plt.xlabel("Año")
plt.ylabel("Superficie [ha]")


# Gráfico 4: rendimiento vs tiempo:
plt.subplot(2, 2, 4)
plt.plot(tiempo, rendimiento, color="red")
plt.title("Rendimiento")
plt.xlabel("Año")
plt.ylabel("Rendimiento [kg/ha]")



# genera padding vertical entre los subplots para que no queden encimadas:
plt.tight_layout(pad=2.0)




plt.show()