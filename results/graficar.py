import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('resultados_all.csv')

# Filtrar los datos por algoritmo
algoritmos = df['Algoritmo'].unique()

# Crear una gráfica para cada algoritmo
for algoritmo in algoritmos:
    # Filtrar y ordenar los datos para el algoritmo actual
    datos_algoritmo = df[df['Algoritmo'] == algoritmo].sort_values(by='N')
    datos_algoritmo = df[df['Algoritmo'] == algoritmo]
    plt.plot(datos_algoritmo['N'], datos_algoritmo['Tiempo (segundos)'], label=algoritmo)

# Añadir detalles a la gráfica
plt.xlabel('Número N')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de Tiempos de Ejecución por Algoritmo')
plt.legend()
plt.grid(True)
plt.show()