# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero sólo una expresión

# Sintaxis lambda argumentos : expresión 

# x = lambda a, b : a + b

# print(x(2,3)) # 5

def mifuncion(n):
    return lambda a : a * n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

print(duplicador(5)) # 10
print(triplicador(5)) # 15