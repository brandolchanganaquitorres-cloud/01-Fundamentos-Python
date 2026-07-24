# Coleccion de pares clave calor (Ordenado a partir de Python 3.7)

auto = {
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}

print(auto)
print(auto["marca"])
print(auto.get("marca"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("Marca es una de las propiedades de este diccionario")

auto["año"] = 2020
print(auto)

auto["color"] = "Verde"
print(auto)

auto.update({"año": 2022, "puertas": 4})
print(auto)

# auto.pop("puertas")
# print(auto)

# auto.popitem()
# print(auto)

# auto.clear()
# print(auto)

for k in auto: # keys
    print(k)

print("---")
for v in auto.values(): # values
    print(v)

print("---")

for k,v in auto.items(): # keys, value
    print(k,v)

# Diccionarios Anidados

familia = {
    "hijo1" : {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2" : {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3" : {
        "nombre": "Marcelo",
        "edad": 6
    }
}

print(familia["hijo1"]["nombre"])