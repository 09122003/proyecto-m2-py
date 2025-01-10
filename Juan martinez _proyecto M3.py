



import random
import matplotlib.pyplot as plt

def simulacion_galton(num_bolitas, num_baches):
    # Creamos una lista para almacenar el número de bolitas en cada contenedor
    contenedores = [0] * (num_baches + 1)
    
    # Simulamos la caída de cada bolita
    for _ in range(num_bolitas):
        posicion = 0
        for _ in range(num_baches):
            # La bolita puede caer a la izquierda o a la derecha (aleatorio)
            if random.random() < 0.5:
                posicion += 1
        contenedores[posicion] += 1
    
    return contenedores

def graficar_histograma(contenedores):
    # Graficamos el histograma de los contenedores
    plt.bar(range(len(contenedores)), contenedores, width=0.8, color='skyblue', edgecolor='black')
    plt.xlabel('Contenedores')
    plt.ylabel('Número de bolitas')
    plt.title('Simulación de la máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_bolitas = 3000  # Número de bolitas a simular
num_baches = 12     # Número de baches en la máquina de Galton

# Ejecutar la simulación
contenedores = simulacion_galton(num_bolitas, num_baches)

# Graficar los resultados
graficar_histograma(contenedores)
