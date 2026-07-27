# Clase 22. Listas en Python (`list`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo funcionan las listas en Python, aprender a crear, acceder, modificar, recorrer y combinar listas, dominar los métodos más utilizados (`append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `extend()`) y entender su comportamiento interno para utilizarlas correctamente en aplicaciones reales.

---

# Contenido del curso

Las **listas** son una de las estructuras de datos más importantes de Python.

Permiten almacenar múltiples elementos dentro de una sola variable y son utilizadas prácticamente en cualquier aplicación.

Una lista en Python posee tres características principales:

- Es **ordenada**.
- Es **mutable**.
- Permite **elementos duplicados**.

---

# Crear una lista

Las listas se crean utilizando corchetes (`[]`).

```python
frutas = [
    "manzana",
    "naranja",
    "mandarina"
]

print(frutas)
```

Resultado:

```text
['manzana', 'naranja', 'mandarina']
```

---

# Tipo de dato

```python
print(type(frutas))
```

Resultado:

```python
<class 'list'>
```

---

# ¿Qué significa que una lista sea ordenada?

Cada elemento ocupa una posición fija denominada **índice**.

Los índices comienzan en **0**.

```text
Índice

0 → manzana

1 → naranja

2 → mandarina
```

---

# Acceder a un elemento

```python
print(frutas[1])
```

Resultado:

```text
naranja
```

Porque el índice `1` corresponde al segundo elemento.

---

# Expansión técnica

El acceso por índice es muy eficiente.

```text
Lista

↓

Índice

↓

Elemento
```

Python puede acceder directamente al elemento sin recorrer toda la lista.

---

# Listas mutables

Una lista puede modificarse después de haber sido creada.

```python
frutas[1] = "banana"

print(frutas)
```

Resultado:

```text
['manzana', 'banana', 'mandarina']
```

---

# ¿Qué significa mutable?

Mutable significa que el contenido del objeto puede cambiar sin crear una nueva lista.

```text
Lista existente

↓

Modificar elemento

↓

La misma lista cambia
```

Esto diferencia a las listas de otros tipos inmutables como los `str` o las `tuple`.

---

# El orden de ejecución importa

Python ejecuta el código de arriba hacia abajo.

```python
print(frutas)

frutas[1] = "banana"

print(frutas)
```

Primer resultado.

```text
['manzana', 'naranja', 'mandarina']
```

Segundo resultado.

```text
['manzana', 'banana', 'mandarina']
```

---

# Listas con distintos tipos de datos

Python permite mezclar tipos diferentes.

```python
datos = [
    "Juan",
    25,
    True
]
```

Resultado.

```python
<class 'list'>
```

---

# Expansión técnica

Aunque Python lo permite, en proyectos profesionales se recomienda que las listas almacenen elementos relacionados y, preferiblemente, del mismo tipo.

Ejemplo recomendable.

```python
precios = [15.5, 32.0, 18.9]
```

En lugar de:

```python
["Juan", 25, True]
```

La homogeneidad facilita el mantenimiento y reduce errores.

---

# Contar elementos con `len()`

```python
print(len(frutas))
```

Resultado.

```text
3
```

`len()` devuelve el número de elementos almacenados en la lista.

---

# Slicing de listas

Las listas utilizan el mismo mecanismo de *slicing* que las cadenas.

```python
print(frutas[0:2])
```

Resultado.

```text
['manzana', 'banana']
```

El índice final **no se incluye**.

---

## Desde el inicio

```python
print(frutas[:2])
```

Resultado.

```text
['manzana', 'banana']
```

---

## Hasta el final

```python
print(frutas[1:])
```

Resultado.

```text
['banana', 'mandarina']
```

---

# Verificar existencia con `in`

```python
if "manzana" in frutas:
    print("Existe")
```

Resultado.

```text
Existe
```

El operador `in` devuelve un valor booleano.

---

# Método `append()`

Agrega un elemento al final de la lista.

```python
vehiculos = [
    "auto",
    "moto",
    "avión"
]

vehiculos.append("barco")

print(vehiculos)
```

