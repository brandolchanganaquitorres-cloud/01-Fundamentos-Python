# Clase 8. Asignación múltiple de variables y concatenación en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Objetivo:** Comprender cómo funciona la asignación múltiple de variables, la asignación en cadena y las diferentes formas de mostrar información en pantalla utilizando `print()`, diferenciando correctamente entre separación de argumentos, concatenación de cadenas y operaciones aritméticas.

---

# Contenido del curso

## Asignación múltiple de variables

Python permite asignar varios valores a varias variables en una única instrucción.

```python
x, y, z = "manzana", "naranja", "banana"

print(x, y, z)
```

Salida:

```text
manzana naranja banana
```

Cada variable recibe el valor que ocupa la misma posición en la secuencia de asignación.

| Variable | Valor asignado |
|----------|----------------|
| `x` | `"manzana"` |
| `y` | `"naranja"` |
| `z` | `"banana"` |

Este mecanismo reduce la cantidad de código y mejora la legibilidad.

---

## ¿Cómo funciona la asignación por posición?

Python asigna los valores de izquierda a derecha.

```python
nombre, edad, ciudad = "Brandol", 30, "Lima"
```

Equivale a escribir:

```python
nombre = "Brandol"
edad = 30
ciudad = "Lima"
```

La primera versión es más compacta, fácil de leer y disminuye la posibilidad de cometer errores al repetir asignaciones.

---

## Reglas de la asignación múltiple

Debe existir la misma cantidad de variables que de valores.

Correcto:

```python
a, b, c = 1, 2, 3
```

Incorrecto:

```python
a, b = 1, 2, 3
```

Resultado:

```text
ValueError: too many values to unpack
```

También es incorrecto:

```python
a, b, c = 1, 2
```

Resultado:

```text
ValueError: not enough values to unpack
```

---

# Asignación en cadena

Cuando varias variables deben almacenar exactamente el mismo valor, Python permite realizar una asignación en cadena.

```python
a = b = c = "mandarina"

print(a, b, c)
```

Salida:

```text
mandarina mandarina mandarina
```

Todas las variables reciben inicialmente el mismo valor.

---

# Mostrar información con `print()`

La función `print()` acepta múltiples argumentos.

```python
print(x, y, z)
```

Salida:

```text
manzana naranja banana
```

Python inserta automáticamente un espacio entre cada argumento.

Esta es la forma más sencilla y recomendada de imprimir varios valores.

---

# Concatenación mediante el operador `+`

También es posible unir cadenas utilizando el operador `+`.

```python
print("Mi fruta favorita es " + x)
```

Salida:

```text
Mi fruta favorita es manzana
```

En este caso no existe separación automática.

---

## Agregar espacios manualmente

```python
print(a + " " + z)
```

Salida:

```text
mandarina banana
```

Sin el espacio:

```python
print(a + z)
```

Salida:

```text
mandarinabanana
```

El operador `+` une exactamente el contenido de ambas cadenas.

---

# Uso de `+` con números

Cuando ambos operandos son números, el operador realiza una suma.

```python
d = 5
e = 6

print(d + e)
```

Salida:

```text
11
```

No concatena los valores.

---

# Diferencia entre texto y números

```python
print("5" + "6")
```

Salida:

```text
56
```

Mientras que:

```python
print(5 + 6)
```

produce:

```text
11
```

El comportamiento del operador `+` depende del tipo de dato.

---

# Expansión técnica

## ¿Cómo funciona internamente la asignación múltiple?

Cuando Python encuentra:

```python
x, y, z = "manzana", "naranja", "banana"
```

internamente ocurre un proceso equivalente a:

```text
Se crea una tupla temporal

("manzana", "naranja", "banana")

        │

        ▼

Sequence Unpacking

        │

        ├── x ← "manzana"

        ├── y ← "naranja"

        └── z ← "banana"
```

Este mecanismo recibe el nombre de **Sequence Unpacking** (desempaquetado de secuencias).

No es exclusivo de las tuplas; funciona con cualquier objeto iterable que tenga la misma cantidad de elementos.

Ejemplo:

```python
datos = ["Brandol", 30, "Perú"]

nombre, edad, pais = datos
```

---

## Sequence Unpacking

El desempaquetado es una de las características más utilizadas de Python.

Ejemplo:

```python
coordenadas = (10, 25)

x, y = coordenadas
```

Internamente:

```text
Tupla

↓

Iterador

↓

Primer elemento → x

Segundo elemento → y
```

