# Función: es un bloque de código que solo se ejecuta cuando la llamamos. Permiten organizar y modularizar el código (reutilización)

def saludar(nombre, nacionalidad="Colombia"): # Argumentos
    print("Hola", nombre,"de", nacionalidad)

# saludar("Pedro", "España") # Parámetros
# saludar("María")
# saludar("Ana")

def sumar(a,b):
    return a + b


resultado = sumar(2,3)
print(resultado)

def funcion():
    pass