Resultado.

```text
['auto', 'moto', 'avión', 'barco']
```

---

# Funcionamiento interno

```text
Lista

↓

Añadir elemento

↓

Última posición disponible
```

No modifica el orden de los elementos existentes.

---

# Método `insert()`

Permite insertar un elemento en una posición específica.

```python
vehiculos.insert(1, "bicicleta")
```

Resultado.

```text
['auto', 'bicicleta', 'moto', 'avión', 'barco']
```

---

# Expansión técnica

Cuando se inserta un elemento, todos los elementos posteriores se desplazan una posición hacia la derecha.

```text
Antes

0 auto

1 moto

2 avión
```

```text
Insertar bicicleta

↓

Después

0 auto

1 bicicleta

2 moto

3 avión
```

---

# Método `remove()`

Elimina un elemento indicando su valor.

```python
vehiculos.remove("auto")
```

Resultado.

```text
['bicicleta', 'moto', 'avión', 'barco']
```

---

# Método `pop()`

Elimina un elemento indicando su índice.

```python
vehiculos.pop(1)
```

Resultado.

```text
['bicicleta', 'avión', 'barco']
```

---

# Diferencia entre `remove()` y `pop()`

| Método | Elimina por |
|----------|-------------|
| `remove()` | Valor |
| `pop()` | Índice |

---

# Expansión técnica

Existe una diferencia importante.

```python
elemento = vehiculos.pop(1)
```

`pop()` **devuelve** el elemento eliminado.

```python
print(elemento)
```

Resultado.

```text
avión
```

En cambio:

```python
vehiculos.remove("barco")
```

simplemente elimina el elemento y devuelve `None`.

Esta diferencia es muy utilizada cuando necesitamos extraer un elemento para seguir procesándolo.

---

# Método `sort()`

Ordena la lista.

```python
vehiculos.sort()

print(vehiculos)
```

Resultado.

```text
['avión', 'barco', 'bicicleta']
```

---

# Método `reverse()`

Invierte el orden actual.

```python
vehiculos.reverse()
```

Resultado.

```text
['bicicleta', 'barco', 'avión']
```

---

# Expansión técnica

Es importante distinguir ambos métodos.

```python
sort()
```

ordena.

Mientras que:

```python
reverse()
```

únicamente invierte el orden existente.

Si la lista no estaba ordenada previamente, `reverse()` no la ordenará.

---

# Unir listas con `+`

```python
coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]

coleccion3 = coleccion1 + coleccion2
```

Resultado.

```text
[1, 2, 3, 4, 5, 6]
```

Las listas originales permanecen sin cambios.

---

# Método `extend()`

```python
coleccion1.extend(coleccion2)
```

Resultado.

```text
[1, 2, 3, 4, 5, 6]
```

En este caso **la lista original sí cambia**.

---

# Diferencia entre `+` y `extend()`

| Operación | ¿Modifica la lista original? | ¿Crea una nueva lista? |
|-----------|------------------------------|------------------------|
| `+` | ❌ No | ✅ Sí |
| `extend()` | ✅ Sí | ❌ No |

---

# Funcionamiento interno

Con `+`.

```text
Lista A

+

Lista B

↓

Nueva lista
```

Con `extend()`.

```text
Lista A

↓

Agregar elementos de Lista B

↓

La misma lista cambia
```

---

# AI Engineering

Las listas aparecen constantemente en proyectos de IA.

| Caso | Uso |
|------|-----|
| Prompts | Lista de mensajes para un chat |
| RAG | Lista de documentos recuperados |
| Embeddings | Lista de vectores |
| APIs | Respuestas JSON convertidas en listas |
| Machine Learning | Conjuntos de características (*features*) |
| Automatización | Lista de archivos a procesar |

### Caso práctico

Procesar varios documentos antes de generar embeddings.

```python
documentos = [
    "manual.pdf",
    "contrato.pdf",
    "reporte.pdf"
]

for documento in documentos:
    generar_embedding(documento)
```

