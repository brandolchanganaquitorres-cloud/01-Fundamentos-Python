# Clase 16. Operadores de Asignación en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo funcionan los operadores de asignación en Python, aprender a actualizar variables de forma eficiente utilizando operadores compuestos (`+=`, `-=`, `*=`, `/=`, `%=`, `//=`, `**=`), conocer el operador Walrus (`:=`) y aplicarlos correctamente en código profesional.

---

# Contenido del curso

Los **operadores de asignación** permiten modificar el valor de una variable utilizando su valor actual.

En lugar de escribir operaciones largas, Python ofrece operadores compuestos que hacen el código más corto, más legible y menos propenso a errores.

---

# Asignación básica (`=`)

El operador `=` asigna un valor a una variable.

```python
x = 5

print(x)
```

Resultado:

```python
5
```

Es importante entender que `=` **no significa igualdad matemática**.

En programación significa:

> **"Asigna el valor de la derecha a la variable de la izquierda."**

---

# Expansión técnica

Cuando Python ejecuta:

```python
x = 5
```

ocurre el siguiente proceso:

```text
5

↓

Se crea un objeto entero

↓

La variable x referencia ese objeto
```

La variable no almacena literalmente el número; almacena una referencia al objeto creado.

---

# Operador `+=`

Permite sumar un valor y guardar automáticamente el resultado.

Forma tradicional:

```python
x = 5

x = x + 3
```

Forma abreviada:

```python
x = 5

x += 3
```

Resultado:

```python
8
```

Ambas instrucciones producen exactamente el mismo resultado.

---

# ¿Por qué utilizar `+=`?

Reduce repetición.

Comparación.

```python
saldo = saldo + deposito
```

vs.

```python
saldo += deposito
```

La segunda versión es más clara y fácil de mantener.

---

# Operador `-=`

Resta un valor y actualiza la variable.

```python
x = 8

x -= 3

print(x)
```

Resultado:

```python
5
```

---

# Operador `*=`

Multiplica el valor actual.

```python
x = 5

x *= 3

print(x)
```

Resultado:

```python
15
```

---

# Operador `/=`

Divide el valor actual.

```python
x = 15

x /= 3

print(x)
```

Resultado:

```python
5.0
```

---

# Expansión técnica

Aunque la división sea exacta:

```python
15 / 3
```

Python devuelve:

```python
5.0
```

Porque el operador `/` siempre produce un objeto de tipo `float`.

```python
print(type(x))
```

Resultado:

```python
<class 'float'>
```

---

# Operador `%=`

Calcula el residuo y actualiza la variable.

```python
x = 5

x %= 2

print(x)
```

Resultado:

```python
1
```

---

# Módulo sobre flotantes

```python
x = 5.0

x %= 2

print(x)
```

Resultado:

```python
1.0
```

El resultado conserva el tipo `float`.

---

# Operador `//=`

Realiza una división entera y almacena el resultado.

```python
y = 20

y //= 2

print(y)
```

Resultado:

```python
10
```

---

Si la división tiene parte decimal:

```python
y = 21

y //= 2

print(y)
```

Resultado:

```python
10
```

La parte decimal se descarta mediante **floor division**.

---

# Operador `**=`

Eleva la variable a una potencia.

```python
y = 10

y **= 3

print(y)
```

Resultado:

```python
1000
```

Equivale a:

```python
y = y ** 3
```

---

# Resumen de operadores de asignación

| Operador | Equivale a |
|-----------|------------|
| `=` | `x = valor` |
| `+=` | `x = x + valor` |
| `-=` | `x = x - valor` |
| `*=` | `x = x * valor` |
| `/=` | `x = x / valor` |
| `%=` | `x = x % valor` |
| `//=` | `x = x // valor` |
| `**=` | `x = x ** valor` |

---

# Operador Walrus (`:=`)

Introducido en **Python 3.8**, el operador Walrus permite **asignar un valor y utilizarlo en la misma expresión**.

```python
print(z := 3)
```

Resultado:

```python
3
```

Posteriormente:

```python
print(z)
```

Resultado:

```python
3
```

La variable fue creada durante la evaluación de la expresión.

---

# ¿Por qué se llama Walrus?

Su símbolo:

```python
:=
```

recuerda visualmente a los colmillos de una morsa (*walrus* en inglés).

Es simplemente un nombre informal; su nombre técnico es **Assignment Expression Operator**.

---

# Expansión técnica

Antes de Python 3.8 era necesario escribir:

```python
valor = calcular()

print(valor)
```

Con Walrus:

```python
print(valor := calcular())
```

La asignación y el uso del valor ocurren en una sola expresión.

---

# Funcionamiento interno

