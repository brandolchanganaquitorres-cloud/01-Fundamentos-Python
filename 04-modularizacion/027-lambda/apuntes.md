# Clase 27. Funciones Lambda en Python (`lambda`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender qué son las funciones lambda en Python, aprender su sintaxis, trabajar con uno o varios argumentos, entender el concepto de funciones anónimas y descubrir cómo construir funciones especializadas mediante cierres (*closures*) utilizando `lambda`.

---

# Contenido del curso

Una **función lambda** es una función **anónima**, es decir, una función que no necesita un nombre para ser creada.

Su propósito es representar operaciones pequeñas y simples utilizando una sintaxis muy compacta.

Las funciones lambda poseen las siguientes características:

- No tienen nombre.
- Pueden recibir uno o varios argumentos.
- Solo pueden contener **una única expresión**.
- Devuelven automáticamente el resultado de esa expresión.

---

# Sintaxis de una función lambda

La sintaxis general es:

```python
lambda argumentos: expresión
```

Por ejemplo.

```python
lambda x: x + 10
```

No existe la palabra `return`.

Python devuelve automáticamente el resultado de la expresión.

---

# Comparación con una función tradicional

Función tradicional.

```python
def sumar_diez(a):
    return a + 10
```

Función lambda equivalente.

```python
lambda a: a + 10
```

Ambas realizan exactamente la misma operación.

La diferencia es únicamente la sintaxis.

---

# Una lambda con un argumento

```python
x = lambda a: a + 10

print(x(5))
```

Resultado.

```text
15
```

---

# Funcionamiento interno

```text
Llamada

↓

a = 5

↓

Evaluar

a + 10

↓

15

↓

Devolver resultado
```

Toda la evaluación ocurre en una única expresión.

---

# ¿Qué contiene realmente la variable?

Aunque visualmente parezca una expresión matemática, en realidad la variable almacena una función.

```python
x = lambda a: a + 10
```

Puede comprobarse.

```python
print(type(x))
```

Resultado.

```python
<class 'function'>
```

Las funciones lambda son objetos de tipo `function`, exactamente igual que las funciones creadas con `def`.

---

# Lambda con varios argumentos

Las funciones lambda pueden recibir múltiples argumentos.

```python
x = lambda a, b: a + b

print(x(2, 3))
```

Resultado.

```text
5
```

---

# Funcionamiento interno

```text
2

↓

a
```

```text
3

↓

b
```

↓

Evaluar

```text
a + b
```

↓

Resultado

```text
5
```

---

# Comparación con una función tradicional

```python
def sumar(a, b):
    return a + b
```

Equivale a:

```python
lambda a, b: a + b
```

Cuando la lógica consiste únicamente en una expresión sencilla, ambas producen el mismo resultado.

---

# Restricción de las funciones lambda

Las funciones lambda **solo pueden contener una expresión**.

Esto es válido.

```python
lambda x: x * 2
```

Pero esto no.

```python
lambda x:
    print(x)
    return x
```

Resultado.

```text
SyntaxError
```

Si la lógica requiere varias instrucciones, debe utilizarse una función tradicional con `def`.

---

# Funciones que devuelven funciones

Una función puede devolver otra función.

```python
def mi_funcion(n):
    return lambda a: a * n
```

En este ejemplo ocurre algo muy interesante.

La función no devuelve un número.

Devuelve **otra función**.

---

# Funcionamiento interno

```text
mi_funcion(2)

↓

Crear lambda

↓

Guardar n = 2

↓

Devolver función
```

Posteriormente.

```text
duplicador(5)

↓

5 × 2

↓

10
```

---

# Crear un duplicador

```python
duplicador = mi_funcion(2)

print(duplicador(5))
```

Resultado.

```text
10
```

---

# Crear un triplicador

```python
triplicador = mi_funcion(3)

print(triplicador(5))
```

Resultado.

```text
15
```

---

# Crear un quíntuplicador

Siguiendo exactamente el mismo patrón.

```python
quintuplador = mi_funcion(5)

print(quintuplador(8))
```

Resultado.

```text
40
```

La función original puede reutilizarse para generar cualquier multiplicador.

---

# ¿Qué está ocurriendo realmente?

Cuando se ejecuta:

```python
duplicador = mi_funcion(2)
```

Python recuerda el valor de `n`.

Más adelante.

```python
duplicador(8)
```

La función continúa teniendo acceso al valor `2`, aunque `mi_funcion()` ya terminó de ejecutarse.

Este comportamiento recibe el nombre de **closure** (cierre).

---

# Expansión técnica: Closures

Un **closure** es una función que conserva acceso a las variables del entorno donde fue creada, incluso después de que la función externa haya finalizado.

```text
mi_funcion(2)

↓

n = 2

↓

Crear lambda

↓

Guardar referencia a n

↓

Devolver función
```

Más adelante.

```text
duplicador(8)

↓

Usar n = 2

↓

16
```

Los closures son una característica fundamental de Python y aparecen con frecuencia en bibliotecas modernas.

---

# ¿Cuándo utilizar lambda?

Las funciones lambda son apropiadas cuando:

- la operación es muy pequeña;
- únicamente existe una expresión;
- la función será utilizada una sola vez;
- una API solicita una función como argumento.

Cuando la lógica crece, es preferible utilizar `def`.

