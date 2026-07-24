# Conjunto (set): Colección no ordenada de elementos únicos (no se puede accede por índice)

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))
print(len(frutas))

print("Manzana" in frutas)
print("Pera" not in frutas)

# Agregar
# Add
frutas.add("Pera")
print(frutas)

# Update
frutasTropicales = { "Piña", "Mango"} 
frutas.update(frutasTropicales) # Agregar listas, tuplas, conjuntos
print(frutas)

# Eliminarlos
#Remove
frutas.remove("Mango")
print(frutas)
#Discard
frutas.discard("Banana")
print(frutas)
# Pop
frutas.pop()
print(frutas)
# Clear
frutas.clear()
print(frutas)

# conjuntos = {"Python", 156, True}
# print(conjuntos)
# print(type(conjuntos))

# for item in conjuntos:
#     print(item)

print("--------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

c = a.union(b)

print(c)

i = a.intersection(b)

print(i)

d = a.difference(b)

print(d)