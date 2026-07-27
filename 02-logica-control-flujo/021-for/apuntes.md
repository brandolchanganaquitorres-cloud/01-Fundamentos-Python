# Clase 21. El Bucle `for` en Python (`for`, `range`, `break`, `continue`, `else` y `pass`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo funciona el bucle `for` en Python, recorrer distintos tipos de secuencias iterables, utilizar `range()`, controlar la ejecución mediante `break`, `continue`, `else` y `pass`, y entender cuándo utilizar `for` en lugar de `while`.

---

# Contenido del curso

El **bucle `for`** permite recorrer automáticamente cada elemento de una colección o secuencia.

A diferencia del `while`, donde el programador controla cuándo termina el bucle mediante una condición, el `for` finaliza automáticamente cuando ya no existen más elementos por recorrer.

Es una de las estructuras más utilizadas en Python y aparece constantemente en:

- procesamiento de datos;
- Machine Learning;
- Inteligencia Artificial;
- automatización;
- APIs;
- análisis de archivos;
- procesamiento de texto.

---

# Sintaxis básica

```python
for elemento in secuencia:
    # código
```

Python toma un elemento de la secuencia en cada iteración y lo asigna temporalmente a la variable indicada.

---

# Primer ejemplo

```python
palabra = "Python"

for letra in palabra:
    print(letra)
```

Resultado:

```text
P
y
t
h
o
n
```

Cada iteración obtiene una letra distinta hasta recorrer completamente la cadena.

---

# Funcionamiento interno

```text
Cadena

↓

"P"

↓

Imprimir

↓

"Siguiente carácter"

↓

"y"

↓

Imprimir

↓

...

↓

Fin de la secuencia

↓

Salir del for
```

El programador no necesita incrementar ningún contador.

---

# ¿Qué significa `in`?

El operador:

```python
in
```

indica que Python debe recorrer todos los elementos del objeto iterable.

En este caso:

```python
for letra in palabra
```

significa:

> "Para cada letra contenida en la variable `palabra`."

---

# Recorriendo listas

```python
frutas = [
    "manzana",
    "naranja",
    "kiwi"
]

for fruta in frutas:
    print(fruta)
```

Resultado.

```text
manzana
naranja
kiwi
```

---

# Convención de nombres

Es recomendable utilizar:

```text
frutas

↓

Colección
```

y

```text
fruta

↓

Elemento individual
```

Esta convención mejora considerablemente la legibilidad del código.

---

# La sentencia `break`

`break` termina inmediatamente el bucle.

```python
frutas = [
    "manzana",
    "naranja",
    "kiwi"
]

for fruta in frutas:

    if fruta == "naranja":
        break

    print(fruta)
```

Resultado.

```text
manzana
```

Cuando Python encuentra `"naranja"` finaliza el bucle.

---

# La sentencia `continue`

`continue` omite únicamente la iteración actual.

```python
for fruta in frutas:

    if fruta == "naranja":
        continue

    print(fruta)
```

Resultado.

```text
manzana
kiwi
```

La naranja se omite, pero el recorrido continúa normalmente.

---

# Funcionamiento de `continue`

```text
Elemento actual

↓

¿Debe omitirse?

↓

Sí

↓

continue

↓

Siguiente elemento
```

No finaliza el bucle.

---

# La cláusula `else`

Los bucles `for` también admiten un bloque `else`.

```python
for fruta in frutas:
    print(fruta)

else:
    print("Hemos terminado el recorrido.")
```

Resultado.

```text
manzana
naranja
kiwi
Hemos terminado el recorrido.
```

---

# ¿Cuándo se ejecuta el `else`?

Únicamente cuando el `for` termina de forma natural.

```text
Recorrer todos los elementos

↓

No quedan más elementos

↓

Ejecutar else
```

---

# ¿Cuándo NO se ejecuta?

Si el bucle termina mediante `break`.

```python
for fruta in frutas:

    if fruta == "naranja":
        break

else:
    print("Finalizó")
```

El bloque `else` nunca se ejecuta.

---

# La función `range()`