---

# ¿Cuándo NO utilizar lambda?

No es recomendable utilizar una lambda cuando:

- existen múltiples pasos;
- se necesitan variables intermedias;
- debe escribirse documentación;
- la función será reutilizada ampliamente;
- la legibilidad disminuye.

En estos casos una función tradicional resulta más clara y mantenible.

---

# AI Engineering

Las funciones lambda aparecen con mucha frecuencia en bibliotecas relacionadas con IA y procesamiento de datos.

| Caso | Uso |
|------|-----|
| Ordenar resultados | Función `key` en `sort()` o `sorted()` |
| Procesamiento de datos | Transformaciones rápidas |
| Pandas | Aplicar funciones sobre columnas |
| Machine Learning | Funciones de transformación |
| LangChain | Funciones simples de procesamiento |
| Automatización | Operaciones puntuales dentro de pipelines |

### Caso práctico

Ordenar documentos por puntuación de relevancia.

```python
documentos.sort(
    key=lambda doc: doc["score"],
    reverse=True
)
```

La lambda indica cuál es el criterio utilizado para ordenar.

Este patrón aparece con frecuencia en sistemas RAG y motores de búsqueda.

---

# Problemas reales en producción

## Problema 1

Abusar de las funciones lambda.

```python
lambda x: ...
```

Una lambda demasiado compleja suele ser difícil de leer y mantener.

---

## Problema 2

Intentar escribir varias instrucciones.

```python
lambda x:
    ...
```

Resultado.

```text
SyntaxError
```

Las lambdas admiten únicamente una expresión.

---

## Problema 3

Asignar una lambda a una variable para reutilizarla en todo el proyecto.

```python
sumar = lambda a, b: a + b
```

Aunque es válido, **PEP 8** recomienda utilizar una función con `def` cuando la función necesita un nombre permanente. Esto mejora la legibilidad, facilita el depurado y produce trazas de error más informativas.

---

## Problema 4

Confundir una lambda con una ejecución inmediata.

```python
x = lambda a: a + 10
```

Aquí no se ejecuta ninguna operación.

La ejecución ocurre únicamente cuando se llama.

```python
x(5)
```

---

# Buenas prácticas

- Utiliza `lambda` únicamente para expresiones pequeñas y claras.
- Prefiere `def` cuando la función tenga varias instrucciones o vaya a reutilizarse ampliamente.
- Aprovecha las lambdas como argumentos en funciones que esperan otra función.
- Mantén las expresiones simples para preservar la legibilidad.
- No sustituyas sistemáticamente todas las funciones por lambdas; cada herramienta tiene su propósito.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "Las lambdas son mejores porque escriben menos código"

### Corrección técnica

No necesariamente.

El criterio principal debe ser la **legibilidad**, no la cantidad de caracteres escritos. Una función tradicional suele ser preferible cuando tiene un nombre descriptivo o contiene lógica que podría evolucionar.

---

## Corrección 2. "Las lambdas son funciones especiales"

### Corrección técnica

No. Las lambdas crean objetos del mismo tipo que las funciones definidas con `def`.

```python
type(lambda x: x)
```

Resultado.

```python
<class 'function'>
```

La principal diferencia es que las lambdas son anónimas y están limitadas a una única expresión.

---

## Corrección 3. "La fábrica de funciones devuelve una lambda"

### Corrección técnica

Desde el punto de vista del lenguaje, la función no devuelve "una lambda", sino un **objeto función** que mantiene un cierre (*closure*) sobre la variable `n`. Este mecanismo permite que la función recuerde el valor capturado incluso después de finalizar la ejecución de la función externa.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre una función creada con `def` y una función `lambda`?

### Qué evalúa

Comprensión de las diferencias sintácticas y de uso.

### Errores comunes

- Responder que una lambda es más rápida.

### Respuesta de alto impacto

> Ambas crean objetos de tipo `function`. La diferencia principal es que una lambda es una función anónima limitada a una única expresión, mientras que `def` permite múltiples instrucciones, documentación, anotaciones y un nombre descriptivo, por lo que suele ser la opción recomendada para funciones reutilizables.

---

## Pregunta 2

¿Qué es un closure y por qué es importante?

### Qué evalúa

Conocimiento del funcionamiento interno de las funciones.

### Errores comunes

- Confundirlo con una variable global.

### Respuesta de alto impacto

> Un closure es una función que conserva acceso a las variables del entorno donde fue creada, incluso después de que ese entorno haya terminado de ejecutarse. Este mecanismo permite construir fábricas de funciones, decoradores y otras técnicas avanzadas utilizadas ampliamente en Python.

---

## Pregunta 3

¿Por qué PEP 8 recomienda evitar asignar lambdas a variables?

### Qué evalúa

Conocimiento de buenas prácticas del lenguaje.

### Errores comunes

- Pensar que es un error de sintaxis.

### Respuesta de alto impacto

> Porque si una función necesita un nombre permanente, resulta más claro definirla con `def`. Esto mejora la legibilidad del código, facilita el mantenimiento y proporciona mejores nombres en los mensajes de error y durante el depurado.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Lambda Expressions.
- Python Documentation — Functional Programming Tools.
- Python Documentation — Functions.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 3107** — Function Annotations (relacionado con funciones modernas).

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.
```