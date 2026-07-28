# Clase 24. Conjuntos en Python (`set`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo funcionan los conjuntos (`set`) en Python, aprender a crear, modificar y recorrer conjuntos, utilizar sus métodos principales (`add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`), realizar operaciones matemáticas entre conjuntos y entender por qué son una de las estructuras más eficientes para eliminar duplicados y realizar búsquedas.

---

# Contenido del curso

Los **conjuntos** (`set`) son colecciones de datos que almacenan elementos **únicos**.

Su principal característica es que **no permiten elementos duplicados**.

Además, un conjunto es:

- No ordenado.
- Mutable (puede agregar o eliminar elementos).
- No indexado.
- Formado únicamente por elementos únicos.

Los conjuntos están inspirados en la teoría matemática de conjuntos.

---

# Crear un conjunto

Los conjuntos se crean utilizando llaves (`{}`).

```python
frutas = {
    "manzana",
    "naranja",
    "mandarina"
}

print(frutas)
```

---

# Tipo de dato

```python
print(type(frutas))
```

Resultado.

```python
<class 'set'>
```

---

# Los elementos duplicados desaparecen

```python
frutas = {
    "manzana",
    "naranja",
    "mandarina",
    "naranja"
}

print(frutas)
```

Resultado.

```text
{'manzana', 'naranja', 'mandarina'}
```

El segundo `"naranja"` nunca llega a almacenarse.

---

# Contar elementos

```python
print(len(frutas))
```

Resultado.

```text
3
```

Aunque se escribieron cuatro elementos, solo existen tres distintos.

---

# Expansión técnica

Cuando se inserta un elemento, Python comprueba automáticamente si ya existe.

```text
Nuevo elemento

↓

¿Existe?

↓

Sí

↓

Ignorar
```

```text
↓

No

↓

Insertar
```

Este comportamiento convierte a los conjuntos en la estructura ideal para eliminar duplicados.

---

# Los conjuntos no están ordenados

```python
frutas = {
    "manzana",
    "naranja",
    "mandarina"
}

for fruta in frutas:
    print(fruta)
```

La salida puede ser.

```text
mandarina
manzana
naranja
```

o

```text
naranja
mandarina
manzana
```

El orden **no está garantizado**.

---

# ¿Por qué ocurre?

Los conjuntos no almacenan los elementos según su posición.

Internamente utilizan una **tabla hash (Hash Table)**.

```text
Elemento

↓

Hash

↓

Posición interna
```

Por ello:

- no existen índices;
- no existe una posición fija;
- el orden puede variar.

---

# Verificar existencia con `in`

```python
print("manzana" in frutas)
```

Resultado.

```python
True
```

---

También puede comprobarse la ausencia.

```python
print("pera" not in frutas)
```

Resultado.

```python
True
```

---

# Expansión técnica

La búsqueda en un conjunto es extremadamente rápida.

```text
Elemento

↓

Hash

↓

Búsqueda directa
```

Por este motivo, los conjuntos suelen utilizarse para validaciones de pertenencia en aplicaciones de alto rendimiento.

---

# Método `add()`

Agrega un único elemento.

```python
frutas.add("pera")

print(frutas)
```

Resultado.

```text
{'manzana', 'naranja', 'mandarina', 'pera'}
```

---

# Método `update()`

Permite agregar múltiples elementos.

```python
tropicales = {
    "piña",
    "mango"
}

frutas.update(tropicales)
```

Resultado.

```text
{'manzana', 'naranja', 'mandarina', 'pera', 'piña', 'mango'}
```

---

# `update()` acepta otros iterables

No es necesario utilizar otro conjunto.

También funciona con listas.

```python
frutas.update([
    "uva",
    "sandía"
])
```

Y con tuplas.

```python
frutas.update((
    "papaya",
    "melón"
))
```

---

# Método `remove()`

Elimina un elemento.

```python
frutas.remove("pera")
```

Resultado.

```text
{'manzana', 'naranja', 'mandarina'}
```

---

# ¿Qué ocurre si no existe?

```python
frutas.remove("limón")
```

Resultado.

```text
KeyError
```

---

# Método `discard()`

```python
frutas.discard("limón")
```

Resultado.

```text
(No ocurre ningún error)
```

