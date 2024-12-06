
print ("            Longitud de una frase                          ")



# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Obtener la longitud de la palabra
longitud = len(palabra)

# Verificar las condiciones de la longitud de la palabra
if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")
  


print("ejercicio 2")


# Función para determinar el cuadrante de un punto
def identificar_cuadrante(x, y):
    if x == 0 or y == 0:
        return "Las coordenadas no deben ser 0"
    elif x > 0 and y > 0:
        return "El punto se encuentra en el cuadrante I"
    elif x < 0 and y > 0:
        return "El punto se encuentra en el cuadrante II"
    elif x < 0 and y < 0:  
        return "El punto se encuentra en el cuadrante III"
    elif x > 0 and y < 0:
        return "El punto se encuentra en el cuadrante IV"

# Entrada de las coordenadas
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

# Verificar el cuadrante
resultado = identificar_cuadrante(x, y)
print(resultado)

