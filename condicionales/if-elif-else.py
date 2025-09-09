x = 5
y = 3
z = 10

if x > y or x > z:
    print("x es mayor a y y x es menor a z")
elif x == y:
    print("x es igual a y")
else:
    print("Ninguna de las condiciones anteriores se cumplió")


a = "Python"
b = "Javascript"
c = "Python"

if a == c:
    if a == b:
        print("a es igual a c pero es distinto a b")
    else:
        print("Estoy saliendo por el else del if interno")
else:
    print("a no es igual a c")


e = 10
f = 10

if e == f:
    pass # Para ignorar la estructura if hasta tanto definamos que comportamiento se espera