`range()` genera secuencias de números.

Es probablemente la función más utilizada junto con `for`.

---

# Forma 1

```python
range(10)
```

Produce:

```text
0
1
2
3
4
5
6
7
8
9
```

El límite superior **no se incluye**.

---

# Forma 2

```python
range(3, 5)
```

Produce:

```text
3
4
```

Comienza en el primer número.

Finaliza antes del segundo.

---

# Forma 3

```python
range(0, 10, 2)
```

Produce.

```text
0
2
4
6
8
```

El tercer parámetro representa el incremento.

---

# ¿Cómo incluir el último número?

Si queremos llegar hasta el 10.

```python
range(0, 11, 2)
```

Resultado.

```text
0
2
4
6
8
10
```

La regla general es sencilla:

> **`range()` siempre excluye el límite superior.**

---

# Expansión técnica

Internamente, `range()` **no crea una lista con todos los números**. Genera un objeto especial que produce cada valor cuando el `for` lo necesita.

```text
range

↓

Objeto range

↓

Generar siguiente número

↓

Generar siguiente número

↓

...
```

Gracias a este diseño, `range()` consume muy poca memoria incluso cuando representa millones de valores.

---

# Recorriendo un `range`

```python
for numero in range(5):
    print(numero)
```

Resultado.

```text
0
1
2
3
4
```

---

# Bucles anidados

Es posible colocar un `for` dentro de otro.

```python
adjetivos = [
    "rica",
    "saludable"
]

frutas = [
    "manzana",
    "naranja",
    "kiwi"
]

for adjetivo in adjetivos:

    for fruta in frutas:

        print(fruta, adjetivo)
```

Resultado.

```text
manzana rica
naranja rica
kiwi rica
manzana saludable
naranja saludable
kiwi saludable
```

---

# ¿Por qué ocurre ese orden?

El bucle externo controla cuándo comienza una nueva serie.

```text
Adjetivo

↓

Recorrer TODAS las frutas

↓

Siguiente adjetivo

↓

Recorrer TODAS las frutas
```

---

# Cambiando el orden

Si invertimos los bucles.

```python
for fruta in frutas:

    for adjetivo in adjetivos:

        print(fruta, adjetivo)
```

Resultado.

```text
manzana rica
manzana saludable
naranja rica
naranja saludable
kiwi rica
kiwi saludable
```

El orden cambia completamente.

---

# La sentencia `pass`

Un bloque vacío produce un error.

Incorrecto.

```python
for i in range(10):
```

Resultado.

```text
IndentationError
```

---

# Utilizando `pass`

```python
for i in range(10):
    pass
```

El programa continúa ejecutándose sin realizar ninguna acción.

---

# ¿Para qué sirve `pass`?

`pass` funciona como un **placeholder** durante el desarrollo.

Permite definir primero la estructura del programa y completar la implementación posteriormente.

---

# ¿Cuándo utilizar `for` y cuándo `while`?

| `for` | `while` |
|--------|----------|
| Recorre una secuencia | Repite mientras una condición sea verdadera |
| Número de iteraciones generalmente conocido por la secuencia | Número de iteraciones normalmente desconocido |
| No requiere actualizar manualmente un contador | Suele requerir una variable de control |
| Ideal para iterar colecciones | Ideal para esperar eventos o condiciones |

---

# AI Engineering

El bucle `for` es una de las estructuras más utilizadas en aplicaciones de IA.

| Caso | Uso |
|------|-----|
| Embeddings | Procesar documentos uno por uno |
| APIs | Enviar múltiples solicitudes |
| Machine Learning | Recorrer conjuntos de entrenamiento |
| RAG | Indexar documentos |
| Automatización | Procesar archivos de una carpeta |
| Agentes | Ejecutar varias herramientas en secuencia |

### Caso práctico

Procesar múltiples documentos antes de generar embeddings.

```python
documentos = [
    "manual.pdf",
    "contrato.pdf",
    "reporte.pdf"
]

for documento in documentos:
    generar_embedding(documento)
```

