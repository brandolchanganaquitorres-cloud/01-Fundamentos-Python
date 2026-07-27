# Clase 12. Indexación, Slicing y Manipulación de Strings en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo acceder, extraer, modificar y normalizar cadenas de texto mediante indexación, slicing y los métodos `replace()`, `split()` y `lower()`, aplicando estas técnicas en escenarios reales de desarrollo de software e Inteligencia Artificial.

---

# Contenido del curso

En Python, un **string** puede tratarse como una secuencia ordenada de caracteres.

Esto permite:

- acceder a caracteres individuales;
- extraer fragmentos de texto;
- reemplazar palabras;
- dividir cadenas;
- realizar búsquedas confiables.

Estas operaciones son fundamentales para el procesamiento de texto y aparecen constantemente en aplicaciones web, APIs, automatización y sistemas de IA.

---

# Indexación en Strings

Cada carácter de una cadena posee una posición denominada **índice**.

Python utiliza **indexación base cero**, por lo que el primer carácter siempre ocupa la posición `0`.

```python
texto = "Este es un texto"

print(texto[0])
```

Resultado:

```python
E
```

---

# Los espacios también tienen índice

Los espacios forman parte del string y ocupan una posición como cualquier otro carácter.

```python
texto = "Este es un texto"

print(texto[4])
```

Resultado:

```text
' '
```

---

# Visualizando los índices

```text
Texto:

E  s  t  e     e  s     u  n     t  e  x  t  o
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
```

Cada posición puede accederse mediante corchetes.

```python
print(texto[11])
```

Resultado:

```text
t
```

---

# Expansión técnica

Los strings en Python implementan el protocolo de **secuencia**, lo que significa que pueden recorrerse y accederse mediante índices, igual que listas y tuplas.

Internamente:

```text
String

↓

Secuencia ordenada

↓

Índice

↓

Carácter
```

Este diseño permite reutilizar una sintaxis consistente en distintos tipos de datos.

---

# Problema común

Intentar acceder a una posición inexistente.

```python
texto = "Python"

print(texto[20])
```

Resultado:

```text
IndexError: string index out of range
```

Siempre debe verificarse que el índice exista antes de acceder a él.

---

# Slicing

El **slicing** permite extraer una parte de una cadena.

Su sintaxis es:

```python
cadena[inicio:fin]
```

El carácter ubicado en `inicio` sí se incluye.

El carácter ubicado en `fin` **no** se incluye.

---

# Extraer una palabra

```python
texto = "Este es un texto"

print(texto[0:4])
```

Resultado:

```text
Este
```

Python toma:

```text
0
1
2
3
```

pero no toma el índice `4`.

---

# ¿Por qué el final no se incluye?

El rango funciona igual que la función `range()`.

```python
range(0,4)
```

produce:

```text
0
1
2
3
```

Esta consistencia simplifica el aprendizaje del lenguaje.

---

# Omitir el inicio

Si el inicio se omite, Python comienza desde el primer carácter.

```python
print(texto[:7])
```

Resultado:

```text
Este es
```

---

# Omitir el final

Si el final se omite, Python continúa hasta el último carácter.

```python
print(texto[5:])
```

Resultado:

```text
es un texto
```

---

# Índices negativos

Python permite contar desde el final.

```text
-1  Último carácter

-2  Penúltimo

-3  Antepenúltimo
```

Ejemplo.

```python
texto = "Python"

print(texto[-1])
```

Resultado:

```text
n
```

---

# Slicing con índices negativos

```python
texto = "Este es un texto"

print(texto[5:-2])
```

Resultado:

```text
es un tex
```

El índice `-2` no se incluye, siguiendo la misma regla del slicing.

---

# Expansión técnica

Los índices negativos evitan tener que calcular manualmente la longitud del texto.

En lugar de escribir:

```python
texto[0:len(texto)-1]
```

puede utilizarse:

```python
texto[:-1]
```

El código resulta más legible y menos propenso a errores.

---

# Método `replace()`

Permite reemplazar una cadena por otra.

```python
curso = "Este curso es de JavaScript"

nuevo = curso.replace("JavaScript","Python")

print(nuevo)
```

Resultado:

```text
Este curso es de Python
```

---

# Reemplazo múltiple

`replace()` sustituye todas las apariciones del texto buscado.

```python
texto = "Python Python Python"

print(texto.replace("Python","IA"))
```

Resultado:

```text
IA IA IA
```

---

# Expansión técnica

`replace()` no modifica el string original.

Devuelve una nueva cadena.

```python
texto = "Python"

nuevo = texto.replace("P","J")
```

Después de ejecutar el código:

```python
texto
```

sigue siendo:

```text
Python
```

---

# Método `split()`

Convierte un string en una lista.

```python
texto = "Este es un texto"

palabras = texto.split(" ")

print(palabras)
```

Resultado:

```python
['Este', 'es', 'un', 'texto']
```

---

# Funcionamiento interno

```text
Texto

↓

Separador

↓

División

↓

Lista
```

Cada vez que Python encuentra el separador indicado genera un nuevo elemento de la lista.

---

# ¿Para qué sirve `split()`?

Es uno de los métodos más utilizados para:

- procesar archivos CSV;
- analizar logs;
- leer archivos TXT;
- tokenizar texto;
- procesar prompts;
- limpiar datos.

---

# Comparaciones con `lower()`

Python distingue entre mayúsculas y minúsculas.

```python
texto = "Python"

print("python" in texto)
```

Resultado:

```python
False
```

---

# Normalización

Una práctica habitual consiste en convertir ambos textos al mismo formato antes de compararlos.

```python
texto = "Este Texto tiene MAYÚSCULAS y minúsculas"

buscado = "mayúsculas"

print(buscado.lower() in texto.lower())
```

Resultado:

```python
True
```

---

# Expansión técnica

Este proceso recibe el nombre de **normalización de texto**.

Consiste en transformar la información antes de procesarla para evitar diferencias que no aportan significado.

Ejemplos comunes:

- convertir a minúsculas;
- eliminar espacios;
- eliminar caracteres especiales;
- unificar formatos.

La normalización mejora la calidad de los datos y reduce errores en comparaciones.

---

# AI Engineering

El procesamiento de texto es una de las tareas más frecuentes en aplicaciones de Inteligencia Artificial.

| Método | Uso en IA |
|---------|-----------|
| Indexación | Analizar caracteres específicos |
| Slicing | Dividir prompts y documentos |
| `replace()` | Sustituir variables en plantillas de prompts |
| `split()` | Tokenización básica y preprocesamiento |
| `lower()` | Normalización antes de búsquedas o clasificación |

### Caso práctico

Construcción dinámica de un prompt.

```python
plantilla = """
Resume el siguiente documento:

{documento}
"""

prompt = plantilla.replace("{documento}", contenido)
```

Este patrón es habitual al trabajar con OpenAI SDK, LangChain, LangGraph y otros frameworks de IA.

---

# Problemas reales en producción

## Problema 1

Acceder a un índice inexistente.

```python
texto[100]
```

Produce:

```text
IndexError
```

---

## Problema 2

Olvidar que el final del slicing no se incluye.

```python
texto[0:4]
```

Devuelve:

```text
Este
```

No incluye el carácter en la posición `4`.

---

## Problema 3

Comparar cadenas sin normalizar.

```python
"ADMIN"

!=

"admin"
```

Puede provocar fallos de autenticación o búsquedas incorrectas.

---

## Problema 4

Esperar que `replace()` modifique la variable.

```python
texto.replace("A","B")
```

No cambia el string original.

---

## Problema 5

Usar `split(" ")` sobre datos con múltiples espacios consecutivos.

```python
texto = "Python   IA"

print(texto.split(" "))
```

Resultado:

```python
['Python', '', '', 'IA']
```

En estos casos suele ser preferible utilizar `split()` sin argumentos, ya que trata cualquier cantidad de espacios en blanco consecutivos como un único separador.

```python
print(texto.split())
```

Resultado:

```python
['Python', 'IA']
```

---

# Buenas prácticas

- Utiliza índices negativos cuando trabajes desde el final de una cadena.
- Recuerda siempre que el límite final del slicing no se incluye.
- Normaliza texto antes de realizar comparaciones cuando el dominio lo permita.
- Guarda el resultado de `replace()` en una variable.
- Utiliza `split()` para convertir texto en listas antes de procesarlo.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`replace()` modifica el string"

### Corrección técnica

Los strings son **inmutables**. `replace()` devuelve una nueva cadena y el objeto original permanece sin cambios.

---

## Corrección 2. "`split(" ")` es siempre la mejor opción"

### Corrección técnica

Cuando únicamente se desea dividir por espacios en blanco, `split()` sin argumentos suele ser más robusto porque maneja múltiples espacios, tabulaciones y saltos de línea automáticamente.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué el slicing de Python no incluye el índice final?

### Qué evalúa

Comprensión del modelo de secuencias de Python.

### Errores comunes

- Creer que ambos límites son inclusivos.

### Respuesta de alto impacto

> El slicing utiliza intervalos semiabiertos `[inicio:fin)`, igual que `range()`. Este diseño mantiene consistencia en el lenguaje, simplifica los cálculos de longitud y reduce errores al trabajar con secuencias.

---

## Pregunta 2

¿Cuándo utilizarías índices negativos?

### Qué evalúa

Capacidad para escribir código más limpio y mantenible.

### Errores comunes

- Calcular manualmente `len(cadena)-1`.

### Respuesta de alto impacto

> Utilizaría índices negativos cuando necesite acceder a elementos cercanos al final de una secuencia sin depender de su longitud, ya que el código resulta más legible y resistente a cambios en el tamaño de la cadena.

---

## Pregunta 3

¿Por qué normalizarías un texto antes de buscar una palabra?

### Qué evalúa

Experiencia en procesamiento de datos.

### Errores comunes

- Comparar cadenas directamente ignorando diferencias de formato.

### Respuesta de alto impacto

> Porque los datos provenientes de usuarios o sistemas externos suelen tener diferencias de mayúsculas, espacios o formato. Normalizar previamente reduce falsos negativos y hace que las búsquedas sean más consistentes y confiables.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Text Sequence Type (`str`).
- Python Documentation — Common Sequence Operations.
- Python Documentation — String Methods (`replace`, `split`).

## PEPs

- PEP 8 — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.