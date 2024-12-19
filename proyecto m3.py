


import random
import matplotlib.pyplot as plt 

# Función para simular la caída de las canicas
def simulacion_galton(num_canicas, num_niveles):
    # Creamos una lista para contar cuántas canicas caen en cada contenedor
    contenedores = [0] * (num_niveles + 1)
    
    # Simulamos la caída de cada canica
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            # Cada canica decide si va a la izquierda o a la derecha (50% de probabilidad)
            if random.random() < 0.5:
                posicion += 1
        contenedores[posicion] += 1
    
    return contenedores

# Función para graficar el histograma
def graficar_histograma(contenedores):
    # Graficamos el histograma de los contenedores
    plt.bar(range(len(contenedores)), contenedores, width=0.8, color='skyblue', edgecolor='black')
    plt.xlabel('Contenedores')
    plt.ylabel('Número de Canicas')
    plt.title('Simulación de la máquina de Galton (3000 Canicas, 12 Niveles)')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000  # Número de canicas
num_niveles = 12    # Número de niveles de obstáculos

# Ejecutamos la simulación
contenedores = simulacion_galton(num_canicas, num_niveles)

# Graficamos el histograma
graficar_histograma(contenedores)