Si el elemento no existe, Python simplemente continúa.

---

# Diferencia entre `remove()` y `discard()`

| Método | Si el elemento no existe |
|----------|-------------------------|
| `remove()` | Lanza `KeyError` |
| `discard()` | No ocurre nada |

---

# Método `pop()`

```python
frutas.pop()
```

Elimina un elemento del conjunto.

Sin embargo, **no existe garantía sobre cuál será eliminado**.

---

# Expansión técnica

Como los conjuntos no poseen índices ni orden definido, `pop()` elimina un elemento arbitrario determinado por la organización interna del conjunto.

Por ello, **no debe utilizarse cuando sea necesario eliminar un elemento específico**.

---

# Método `clear()`

Vacía completamente el conjunto.

```python
frutas.clear()

print(frutas)
```

Resultado.

```text
set()
```

---

# Operaciones entre conjuntos

Una de las principales ventajas de los `set` es que implementan directamente las operaciones de teoría de conjuntos.

---

# Unión

```python
set1 = {
    "a",
    "b",
    "c"
}

set2 = {
    "c",
    "d",
    "e"
}

print(set1.union(set2))
```

Resultado.

```text
{'a', 'b', 'c', 'd', 'e'}
```

Todos los elementos aparecen una sola vez.

---

# Funcionamiento

```text
Set A

+

Set B

↓

Todos los elementos
```

---

# Intersección

```python
print(set1.intersection(set2))
```

Resultado.

```text
{'c'}
```

Únicamente aparecen los elementos comunes.

---

# Funcionamiento

```text
Set A

∩

Set B

↓

Elementos comunes
```

---

# Diferencia

```python
print(set1.difference(set2))
```

Resultado.

```text
{'a', 'b'}
```

Se obtienen únicamente los elementos presentes en `set1` pero ausentes en `set2`.

---

# Funcionamiento

```text
Set A

−

Set B

↓

Elementos exclusivos de A
```

---

# Eliminar duplicados de una lista

Uno de los usos más frecuentes de los conjuntos consiste en eliminar elementos repetidos.

```python
lista = [
    1,
    2,
    2,
    3,
    3,
    4
]

lista_limpia = list(set(lista))

print(lista_limpia)
```

Resultado.

```text
[1, 2, 3, 4]
```

---

# Expansión técnica

El proceso ocurre en tres etapas.

```text
Lista

↓

set()

↓

Eliminar duplicados

↓

list()

↓

Nueva lista
```

Debe tenerse en cuenta que el orden original puede cambiar.

---

# ¿Cuándo utilizar un conjunto?

Los conjuntos son ideales cuando:

- no importan las posiciones;
- se necesitan elementos únicos;
- las búsquedas deben ser muy rápidas;
- se realizarán operaciones matemáticas entre colecciones.

---

# Set frente a lista

| Característica | Lista | Set |
|---------------|--------|-----|
| Ordenado | ✅ Sí | ❌ No |
| Índices | ✅ Sí | ❌ No |
| Duplicados | ✅ Sí | ❌ No |
| Mutable | ✅ Sí | ✅ Sí |
| Búsqueda por pertenencia | Buena | Muy rápida |

---

# AI Engineering

Los conjuntos aparecen constantemente en sistemas de IA y procesamiento de datos.

| Caso | Uso |
|------|-----|
| RAG | Eliminar documentos duplicados recuperados |
| Embeddings | Evitar procesar dos veces el mismo archivo |
| NLP | Obtener vocabularios únicos de un corpus |
| APIs | Detectar identificadores repetidos |
| ETL | Limpiar datos antes del procesamiento |
| Machine Learning | Eliminar categorías duplicadas |

### Caso práctico

Eliminar documentos repetidos antes de generar embeddings.

```python
documentos = [
    "manual.pdf",
    "manual.pdf",
    "contrato.pdf",
    "reporte.pdf"
]

documentos_unicos = list(set(documentos))
```

Esto evita procesar varias veces el mismo documento y reduce el consumo de tiempo y recursos.

---

# Problemas reales en producción

## Problema 1

Intentar acceder por índice.

```python
frutas[0]
```

Resultado.

```text
TypeError
```

Los conjuntos no poseen índices.

---

## Problema 2

Suponer que el orden siempre será el mismo.

