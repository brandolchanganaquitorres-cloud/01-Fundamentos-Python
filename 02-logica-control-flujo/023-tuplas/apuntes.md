# Clase 23. Tuplas en Python (`tuple`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender qué son las tuplas en Python, cómo crearlas, acceder a sus elementos, recorrerlas, desempaquetarlas, concatenarlas y conocer cuándo utilizar una tupla en lugar de una lista en aplicaciones reales.

---

# Contenido del curso

Las **tuplas** son colecciones de datos que permiten almacenar múltiples elementos dentro de una sola variable.

Comparten varias características con las listas, pero poseen una diferencia fundamental:

> **Las tuplas son inmutables.**

Una vez creadas, sus elementos no pueden modificarse, eliminarse ni agregarse directamente.

Las tuplas presentan las siguientes características:

- Son **ordenadas**.
- Son **inmutables**.
- Permiten **elementos duplicados**.
- Admiten **distintos tipos de datos**.

---

# Crear una tupla

Las tuplas se crean utilizando paréntesis.

```python
tecnologias = (
    "Python",
    "JavaScript",
    "Go"
)

print(tecnologias)
```

Resultado.

```text
('Python', 'JavaScript', 'Go')
```

---

# Tipo de dato

```python
print(type(tecnologias))
```

Resultado.

```python
<class 'tuple'>
```

---

# Índices

Al igual que las listas, los índices comienzan en cero.

```text
Índice

0 → Python

1 → JavaScript

2 → Go
```

---

# Acceder a un elemento

```python
print(tecnologias[1])
```

Resultado.

```text
JavaScript
```

---

# Expansión técnica

El acceso mediante índice tiene un comportamiento equivalente al de las listas.

```text
Tupla

↓

Índice

↓

Elemento
```

No es necesario recorrer toda la colección para acceder a un elemento específico.

---

# Tuplas con elementos duplicados

Las tuplas permiten almacenar valores repetidos.

```python
lenguajes = (
    "Python",
    "JavaScript",
    "Go",
    "Python"
)

print(lenguajes)
```

Resultado.

```text
('Python', 'JavaScript', 'Go', 'Python')
```

---

# Contar elementos

```python
print(len(lenguajes))
```

Resultado.

```text
4
```

Los elementos duplicados también son contabilizados.

---

# La tupla de un solo elemento

Este es uno de los errores más frecuentes al comenzar con Python.

Incorrecto.

```python
fruta = ("manzana")

print(type(fruta))
```

Resultado.

```python
<class 'str'>
```

Los paréntesis por sí solos **no crean una tupla** cuando existe un único elemento.

---

# La coma es obligatoria

Correcto.

```python
fruta = ("manzana",)

print(type(fruta))
```

Resultado.

```python
<class 'tuple'>
```

La coma es la que indica a Python que se trata de una tupla.

---

# Expansión técnica

Internamente, no son los paréntesis los que definen una tupla, sino la presencia de la coma.

Por ejemplo.

```python
a = 5,
```

También produce una tupla.

```python
print(type(a))
```

Resultado.

```python
<class 'tuple'>
```

Los paréntesis solo mejoran la legibilidad.

---

# Tuplas con distintos tipos de datos

Las tuplas pueden almacenar diferentes tipos simultáneamente.

```python
datos = (
    "Python",
    5,
    True
)
```

Resultado.

```python
<class 'tuple'>
```

---

# Desempaquetado de tuplas

Cada elemento puede asignarse directamente a una variable.

```python
datos = (
    "Python",
    5,
    True
)

lenguaje, version, activo = datos
```

Ahora:

```python
print(lenguaje)
```

Resultado.

```text
Python
```

---

```python
print(version)
```

Resultado.

```text
5
```

---

```python
print(activo)
```

Resultado.

```text
True
```

---

# Funcionamiento interno

```text
Tupla

↓

Elemento 1

↓

Variable 1
```

```text
Elemento 2

↓

Variable 2
```

```text
Elemento 3

↓

Variable 3
```

El número de variables debe coincidir con el número de elementos.

---

# ¿Qué ocurre si no coinciden?

```python
datos = (
    "Python",
    5,
    True
)

a, b = datos
```

Resultado.

```text
ValueError
```

Python no puede distribuir correctamente los elementos.

---

# Concatenar tuplas

El operador `+` crea una nueva tupla.

```python
tupla1 = (
    1,
    2,
    3
)

tupla2 = (
    3,
    4,
    5
)

tupla3 = tupla1 + tupla2
```

Resultado.

```text
(1, 2, 3, 3, 4, 5)
```

Las tuplas originales permanecen sin cambios.

---

# Multiplicar una tupla

El operador `*` repite todos los elementos.

```python
numeros = (
    1,
    2,
    3
)

print(numeros * 2)
```

Resultado.

```text
(1, 2, 3, 1, 2, 3)
```

---

# Recorrer una tupla

Las tuplas pueden recorrerse mediante `for`.

```python
for lenguaje in tecnologias:
    print(lenguaje)
```

Resultado.

```text
Python
JavaScript
Go
```

---

# ¿Puede modificarse una tupla?

No.

El siguiente código produce un error.

```python
tecnologias[0] = "Rust"
```

Resultado.

```text
TypeError
```

La inmutabilidad es una característica del tipo de dato.

---

# Modificar una tupla indirectamente

Una solución consiste en convertir temporalmente la tupla en lista.

```python
tecnologias = (
    "Python",
    "JavaScript",
    "Go"
)

lista = list(tecnologias)

lista.append("React")

tecnologias = tuple(lista)
```

Resultado.

```text
('Python', 'JavaScript', 'Go', 'React')
```

---

# Funcionamiento interno

```text
Tuple

↓

list()

↓

Lista mutable

↓

Modificar

↓

tuple()

↓

Nueva tupla
```

