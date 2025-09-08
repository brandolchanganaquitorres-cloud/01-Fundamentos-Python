from math import sin


print('Hola "Mundo"')

ingles = "I'm Sergie"

multiples = """Hola
Mundo
desde
las
comillas
triples"""

print(ingles)
print(multiples)

palabra = "Murciélago"
print(len(palabra))

texto = "Este curso es de Fundamentos de Python"
estaIncluda = "Python" in texto
noEstaIncluida = "Javascript" not in texto

print(noEstaIncluida)

mayuscula = texto.upper()
minuscula = texto.lower()

texto2 = texto.upper()
texto2 = texto.lower()

print(texto2)

espacios = "        Este es el texto         "
sinEspacios = espacios.strip()

print(sinEspacios)