# Importar bibliotecas necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Paso 1: Crear un dataset de ejemplo
data = {
    'Ruta': ['A-B', 'A-C', 'B-D', 'B-E', 'C-F', 'E-F'],
    'Distancia_km': [5, 10, 4, 6, 7, 3],
    'Tiempo_estimado_min': [15, 30, 10, 20, 25, 8],
    'Pasajeros_promedio': [100, 150, 50, 80, 120, 40]
}

# Convertir a DataFrame
df_transporte = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df_transporte.to_csv('dataset_transporte_masivo.csv', index=False)

# Mostrar el DataFrame
print("Dataset creado:")
print(df_transporte)

# Paso 2: Cargar el dataset
df = pd.read_csv('dataset_transporte_masivo.csv')

# Paso 3: Definir las características (X) y la variable objetivo (y)
X = df[['Distancia_km', 'Pasajeros_promedio']]
y = df['Tiempo_estimado_min']

# Paso 4: Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 5: Inicializar el modelo de regresión lineal
modelo = LinearRegression()

# Paso 6: Ajustar el modelo a los datos de entrenamiento
modelo.fit(X_train, y_train)

# Paso 7: Hacer predicciones sobre los datos de prueba
y_pred = modelo.predict(X_test)

# Paso 8: Calcular el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)

# Paso 9: Imprimir resultados
print(f'Error cuadrático medio: {mse:.2f}')