Este patrón es uno de los más comunes en aplicaciones RAG.

---

# Problemas reales en producción

## Problema 1

Acceder a un índice inexistente.

```python
frutas[10]
```

Resultado.

```text
IndexError: list index out of range
```

Siempre debe comprobarse que el índice exista.

---

## Problema 2

Eliminar un elemento que no está presente.

```python
vehiculos.remove("tren")
```

Resultado.

```text
ValueError
```

Antes de eliminar puede verificarse:

```python
if "tren" in vehiculos:
    vehiculos.remove("tren")
```

---

## Problema 3

Modificar una lista mientras se está recorriendo.

```python
for fruta in frutas:
    frutas.remove(fruta)
```

Puede provocar resultados inesperados y elementos omitidos.

---

## Problema 4

Suponer que `+` modifica la lista original.

```python
a + b
```

Si el resultado no se asigna a una variable, la nueva lista se pierde.

---

# Buenas prácticas

- Utiliza listas cuando el orden de los elementos sea importante.
- Prefiere almacenar elementos del mismo tipo dentro de una misma lista.
- Utiliza `append()` para agregar elementos individuales al final.
- Emplea `extend()` cuando desees incorporar todos los elementos de otra lista.
- Comprueba la existencia de un elemento antes de utilizar `remove()`.
- Evita modificar una lista mientras la recorres.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`sort()` solo ordena alfabéticamente"

### Corrección técnica

`sort()` ordena según el criterio natural de los elementos. En cadenas utiliza el orden lexicográfico; en números realiza un orden numérico ascendente. Además, admite parámetros como `reverse=True` y `key` para personalizar el criterio de ordenación.

Ejemplo.

```python
numeros = [8, 2, 15, 4]

numeros.sort()

print(numeros)
```

Resultado.

```text
[2, 4, 8, 15]
```

---

## Corrección 2. "`reverse()` ordena de mayor a menor"

### Corrección técnica

No. `reverse()` únicamente invierte el orden actual de la lista. Si la lista está desordenada, seguirá desordenada, pero en sentido inverso.

---

## Corrección 3. "Las listas pueden contener cualquier combinación de tipos y siempre es una buena práctica"

### Corrección técnica

Aunque Python lo permite, en desarrollo profesional se procura que una lista represente una colección homogénea de elementos relacionados. Esto facilita el análisis, el mantenimiento y el uso de herramientas de tipado estático como `mypy`.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre `append()` y `extend()`?

### Qué evalúa

Comprensión de los métodos fundamentales de las listas.

### Errores comunes

- Pensar que ambos agregan exactamente lo mismo.

### Respuesta de alto impacto

> `append()` agrega un único elemento al final de la lista, incluso si ese elemento es otra lista. `extend()` incorpora cada elemento del iterable recibido de forma individual, ampliando la lista existente sin crear una nueva.

---

## Pregunta 2

¿Cuándo utilizarías `remove()` y cuándo `pop()`?

### Qué evalúa

Capacidad para elegir el método adecuado según el contexto.

### Errores comunes

- Confundir eliminación por valor con eliminación por índice.

### Respuesta de alto impacto

> Utilizaría `remove()` cuando conozca el valor que deseo eliminar y `pop()` cuando conozca la posición o necesite recuperar el elemento eliminado para seguir procesándolo, ya que `pop()` devuelve dicho elemento.

---

## Pregunta 3

¿Por qué acceder a un elemento mediante índice es una operación eficiente?

### Qué evalúa

Comprensión básica del funcionamiento interno de las listas.

### Errores comunes

- Pensar que Python recorre toda la lista para encontrar el elemento.

### Respuesta de alto impacto

> Porque las listas están implementadas como arreglos dinámicos. Python puede calcular directamente la dirección del elemento a partir de su índice, lo que permite acceder a él en tiempo constante promedio, sin recorrer previamente el resto de la colección.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `list`.
- Python Documentation — List Methods.
- Python Documentation — Data Structures.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 484** — Type Hints (tipado de listas).

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.