```python
for elemento in conjunto:
```

El orden puede variar entre ejecuciones e incluso cambiar tras agregar o eliminar elementos.

---

## Problema 3

Utilizar `remove()` cuando el elemento podría no existir.

```python
frutas.remove("limón")
```

Resultado.

```text
KeyError
```

En estos casos suele ser preferible utilizar `discard()`.

---

## Problema 4

Eliminar duplicados convirtiendo una lista en conjunto y esperar conservar el orden.

```python
list(set(lista))
```

Aunque elimina correctamente los duplicados, el orden original no está garantizado.

---

# Buenas prácticas

- Utiliza conjuntos cuando la unicidad de los elementos sea más importante que su orden.
- Emplea `discard()` si no tienes certeza de que el elemento exista.
- Reserva `remove()` para situaciones en las que la ausencia del elemento represente un error lógico.
- No utilices `pop()` si necesitas eliminar un valor específico.
- Convierte listas en conjuntos para eliminar duplicados de forma sencilla, teniendo presente que el orden puede cambiar.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`pop()` elimina un elemento aleatorio"

### Corrección técnica

Desde el punto de vista del programador, el elemento eliminado es **arbitrario**, ya que no existe un orden definido en el conjunto. Internamente, Python elimina un elemento según la organización de su tabla hash, por lo que el resultado no debe considerarse predecible ni utilizarse cuando importe qué elemento se elimina.

---

## Corrección 2. "`update()` solo acepta otros conjuntos"

### Corrección técnica

No. `update()` acepta cualquier **iterable**, incluyendo listas, tuplas, cadenas, generadores e incluso otros conjuntos.

Ejemplo.

```python
frutas.update("uva")
```

Resultado.

```text
{'u', 'v', 'a', ...}
```

En este caso, la cadena se recorre carácter por carácter, ya que las cadenas también son iterables.

---

## Corrección 3. "Convertir una lista en `set` y luego otra vez en `list` es la mejor forma de eliminar duplicados"

### Corrección técnica

Es una solución rápida, pero **no conserva el orden original**. Si el orden es importante, una alternativa moderna consiste en utilizar un diccionario, ya que desde Python 3.7 mantiene el orden de inserción.

```python
lista = [1, 2, 2, 3, 3, 4]

lista_limpia = list(dict.fromkeys(lista))
```

Resultado.

```text
[1, 2, 3, 4]
```

Esta técnica elimina duplicados preservando el orden original.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuándo utilizarías un `set` en lugar de una lista?

### Qué evalúa

Capacidad para elegir la estructura de datos adecuada.

### Errores comunes

- Responder únicamente "porque elimina duplicados".

### Respuesta de alto impacto

> Utilizaría un `set` cuando necesite garantizar la unicidad de los elementos, realizar búsquedas rápidas de pertenencia o aplicar operaciones de teoría de conjuntos como unión e intersección. Si el orden o los índices son importantes, preferiría una lista.

---

## Pregunta 2

¿Cuál es la diferencia entre `remove()` y `discard()`?

### Qué evalúa

Conocimiento de los métodos fundamentales de los conjuntos.

### Errores comunes

- Pensar que ambos tienen exactamente el mismo comportamiento.

### Respuesta de alto impacto

> Ambos eliminan un elemento del conjunto, pero `remove()` lanza una excepción (`KeyError`) si el elemento no existe, mientras que `discard()` ignora silenciosamente esa situación. Elegir uno u otro depende de si la ausencia del elemento debe considerarse un error de lógica o un caso esperado.

---

## Pregunta 3

¿Por qué los conjuntos ofrecen búsquedas tan rápidas?

### Qué evalúa

Comprensión del funcionamiento interno de Python.

### Errores comunes

- Responder que simplemente "Python está optimizado".

### Respuesta de alto impacto

> Porque los conjuntos están implementados mediante tablas hash. Antes de almacenar o buscar un elemento, Python calcula su valor hash, lo que permite localizarlo directamente sin recorrer toda la colección. Gracias a este diseño, las operaciones de pertenencia suelen ejecutarse en tiempo constante promedio.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `set`.
- Python Documentation — Set Types.
- Python Documentation — Built-in Types.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 218** — Adding a Built-In Set Object Type.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.