La tupla original nunca cambia.

Simplemente se crea otra con el contenido actualizado.

---

# ¿Cuándo utilizar una tupla?

Las tuplas son apropiadas cuando los datos **no deben modificarse** durante la ejecución.

Ejemplos:

- coordenadas geográficas;
- fechas;
- colores RGB;
- configuraciones constantes;
- resultados que representan un registro fijo.

---

# Tuplas frente a listas

| Característica | Lista | Tupla |
|---------------|-------|--------|
| Mutable | ✅ Sí | ❌ No |
| Ordenada | ✅ Sí | ✅ Sí |
| Duplicados | ✅ Sí | ✅ Sí |
| Acceso por índice | ✅ Sí | ✅ Sí |
| Métodos de modificación | ✅ Sí | ❌ No |

---

# Expansión técnica

Las tuplas consumen ligeramente menos memoria que las listas y requieren menos trabajo para mantener su estructura, precisamente porque no pueden modificarse después de su creación.

Por ello, cuando un conjunto de datos es fijo, utilizar una tupla comunica claramente la intención del desarrollador y evita modificaciones accidentales.

---

# AI Engineering

Las tuplas aparecen con frecuencia en proyectos de IA y procesamiento de datos.

| Caso | Uso |
|------|-----|
| Coordenadas | `(latitud, longitud)` |
| Dimensiones | `(alto, ancho)` de imágenes |
| Resultados | `(texto, puntuación)` |
| Configuración | Valores constantes de un modelo |
| Machine Learning | Representación de pares `(entrada, etiqueta)` |

### Caso práctico

Representar la resolución de una imagen.

```python
resolucion = (1920, 1080)

ancho, alto = resolucion
```

Las dimensiones no deberían modificarse accidentalmente durante el procesamiento.

---

# Problemas reales en producción

## Problema 1

Intentar modificar una tupla.

```python
configuracion[0] = "nuevo"
```

Resultado.

```text
TypeError
```

---

## Problema 2

Olvidar la coma en una tupla de un elemento.

```python
valor = ("Python")
```

Resultado.

```python
<class 'str'>
```

Debe escribirse.

```python
valor = ("Python",)
```

---

## Problema 3

Desempaquetar con un número incorrecto de variables.

```python
a, b = (1, 2, 3)
```

Resultado.

```text
ValueError
```

---

## Problema 4

Convertir continuamente entre lista y tupla.

```python
tuple(list(tuple(...)))
```

Si una estructura necesita modificaciones frecuentes, probablemente debería ser una lista desde el inicio.

---

# Buenas prácticas

- Utiliza tuplas cuando los datos representen información fija.
- Emplea listas cuando necesites agregar, eliminar o modificar elementos con frecuencia.
- Aprovecha el desempaquetado para mejorar la legibilidad del código.
- Recuerda que la coma, y no los paréntesis, define una tupla de un solo elemento.
- Evita convertir constantemente entre listas y tuplas si la estructura va a cambiar repetidamente.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "Las tuplas no pueden modificarse nunca"

### Corrección técnica

La **tupla como estructura** es inmutable, pero esto no significa que todos los objetos almacenados dentro de ella también lo sean.

Ejemplo.

```python
datos = (
    [1, 2],
    "Python"
)

datos[0].append(3)

print(datos)
```

Resultado.

```text
([1, 2, 3], 'Python')
```

La referencia almacenada en la tupla no cambió; lo que cambió fue el contenido de la lista, que sí es mutable.

---

## Corrección 2. "`+` modifica las dos tuplas"

### Corrección técnica

No. El operador `+` crea una **nueva tupla**. Las tuplas originales permanecen exactamente iguales porque son inmutables.

---

## Corrección 3. "Las tuplas son simplemente listas que no pueden modificarse"

### Corrección técnica

Aunque externamente son similares, las tuplas y las listas son tipos de datos distintos con implementaciones diferentes. Las tuplas están optimizadas para representar colecciones inmutables y suelen ser más eficientes en memoria y velocidad de creación que las listas.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuándo utilizarías una tupla en lugar de una lista?

### Qué evalúa

Capacidad para seleccionar la estructura de datos adecuada.

### Errores comunes

- Responder únicamente "porque no cambia", sin justificar el diseño.

### Respuesta de alto impacto

> Utilizaría una tupla cuando los datos representen un conjunto fijo que no debe modificarse, como coordenadas, configuraciones o resultados estructurados. Además de evitar cambios accidentales, el uso de una tupla comunica claramente esa intención al resto del equipo y ofrece un ligero beneficio de rendimiento y memoria.

---

## Pregunta 2

¿Por qué una tupla con un solo elemento necesita una coma?

### Qué evalúa

Conocimiento de la sintaxis del lenguaje.

### Errores comunes

- Pensar que los paréntesis crean la tupla.

### Respuesta de alto impacto

> Porque en Python la presencia de la coma es lo que define una tupla. Los paréntesis son opcionales en muchos contextos y solo ayudan a la legibilidad. Sin la coma, Python interpreta la expresión como el propio valor entre paréntesis.

---

## Pregunta 3

¿La inmutabilidad de una tupla garantiza que todos sus elementos sean inmutables?

### Qué evalúa

Comprensión profunda del concepto de inmutabilidad.

### Errores comunes

- Responder que sí.

### Respuesta de alto impacto

> No. La tupla impide reemplazar las referencias que contiene, pero si uno de sus elementos es un objeto mutable, como una lista o un diccionario, ese objeto puede seguir modificándose. La inmutabilidad afecta a la estructura de la tupla, no necesariamente al estado interno de los objetos almacenados.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `tuple`.
- Python Documentation — Sequence Types.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 3132** — Extended Iterable Unpacking.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.