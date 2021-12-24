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
# hacer que los resultados se guarden en un archivo de texto.
# Ver si se puede presentar como una tabla linda. Pandas o numpy pueden hacer eso
# Lo mismo con el archivo generado. Si es en PDF se puede dar un formato mejor.
# Ver si conviene hacerlo con quo


# Número total de datos
tamano_dataframe = data_soja.size
print("Tamaño del dataframe: " + str(tamano_dataframe))



# Medias:
prod_soja_promedio = np.mean(prod_soja)
superficie_cosechada_promedio = np.mean(superficie_cosechada)
superficie_sembrada_promedio = np.mean(superficie_sembrada)
rendimiento_promedio = np.mean(rendimiento)


# Desvío estándar
std_prod_soja = np.std(prod_soja)
std_superficie_cosechada = np.std(superficie_cosechada)
std_superficie_sembrada = np.std(superficie_sembrada)
std_rendimiento = np.std(rendimiento)


# Valor mínimo
min_prod_soja = np.min(prod_soja)
min_superficie_cosechada = np.min(superficie_cosechada)
min_superficie_sembrada = np.min(superficie_sembrada)
min_rendimiento = np.min(rendimiento)

# Valor máximo
max_prod_soja = np.max(prod_soja)
max_superficie_cosechada = np.max(superficie_cosechada)
max_superficie_sembrada = np.max(superficie_sembrada)
max_rendimiento = np.max(rendimiento)

# Percentiles

# 25%

# 50%

# 75%









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



plt.suptitle("Producción argentina de soja, período 1969-2019")
plt.show()