```text
Expresión

↓

Calcular valor

↓

Asignar variable

↓

Devolver el mismo valor

↓

Continuar evaluando
```

Esto permite reducir código repetitivo sin perder claridad cuando se utiliza correctamente.

---

# Producción

Un caso muy frecuente consiste en evitar ejecutar dos veces una función costosa.

Sin Walrus:

```python
texto = obtener_texto()

if texto:
    print(texto)
```

Con Walrus:

```python
if texto := obtener_texto():
    print(texto)
```

La función se ejecuta una única vez.

Esto mejora la eficiencia y evita duplicar llamadas innecesarias.

---

# AI Engineering

Los operadores de asignación aparecen constantemente en proyectos de IA.

| Operador | Caso de uso |
|-----------|-------------|
| `+=` | Acumular tokens procesados |
| `-=` | Reducir memoria disponible |
| `*=` | Ajustar pesos o escalas |
| `/=` | Calcular promedios de métricas |
| `%=` | Distribuir tareas entre procesos |
| `//=` | Calcular número de batches |
| `**=` | Operaciones matemáticas en modelos |
| `:=` | Evitar recalcular resultados costosos |

### Caso práctico

Acumular el número total de tokens procesados.

```python
tokens = 0

tokens += respuesta["usage"]["total_tokens"]
```

Este patrón aparece constantemente al consumir APIs de modelos de lenguaje.

---

# Problemas reales en producción

## Problema 1

Esperar que `/=` conserve el tipo entero.

```python
x = 6

x /= 2
```

Resultado:

```python
3.0
```

No:

```python
3
```

---

## Problema 2

Confundir `//=` con una simple eliminación de decimales.

```python
x = -7

x //= 2
```

Resultado:

```python
-4
```

No:

```python
-3
```

Porque realiza **floor division**, redondeando hacia menos infinito.

---

## Problema 3

Abusar del operador Walrus.

```python
if (x := f()) and (y := g()) and (z := h()):
```

Aunque es válido, reduce considerablemente la legibilidad.

Debe utilizarse únicamente cuando realmente simplifique el código.

---

## Problema 4

Olvidar que los operadores de asignación modifican la variable.

```python
contador += 1
```

Después de ejecutar la instrucción, el valor original ya no existe.

---

# Buenas prácticas

- Utiliza operadores compuestos para evitar repetir nombres de variables.
- Emplea `+=` y `-=` cuando actualices contadores o acumuladores.
- Recuerda que `/=` siempre genera un `float`.
- Utiliza `//=` únicamente cuando realmente necesites una división entera.
- Usa el operador Walrus con moderación; prioriza siempre la legibilidad del código.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`//=` ignora simplemente los decimales"

### Corrección técnica

`//=` realiza una **floor division**. En números positivos suele coincidir con eliminar la parte decimal, pero en números negativos redondea hacia menos infinito.

Ejemplo.

```python
print(-7 // 2)
```

Resultado:

```python
-4
```

---

## Corrección 2. "El operador Walrus sirve para escribir menos código"

### Corrección técnica

Su objetivo principal no es reducir líneas, sino **evitar repetir evaluaciones de una misma expresión**. Debe utilizarse únicamente cuando mejora la claridad y evita cálculos duplicados.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la ventaja de utilizar `+=` en lugar de `x = x + valor`?

### Qué evalúa

Buenas prácticas y legibilidad del código.

### Errores comunes

- Pensar que únicamente reduce caracteres.

### Respuesta de alto impacto

> Ambos producen el mismo resultado, pero `+=` expresa de forma más clara la intención de actualizar el valor existente, reduce la repetición y facilita el mantenimiento del código.

---

## Pregunta 2

¿Cuándo utilizarías el operador Walrus (`:=`)?

### Qué evalúa

Conocimiento de características modernas del lenguaje.

### Errores comunes

- Utilizarlo en cualquier asignación.

### Respuesta de alto impacto

> Lo utilizaría cuando una expresión necesita evaluarse una única vez y su resultado será reutilizado inmediatamente, por ejemplo al leer datos, procesar respuestas de APIs o validar funciones costosas dentro de una condición.

---

## Pregunta 3

¿Por qué `x /= 2` cambia el tipo de la variable?

### Qué evalúa

Comprensión del modelo numérico de Python.

### Errores comunes

- Esperar que siga siendo un entero.

### Respuesta de alto impacto

> Porque el operador `/` siempre realiza una división real y devuelve un objeto de tipo `float`, incluso cuando el resultado matemático sea un número entero. Si necesito conservar una división entera utilizaría `//=`.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Assignment Statements.
- Python Documentation — Assignment Expressions (`:=`).
- Python Documentation — Numeric Types.

## PEPs

- **PEP 572** — Assignment Expressions (Operador Walrus).
- **PEP 8** — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.