Este mecanismo aparece constantemente en:

- procesamiento de APIs REST;
- lectura de archivos;
- consultas SQL;
- manipulación de diccionarios;
- bibliotecas como Pandas, NumPy y LangChain.

---

## Intercambio de variables sin variable temporal

Gracias al desempaquetado, Python permite intercambiar valores de forma elegante.

```python
a = 5
b = 8

a, b = b, a
```

Resultado:

```python
print(a)
```

```text
8
```

```python
print(b)
```

```text
5
```

Internamente:

```text
(a, b)

↓

(b, a)

↓

Desempaquetado
```

No se necesita una variable auxiliar, como ocurre en otros lenguajes.

---

## ¿Cómo funciona la asignación en cadena?

Cuando escribimos:

```python
a = b = c = 100
```

Python evalúa primero el valor situado a la derecha y después asigna la misma referencia a cada variable.

```text
        100
         ▲
         │
 ┌───┬───┴───┬───┐
 │   │       │   │
 a   b       c
```

Con objetos inmutables (enteros, cadenas, tuplas) esto no representa ningún problema.

---

## Atención con objetos mutables

Aquí aparece uno de los errores más frecuentes entre programadores principiantes.

```python
a = b = []
```

Parece que existen dos listas.

En realidad existe **una sola**.

```text
        ┌──────────────┐
a ─────►│      []      │
b ─────►└──────────────┘
```

Si hacemos:

```python
a.append(10)
```

Obtendremos:

```python
print(b)
```

```text
[10]
```

Porque ambas variables apuntan al mismo objeto.

La forma correcta es:

```python
a = []
b = []
```

o

```python
a, b = [], []
```

---

## ¿Cómo funciona `print()`?

La función `print()` acepta cualquier cantidad de argumentos.

```python
print(x, y, z)
```

Internamente ocurre un proceso similar a:

```text
print()

↓

Convierte cada argumento mediante str()

↓

Inserta el separador (sep)

↓

Agrega el final de línea (end)

↓

Envía el resultado a stdout
```

Por defecto:

```python
sep = " "
end = "\n"
```

Por eso aparece un espacio entre los valores y un salto de línea al finalizar.

---

## Personalizar el separador

Pocas personas conocen que `print()` permite modificar el separador.

```python
print(x, y, z, sep="-")
```

Salida:

```text
manzana-naranja-banana
```

Otro ejemplo:

```python
print(x, y, z, sep=" | ")
```

Salida:

```text
manzana | naranja | banana
```

También puede modificarse el carácter final.

```python
print("Hola", end="")
print(" Mundo")
```

Salida:

```text
Hola Mundo
```

---

## ¿Qué hace realmente el operador `+`?

El operador `+` está **sobrecargado** en Python.

Su comportamiento depende del tipo de dato.

Con enteros:

```python
5 + 6
```

↓

```text
11
```

Con cadenas:

```python
"Hola" + " Mundo"
```

↓

```text
Hola Mundo
```

Con listas:

```python
[1, 2] + [3, 4]
```

↓

```text
[1, 2, 3, 4]
```

El mismo operador ejecuta operaciones distintas según el tipo de los operandos.

Este concepto se conoce como **sobrecarga de operadores (Operator Overloading)**.

---

## ¿Por qué falla esta expresión?

```python
edad = 30

print("Edad: " + edad)
```

Resultado:

```text
TypeError: can only concatenate str (not "int") to str
```

Porque Python no convierte automáticamente un entero en texto.

Debe hacerse explícitamente.

```python
print("Edad: " + str(edad))
```

Aunque la opción más recomendable es:

```python
print("Edad:", edad)
```

o, en Python moderno:

```python
print(f"Edad: {edad}")
```

---

# Problemas reales en producción

## Problema 1

Asignar varias listas mediante asignación en cadena.

```python
usuarios = administradores = []
```

Modificar una modifica ambas.

---

## Problema 2

Concatenar texto con números.

```python
print("Total: " + total)
```

Genera un `TypeError`.

---

## Problema 3

Olvidar que `print()` añade espacios automáticamente.

```python
print(nombre, apellido)
```

Muchos desarrolladores agregan espacios manualmente sin necesidad.

---

## Problema 4

Intentar desempaquetar una cantidad distinta de elementos.

```python
x, y = [1, 2, 3]
```

Produce:

```text
ValueError
```

---

# Relación con AI Engineering

La asignación múltiple y el desempaquetado aparecen constantemente en proyectos de IA.

Ejemplos habituales:

```python
prompt, temperature, max_tokens = configuracion
```

Procesando respuestas de una API:

```python
status_code, respuesta = obtener_respuesta()
```

Con LangChain:

```python
documento, metadata = loader.load()
```

Con Pandas:

```python
indice, fila = siguiente_registro
```

En aplicaciones de IA estas técnicas permiten escribir código más limpio y expresivo al trabajar con respuestas complejas de APIs, modelos de lenguaje y bases de datos.

---

# Buenas prácticas

- Utiliza asignación múltiple cuando las variables estén relacionadas.
- Emplea asignación en cadena únicamente con objetos inmutables.
- Prefiere `print()` con múltiples argumentos antes que concatenar mediante `+`.
- Evita concatenar cadenas con números; utiliza `str()` o, preferiblemente, **f-strings**.
- Aprovecha el desempaquetado para escribir código más legible.
- Utiliza nombres descriptivos incluso en asignaciones múltiples.

---

# Errores conceptuales detectados en el curso

## Corrección 1. La asignación múltiple no copia valores

El curso explica que cada variable "recibe" un valor.

### Corrección técnica

En Python las variables almacenan **referencias a objetos**, no copias de los objetos. Durante el desempaquetado, cada variable pasa a referenciar el objeto correspondiente.

---

## Corrección 2. El operador `+` no solo suma o concatena

El curso menciona únicamente cadenas y números.

### Corrección técnica

El operador `+` está sobrecargado. Además de sumar números y concatenar cadenas, también puede concatenar listas, tuplas y cualquier objeto que implemente el método especial `__add__()`.

---

## Corrección 3. El curso recomienda utilizar `+` para construir mensajes

### Corrección técnica

Aunque es correcto para aprender los fundamentos, en Python moderno la práctica recomendada es utilizar **f-strings** (PEP 498), ya que ofrecen mejor legibilidad, mayor rendimiento y menor probabilidad de errores.

Ejemplo:

```python
nombre = "Brandol"

print(f"Mi nombre es {nombre}")
```

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Qué ocurre internamente durante una asignación múltiple en Python?

### Qué evalúa

Comprensión del mecanismo de desempaquetado de secuencias.

### Errores comunes

- Pensar que Python realiza varias asignaciones independientes.
- Desconocer el concepto de *Sequence Unpacking*.

### Respuesta de alto impacto

> Python evalúa primero la expresión del lado derecho, obtiene un objeto iterable y posteriormente realiza un proceso de *Sequence Unpacking*, asignando cada elemento a la variable correspondiente. Si la cantidad de elementos no coincide con la cantidad de variables, se genera un `ValueError`.

---

## Pregunta 2

¿Por qué `a = b = []` puede provocar errores difíciles de detectar?

### Qué evalúa

Comprensión del modelo de referencias y objetos mutables.

### Errores comunes

- Creer que se crean dos listas independientes.

### Respuesta de alto impacto

> Porque la asignación en cadena no crea varios objetos; todas las variables apuntan a la misma lista en memoria. Al modificar la lista desde una referencia, el cambio es visible desde las demás. Para evitar este comportamiento deben crearse listas independientes.

---

## Pregunta 3

¿Por qué suele recomendarse `print(nombre, edad)` en lugar de `print(nombre + str(edad))`?

### Qué evalúa

Conocimiento del funcionamiento de `print()` y de la conversión de tipos.

### Errores comunes

- Pensar que `print()` solo acepta cadenas.

### Respuesta de alto impacto

> Porque `print()` acepta argumentos de cualquier tipo, realiza internamente la conversión mediante `str()`, aplica automáticamente el separador definido por `sep` y evita errores de concatenación. El código resulta más limpio, seguro y fácil de mantener.

---

## Pregunta 4

¿Cuál es la ventaja del desempaquetado de secuencias frente a realizar varias asignaciones?

### Qué evalúa

Conocimiento de características propias de Python.

### Errores comunes

- Considerarlo únicamente una forma de escribir menos código.

### Respuesta de alto impacto

> El desempaquetado mejora la legibilidad, reduce la repetición de código, permite intercambiar variables sin temporales y facilita trabajar con funciones y APIs que devuelven múltiples valores, una práctica muy común en aplicaciones de IA y procesamiento de datos.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Assignment Statements.
- Python Documentation — Built-in Functions (`print`).
- Python Documentation — Data Model.

## PEPs

- PEP 8 — Style Guide for Python Code.
- PEP 498 — Literal String Interpolation (f-strings).

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.

---