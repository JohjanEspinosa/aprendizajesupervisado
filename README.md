# aprendizajesupervisado
Descripción del código

1. Importación de bibliotecas:
* Se importan las bibliotecas necesarias para manejar datos (pandas), dividir el dataset (train_test_split), crear el modelo de regresión (LinearRegression), y calcular el error (mean_squared_error).
  
2. Creación del dataset:
* Se define un diccionario con datos ficticios sobre rutas, distancias, tiempos estimados y pasajeros promedio.
* Se convierte este diccionario en un DataFrame de pandas y se guarda como un archivo CSV llamado dataset_transporte_masivo.csv.

3. Carga del dataset:
* Se carga el dataset desde el archivo CSV para ser utilizado en el modelo.
  
4. Definición de características y variable objetivo:

* Se seleccionan las características (distancia y pasajeros promedio) y la variable objetivo (tiempo estimado) para el modelo.
  
5. División de datos:
* Se divide el dataset en conjuntos de entrenamiento y prueba, utilizando el 20% de los datos para pruebas.
  
6. Inicialización y ajuste del modelo:
*Se crea una instancia del modelo de regresión lineal y se entrena utilizando los datos de entrenamiento.

7. Predicciones:
* Se realizan predicciones sobre el conjunto de prueba.

8. Cálculo del error:

* Se calcula el error cuadrático medio (MSE) para evaluar la precisión del modelo.

9. Resultados:
* Se imprime el error cuadrático medio obtenido, lo que indica qué tan bien se está desempeñando el modelo.
