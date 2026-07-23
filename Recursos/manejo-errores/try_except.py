try:
    numero = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

x = 1

try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida")
finally:
    print("Esto será ejecutado siendo exitoso o no el bloque")

