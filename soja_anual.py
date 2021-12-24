import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import quo

#=========================================
# ÍNIDICE
# 1- EXTRAYENDO LOS DATOS 
# 2- TRATAMIENTO ESTADÍSTICO DE LOS DATOS
# 3- GRÁFICAS
# 4- IMPRIMIR DATOS EN LA CONSOLA
# 5- VOLCANDO LOS DATOS A UN ARCHIVO DE TEXTO
#=========================================



#========================================================================================================================
# 1- EXTRAYENDO LOS DATOS:
# Extraer los datos de todo el dataset:
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
# Ver si se puede presentar como una tabla linda. Pandas o numpy pueden hacer eso
# Lo mismo con el archivo generado. Si es en PDF se puede dar un formato mejor.
# Ver si conviene hacerlo con quo


# Número total de datos
tamano_dataframe = data_soja.size


# Medias:
prod_soja_promedio = np.mean(prod_soja)
superficie_cosechada_promedio = np.mean(superficie_cosechada)
superficie_sembrada_promedio = np.mean(superficie_sembrada)
rendimiento_promedio = np.mean(rendimiento)


# Desvío estándar:
std_prod_soja = np.std(prod_soja)
std_superficie_cosechada = np.std(superficie_cosechada)
std_superficie_sembrada = np.std(superficie_sembrada)
std_rendimiento = np.std(rendimiento)


# Valor mínimo:
min_prod_soja = np.min(prod_soja)
min_superficie_cosechada = np.min(superficie_cosechada)
min_superficie_sembrada = np.min(superficie_sembrada)
min_rendimiento = np.min(rendimiento)

# Valor máximo:
max_prod_soja = np.max(prod_soja)
max_superficie_cosechada = np.max(superficie_cosechada)
max_superficie_sembrada = np.max(superficie_sembrada)
max_rendimiento = np.max(rendimiento)



# Percentiles:
# 25%
percentil25_prod_soja = np.percentile(prod_soja, 25)
percentil25_superficie_cosechada = np.percentile(superficie_cosechada, 25)
percentil25_superficie_sembrada = np.percentile(superficie_sembrada, 25)
percentil25_rendimiento = np.percentile(rendimiento, 25)

# 50%
percentil50_prod_soja = np.percentile(prod_soja, 50)
percentil50_superficie_cosechada = np.percentile(superficie_cosechada, 50)
percentil50_superficie_sembrada = np.percentile(superficie_sembrada, 50)
percentil50_rendimiento = np.percentile(rendimiento, 50)

# 75%
percentil75_prod_soja = np.percentile(prod_soja, 75)
percentil75_superficie_cosechada = np.percentile(superficie_cosechada, 75)
percentil75_superficie_sembrada = np.percentile(superficie_sembrada, 75)
percentil75_rendimiento = np.percentile(rendimiento, 75)








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
plt.tight_layout(pad=1.5)


plt.suptitle("Producción argentina de soja, rendimiento y superficie destinada. Período 1969-2019")


# El plt.show() que muestra el gráfico se puso mas abajo para que se muestre después de la tabla.





#=====================================================================================================================
# 4- IMPRIMIR DATOS EN LA CONSOLA

# Tabla

tabla = [
     ["Dato", "Producción", "Sup. cosechada", "Sup. sembrada", "Rendimiento"],
     ["Media", int(prod_soja_promedio), int(superficie_cosechada_promedio), int(superficie_sembrada_promedio), int(rendimiento_promedio)],
     ["Desvío estándar", int(std_prod_soja), int(std_superficie_cosechada), int(std_superficie_sembrada), int(std_rendimiento)],
     ["Máximo", int(max_prod_soja), int(max_superficie_cosechada), int(max_superficie_sembrada), int(max_rendimiento)],
     ["Mínimo", int(min_prod_soja), int(min_superficie_cosechada), int(min_superficie_sembrada), int(min_rendimiento)],
     ["Percentil 25", int(percentil25_prod_soja), int(percentil25_superficie_cosechada), int(percentil25_superficie_sembrada), int(percentil25_rendimiento)],
     ["Percentil 50", int(percentil50_prod_soja), int(percentil50_superficie_cosechada), int(percentil50_superficie_sembrada), int(percentil50_rendimiento)],
     ["Percentil 75", int(percentil75_prod_soja), int(percentil75_superficie_cosechada), int(percentil75_superficie_sembrada), int(percentil75_rendimiento)],
   ]

print()
quo.echo(f"RESULTADOS DEL ANÁLISIS ESTADÍSTICO", fg="red", bold=True)
quo.echo(quo.tabular(tabla))


# Imprimo la gráfica acá para que aparezca después de la tabla:
plt.show()




#===============================================================================================================================
# 5- VOLCANDO LOS DATOS A UN ARCHIVO DE TEXTO:
f = open("datos.txt", "w")
f.write("RESULTADO DEL ANÁLISIS ESTADÍSTICO:")
f.write(str(pd.DataFrame(tabla)))
f.close()

# me llena el txt de 1 y 0 en la parte de arriba. Ver como sacarlos y como centrar los datos.





