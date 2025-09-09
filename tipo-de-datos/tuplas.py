# Tupla: Colección ordenada e inmutable de elementos que permiten duplicados

# Indice         0           1           2      3
tecnologias = ("Python", "Javascript", "Go", "Python")

print(tecnologias)
print(tecnologias[1])

print(len(tecnologias))

print(type(tecnologias))

fruta = ("Manzana",)

print(type(fruta))

tupla = ("Python", 5, True)

print(tupla)
print(type(tupla))

x, y, z = tupla
print(x)
print(y)
print(z)

tupla1 = (1,2,3)
tupla2 = (3,4,5)
tupla3 = tupla1 + tupla2

print(tupla3)

tupla = ("Python", 5, True)

print(tupla * 2)

for item in tupla:
    print(item)

print("---------------")

tuplaAModificar = ("Python", "Javascript", "Go")
listaComodin = list(tuplaAModificar)
listaComodin.append("ReactJS")
tuplaAModificar = tuple(listaComodin)

print(tuplaAModificar)