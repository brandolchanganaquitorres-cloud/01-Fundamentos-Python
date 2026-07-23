palabra = "Python"

for letra in palabra:
    print(letra)

adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Naranja", "Kiwi"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)

# Manzana Rica
# Manzana Saludable
# Naranja Rica
# Naranja Saludable
# Kiwi Rica
# Kiwi Saludable

# for fruta in frutas:
#     if fruta == "Naranja":
#         continue
#     print(fruta)
# else:
#     print("Ya hemos terminado el bucle for")



print("-------------------------")

# Range

# Comienza desde el cero y termina en el número que asignemos sin incluírlo
# for i in range(10):
#     print(i)

# for i in range(3,5):
#     print(i)

# for i in range(0,11,2):
#     print(i)

for i in range(10):
    pass