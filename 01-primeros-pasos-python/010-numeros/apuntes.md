# Clase 10. Tipos numéricos, conversión de tipos y números aleatorios en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender los tipos numéricos de Python, aprender a identificar su tipo mediante `type()`, realizar conversiones seguras entre `int`, `float` y `complex`, entender los riesgos de pérdida de información durante el casteo y generar números pseudoaleatorios utilizando el módulo `random`.

---

# Contenido del curso

Python incorpora tres tipos numéricos fundamentales:

- `int` (**Integer**): números enteros.
- `float`: números con parte decimal.
- `complex`: números complejos.

Cada uno representa una categoría distinta de datos y posee un comportamiento específico.

---

# Tipos numéricos y verificación con `type()`

Python permite identificar el tipo exacto de cualquier objeto mediante la función incorporada `type()`.

```python
x = 1          # Entero
y = 2.5        # Flotante
z = 5 + 1j     # Complejo

print(type(x))
print(type(y))
print(type(z))
```

Salida:

```python
<class 'int'>
<class 'float'>
<class 'complex'>
```

La función `type()` resulta especialmente útil durante el desarrollo y el proceso de depuración, ya que permite verificar que una variable contiene el tipo de dato esperado.

---

# Expansión técnica

## ¿Qué hace realmente `type()`?

En Python prácticamente todo es un objeto.

Cuando ejecutamos:

```python
type(x)
```

Python devuelve la clase a partir de la cual fue creado ese objeto.

```text
Variable

↓

Objeto

↓

Clase

↓

type()
```

Por ejemplo:

```python
numero = 10

print(type(numero))
```

Resultado:

```python
<class 'int'>
```

Esto indica que `numero` es una instancia de la clase `int`.

---

## Caso real

Durante el consumo de APIs es frecuente recibir datos con tipos inesperados.

```python
edad = "30"

print(type(edad))
```

Aunque representa un número, realmente es una cadena de texto.

Verificar el tipo antes de procesar la información evita numerosos errores en producción.

---

# Enteros (`int`)

Los enteros representan números sin parte decimal.

Pueden ser positivos o negativos.

```python
edad = 30

saldo = -150
```

---

# Flotantes (`float`)

Los flotantes representan números reales con parte decimal.

Python utiliza el punto (`.`) como separador decimal.

```python
precio = 15.75

temperatura = -8.5
```

No debe utilizarse la coma.

Incorrecto:

```python
precio = 15,75
```

Esto crea una tupla, no un número decimal.

---

# Complejos (`complex`)

Los números complejos poseen:

- parte real;
- parte imaginaria.

La parte imaginaria se representa mediante la letra `j`.

```python
z = 5 + 2j

w = -8 - 3j
```

---

# Expansión técnica

Aunque los números complejos no son frecuentes en desarrollo web, tienen aplicaciones importantes en:

- procesamiento digital de señales;
- telecomunicaciones;
- simulaciones físicas;
- ingeniería eléctrica;
- computación científica.

Por ello Python incorpora soporte nativo para este tipo numérico.

---

# Conversión de tipos (Casting)

El **casting** consiste en convertir un objeto de un tipo de dato a otro.

Python proporciona funciones específicas para ello.

---

# Convertir un entero a flotante

```python
x = 1

xf = float(x)

print(xf)

print(type(xf))
```

Salida:

```python
1.0

<class 'float'>
```

El valor conserva su magnitud, pero ahora posee parte decimal.

---

# Convertir un flotante a entero

```python
y = 2.5

ye = int(y)

print(ye)

print(type(ye))
```

Salida:

```python
2

<class 'int'>
```

---

# Expansión técnica

## ¿Por qué `int()` devuelve `2` y no `3`?

La función `int()` **no redondea**.

Elimina completamente la parte decimal.

```text
2.9

↓

2
```

```text
-2.9

↓

-2
```

Este proceso recibe el nombre de **truncamiento**.

---

# Problema real en producción

Supongamos un sistema de pagos.

```python
monto = 199.99

total = int(monto)
```

Resultado:

```python
199
```

Se perdió información.

En aplicaciones financieras esto puede provocar errores de facturación o diferencias contables.

Cuando el decimal es importante, no debe utilizarse `int()` para convertir importes monetarios.

---

# Buenas prácticas

- Utiliza `int()` únicamente cuando realmente necesites eliminar la parte decimal.
- Si deseas redondear un número, utiliza `round()` en lugar de `int()`.

Ejemplo:

```python
round(2.5)
```

---

# Conversión hacia números complejos

Es posible convertir enteros y flotantes mediante `complex()`.

```python
entero = 5

flotante = 5.5

print(complex(entero))

print(complex(flotante))
```

Salida:

```python
(5+0j)

(5.5+0j)
```

Python agrega automáticamente una parte imaginaria igual a `0j`.

---

# Limitaciones de la conversión

Es posible convertir:

```text
int

↓

complex
```

y

```text
float

↓

complex
```

Sin embargo, el proceso inverso no está permitido.

```python
numero = 5 + 2j

int(numero)
```

Resultado:

```text
TypeError
```

Lo mismo ocurre con:

```python
float(numero)
```

---

# Expansión técnica

Un número complejo contiene dos componentes.

```text
Parte real

+

Parte imaginaria
```

Convertirlo directamente a un entero o flotante implicaría perder información.

Por ello Python obliga al desarrollador a decidir explícitamente qué componente utilizar (`real` o `imag`) antes de realizar cualquier conversión.

---

# Generación de números pseudoaleatorios

Python proporciona el módulo estándar `random`.

