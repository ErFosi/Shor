import itertools
import math

# Vectores en el retícula
v1 = (2, 0, 0)  # Puedes ajustar la cantidad de dimensiones y sus valores
v2 = (0, 1, 0)  # Puedes ajustar la cantidad de dimensiones y sus valores
num_dimensions = len(v1)  # La cantidad de dimensiones es la longitud de los vectores

# Genera una lista de todos los puntos que son combinaciones lineales de v1 y v2
lattice = [tuple(tuple(x * v1[i] + y * v2[i] for i in range(num_dimensions)) for x, y in itertools.product(range(5), repeat=2))]

# Función para calcular el ángulo entre dos vectores
def angle_between_vectors(v1, v2):
    dot_product = sum(x * y for x, y in zip(v1, v2))
    norm_v1 = math.sqrt(sum(x ** 2 for x in v1))
    norm_v2 = math.sqrt(sum(y ** 2 for y in v2))
    try:
        cosine_similarity = dot_product / (norm_v1 * norm_v2)
    except:
        print("Angulo 0?")
        return(100)
    angle = math.acos(cosine_similarity)
    return math.degrees(angle)

# Buscar dos vectores casi paralelos
closest_angle = float('inf')
v1_result = None
v2_result = None

for vector1, vector2 in itertools.combinations(lattice, 2):
    angle = angle_between_vectors(vector1, vector2)
    if angle < closest_angle:
        v1_result = vector1
        v2_result = vector2
        closest_angle = angle

print("Dos vectores casi paralelos encontrados:")
print("Vector 1:", v1_result)
print("Vector 2:", v2_result)
