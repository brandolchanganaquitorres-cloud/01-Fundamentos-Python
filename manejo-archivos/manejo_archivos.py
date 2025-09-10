
# open(nombre, modo)

# R (read) Lectura 
# W (write) Escritura
# X (Crea archivo nuevo)

try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x")
    print("No se ha encontrado el archivo")

try:
    with open("archivo.txt", "a") as f:
        f.write("\n")
        f.write("Hola mundo desde write en el with")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")