```python
import random
```

Una de sus funciones más utilizadas es `randrange()`.

```python
import random

print(random.randrange(1, 10))
```

Salida posible:

```python
7
```

Cada ejecución puede generar un resultado diferente.

---

# ¿Cómo funciona `randrange()`?

La sintaxis es:

```python
random.randrange(inicio, fin)
```

La función:

- incluye el valor inicial;
- excluye el valor final.

```python
random.randrange(1,10)
```

Puede devolver:

```text
1

2

3

...

9
```

Nunca devolverá:

```text
10
```

---

# Expansión técnica

## ¿Por qué el límite superior no se incluye?

Python sigue la misma convención utilizada por funciones como:

```python
range()
```

Ejemplo:

```python
range(1,10)
```

Genera:

```text
1 2 3 4 5 6 7 8 9
```

Mantener el mismo comportamiento hace que la API sea consistente y reduce errores al trabajar con índices y rangos.

---

# Producción

Es importante entender que `random` **no genera números verdaderamente aleatorios**.

Genera números **pseudoaleatorios**, es decir, calculados mediante un algoritmo determinista.

Esto es suficiente para:

- juegos;
- simulaciones;
- pruebas;
- ejemplos educativos.

No debe utilizarse para:

- generar contraseñas;
- tokens JWT;
- claves criptográficas;
- API Keys;
- códigos de recuperación.

Para esos casos Python proporciona el módulo:

```python
secrets
```

---

# Aplicación en AI Engineering

Estos conceptos aparecen constantemente en proyectos de IA.

| Tipo | Caso de uso |
|------|-------------|
| `int` | `max_tokens`, tamaño de lote (*batch size*), número de documentos |
| `float` | `temperature`, `top_p`, *learning rate*, umbrales de similitud |
| `complex` | Computación científica, procesamiento de señales y modelos matemáticos especializados |
| `type()` | Validación de datos provenientes de APIs y archivos |
| `random` | División de datasets, selección aleatoria de muestras y pruebas reproducibles |

### Caso práctico

Al preparar un conjunto de entrenamiento suele seleccionarse una muestra aleatoria.

```python
import random

indice = random.randrange(0, len(dataset))
```

Este patrón aparece en tareas de ciencia de datos y aprendizaje automático para realizar muestreos simples.

---

# Problemas reales en producción

## Problema 1

Perder decimales mediante `int()`.

```python
precio = 99.99

int(precio)
```

Resultado:

```python
99
```

---

## Problema 2

Intentar convertir directamente un número complejo.

```python
int(5+2j)
```

Produce:

```text
TypeError
```

---

## Problema 3

Esperar que `randrange(1,10)` pueda devolver `10`.

Nunca ocurrirá.

---

## Problema 4

Utilizar `random` para generar contraseñas.

No es un generador criptográficamente seguro.

Debe utilizarse:

```python
import secrets
```

---

# Buenas prácticas

- Utiliza `type()` durante el desarrollo para validar tipos de datos.
- Evita convertir un `float` a `int` si la precisión decimal es importante.
- Emplea `complex()` únicamente cuando el dominio del problema lo requiera.
- Recuerda que `randrange()` excluye el límite superior.
- Utiliza `secrets` cuando necesites generar valores seguros desde el punto de vista criptográfico.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "El casteo obliga a una variable a comportarse como otro tipo"

### Corrección técnica

La variable no cambia de comportamiento. Lo que ocurre es que funciones como `int()`, `float()` o `complex()` crean un **nuevo objeto** del tipo solicitado y devuelven una referencia a él. El objeto original permanece sin cambios.

---

## Corrección 2. "Los números aleatorios son aleatorios"

### Corrección técnica

El módulo `random` genera números **pseudoaleatorios** mediante un algoritmo determinista. Son adecuados para simulaciones y aplicaciones generales, pero no para usos relacionados con seguridad.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre truncar y redondear un número?

### Qué evalúa

Comprensión de la conversión de tipos y precisión numérica.

### Errores comunes

- Confundir `int()` con `round()`.

### Respuesta de alto impacto

> `int()` elimina la parte decimal mediante truncamiento, mientras que `round()` aproxima el valor siguiendo las reglas de redondeo. Elegir uno u otro depende del dominio del problema, especialmente en aplicaciones financieras y científicas.

---

## Pregunta 2

¿Por qué `type()` resulta útil durante el desarrollo?

### Qué evalúa

Capacidad para depurar y validar datos.

### Errores comunes

- Pensar que solo sirve con fines educativos.

### Respuesta de alto impacto

> `type()` permite verificar que los datos recibidos desde APIs, archivos o bases de datos tengan el tipo esperado antes de procesarlos, reduciendo errores de conversión y facilitando el debugging.

---

## Pregunta 3

¿Por qué `random.randrange(1,10)` nunca devuelve `10`?

### Qué evalúa

Comprensión de la API estándar de Python.

### Errores comunes

- Suponer que ambos límites son inclusivos.

### Respuesta de alto impacto

> `randrange()` sigue la misma convención que `range()`: incluye el límite inferior y excluye el superior. Esta decisión proporciona consistencia en el lenguaje y evita errores al trabajar con índices y rangos.

---

## Recursos recomendados

### Documentación oficial

- Python Documentation — Numeric Types.
- Python Documentation — Built-in Functions (`type`, `int`, `float`, `complex`).
- Python Documentation — `random`.
- Python Documentation — `secrets`.

### PEPs

- PEP 3141 — A Type Hierarchy for Numbers.
- PEP 8 — Style Guide for Python Code.

### Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.
```