Este patrón aparece constantemente en pipelines de IA y sistemas RAG.

---

# Problemas reales en producción

## Problema 1

Modificar una colección mientras se está recorriendo.

```python
for usuario in usuarios:
    usuarios.remove(usuario)
```

Puede provocar elementos omitidos y resultados inesperados.

---

## Problema 2

Esperar que `range(10)` incluya el 10.

```python
range(10)
```

Resultado.

```text
0...9
```

El límite superior nunca se incluye.

---

## Problema 3

Esperar que `else` se ejecute después de un `break`.

```python
for x in datos:
    break
else:
    print("Fin")
```

El bloque `else` no se ejecutará.

---

## Problema 4

Utilizar un `for` cuando realmente se necesita un `while`.

Ejemplo.

```python
Esperar una conexión de red.
```

Aquí no existe una colección para recorrer; la repetición depende de una condición cambiante. Un `while` resulta más apropiado.

---

# Buenas prácticas

- Utiliza nombres descriptivos para la variable de iteración (`fruta`, `usuario`, `archivo`).
- Prefiere `for` cuando recorras una colección y `while` cuando dependas de una condición.
- Utiliza `break` únicamente cuando exista una condición clara de salida.
- Emplea `continue` para omitir casos específicos sin detener el recorrido.
- Recuerda que `range()` excluye siempre el límite superior.
- Utiliza `pass` solo como solución temporal durante el desarrollo.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`range()` genera una lista"

### Corrección técnica

No. `range()` devuelve un objeto de tipo `range`, que genera los valores de forma perezosa (*lazy evaluation*). Esto reduce considerablemente el consumo de memoria en comparación con crear una lista completa.

Ejemplo.

```python
print(type(range(10)))
```

Resultado.

```python
<class 'range'>
```

---

## Corrección 2. "`for` funciona únicamente con listas"

### Corrección técnica

`for` puede recorrer cualquier objeto **iterable**, incluyendo:

- cadenas (`str`);
- listas (`list`);
- tuplas (`tuple`);
- diccionarios (`dict`);
- conjuntos (`set`);
- objetos `range`;
- archivos;
- generadores;
- cualquier objeto que implemente el protocolo de iteración.

---

## Corrección 3. "`break` termina únicamente la iteración actual"

### Corrección técnica

No. `break` finaliza completamente el bucle más interno en el que se encuentra. Para omitir solo una iteración debe utilizarse `continue`.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuándo utilizarías un `for` en lugar de un `while`?

### Qué evalúa

Capacidad para seleccionar la estructura de repetición adecuada.

### Errores comunes

- Pensar que ambas estructuras son completamente intercambiables.

### Respuesta de alto impacto

> Utilizaría `for` cuando necesite recorrer una colección o un objeto iterable, ya que el propio lenguaje gestiona la iteración. Reservaría `while` para procesos cuya duración dependa de una condición dinámica, como esperar una conexión, procesar eventos o implementar reintentos.

---

## Pregunta 2

¿Por qué `range()` consume poca memoria incluso con valores muy grandes?

### Qué evalúa

Conocimiento del funcionamiento interno de Python.

### Errores comunes

- Creer que `range()` construye una lista con todos los números.

### Respuesta de alto impacto

> Porque `range()` no almacena todos los valores en memoria. Devuelve un objeto que calcula cada número cuando es necesario, siguiendo un enfoque de evaluación perezosa (*lazy evaluation*), lo que permite representar secuencias enormes con un consumo de memoria mínimo.

---

## Pregunta 3

¿Qué ocurre cuando un `break` aparece dentro de un `for` anidado?

### Qué evalúa

Comprensión del flujo de ejecución.

### Errores comunes

- Pensar que todos los bucles terminan simultáneamente.

### Respuesta de alto impacto

> `break` solo finaliza el bucle más interno en el que se encuentra. Los bucles externos continúan ejecutándose normalmente, salvo que también reciban una instrucción que modifique su flujo.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — The `for` Statement.
- Python Documentation — `range()`.
- Python Documentation — Iterators.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 234** — Iterators.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.