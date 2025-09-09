# LISTAS: Las listas son ordenadas, modificables y permiten valores duplicados

# Índices:   0          1           2            3
# frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
# print(frutas)
# print(type(frutas))

# frutas[1] = "Banana"

# print(frutas[1])
# print(frutas)

# lista = ["Sergie Code", 5, True]
# print(lista)
# print(type(lista))

# print(len(lista))
# print(len(frutas))

# print(frutas[1:])

# if "Manzana" in frutas:
#     print("La manzana está dentro de las frutas")

# Indices      0        1       2
vehiculos = ["Auto", "Moto", "Avión"]

# Métodos 
# Append (agregar un elemento al final de la lista)
vehiculos.append("Barco") # Indice 3
print(vehiculos)

# Insert 
vehiculos.insert(1, "Bicicleta")
print(vehiculos)

# Remove
vehiculos.remove("Auto")
print(vehiculos)

# Pop
vehiculos.pop(1)
print(vehiculos)

# Sort
vehiculos.sort()
print(vehiculos)

# Reverse
vehiculos.reverse()
print(vehiculos)

# Unir listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)