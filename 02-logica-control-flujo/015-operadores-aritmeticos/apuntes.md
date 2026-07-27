# Clase 15. Operadores Aritméticos en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender el funcionamiento de los operadores aritméticos en Python, interpretar correctamente su precedencia, diferenciar la división normal de la división entera y aplicar estos conceptos en problemas reales de desarrollo de software e Inteligencia Artificial.

---

# Contenido del curso

Los **operadores aritméticos** permiten realizar operaciones matemáticas sobre variables y valores numéricos.

Son uno de los elementos más utilizados en cualquier lenguaje de programación y aparecen constantemente en:

- cálculos financieros;
- análisis de datos;
- algoritmos;
- videojuegos;
- Inteligencia Artificial;
- Machine Learning;
- procesamiento científico.

Tomaremos como ejemplo las siguientes variables.

```python
x = 5
y = 10
```

---

# Operador de suma (`+`)

Permite sumar dos valores.

```python
print("Suma:", x + y)
```

Resultado:

```python
15
```

También puede utilizarse para sumar variables, resultados de funciones y expresiones matemáticas.

---

# Operador de resta (`-`)

Permite calcular la diferencia entre dos valores.

```python
print("Resta:", x - y)
```

Resultado:

```python
-5
```

El orden de los operandos es importante.

```python
print(y - x)
```

Resultado:

```python
5
```

---

# Expansión técnica

Python evalúa las operaciones exactamente en el orden indicado.

```text
5 - 10

↓

-5
```

No existe ninguna corrección automática del signo.

---

# Operador de multiplicación (`*`)

La multiplicación utiliza el símbolo `*`.

```python
print(x * y)
```

Resultado:

```python
50
```

---

# ¿Por qué se utiliza `*` y no la letra "x"?

La letra `x` representa un identificador válido en Python.

```python
x = 10
```

Por ello, el lenguaje utiliza el asterisco como operador de multiplicación.

---

# Operador de división (`/`)

Realiza una división convencional.

```python
print(y / x)
```

Resultado:

```python
2.0
```

---

# Expansión técnica

Aunque el resultado matemático sea un número entero, el operador `/` **siempre devuelve un objeto de tipo `float`**.

```python
print(type(10 / 5))
```

Resultado:

```python
<class 'float'>
```

Esto garantiza un comportamiento consistente para todas las divisiones.

---

# Operador módulo (`%`)

El operador módulo devuelve el **residuo** de una división.

```python
print(12 % 5)
```

Resultado:

```python
2
```

Porque:

```text
12 ÷ 5

↓

Cociente = 2

Residuo = 2
```

---

# División exacta

```python
print(10 % 5)
```

Resultado:

```python
0
```

Cuando el residuo es cero, la división es exacta.

---

# Aplicación: determinar si un número es par

```python
numero = 8

print(numero % 2 == 0)
```

Resultado:

```python
True
```

Si el residuo de dividir entre dos es cero, el número es par.

---

# Producción

Este patrón aparece constantemente para:

- validar números pares;
- distribuir tareas entre servidores;
- paginar resultados;
- alternar colores en tablas;
- rotar registros;
- programación de turnos.

---

# Operador de potencia (`**`)

Eleva un número a una potencia.

```python
print(y ** x)
```

Resultado:

```python
100000
```

Equivale a:

```text
10⁵
```

---

# Expansión técnica

La potencia se utiliza frecuentemente en:

- matemáticas;
- estadística;
- física;
- Machine Learning;
- procesamiento científico.

Ejemplo.

```python
2 ** 10
```

Resultado:

```python
1024
```

---

# Operador de división entera (`//`)

Devuelve únicamente la parte entera del cociente.

```python
print(12 // 5)
```

Resultado:

```python
2
```

Mientras que:

```python
print(12 / 5)
```

Resultado:

```python
2.4
```

---

# Diferencia entre `/` y `//`

| Operador | Resultado |
|-----------|-----------|
| `/` | División real (`float`) |
| `//` | División entera (`int` en este ejemplo) |

Ejemplo.

```python
12 / 5
```

Resultado.

```text
2.4
```

Mientras que:

```python
12 // 5
```

Resultado.

```text
2
```

---

# Relación entre `//` y `%`

Ambos operadores representan la división completa.

```text
12 ÷ 5

↓

Cociente

↓

12 // 5

↓

2
```

y

```text
Residuo

↓

12 % 5

↓

2
```

---

# Expansión técnica

Muchos algoritmos utilizan ambos operadores simultáneamente.

Ejemplo.

Conversión de segundos.

```python
segundos = 3675

minutos = segundos // 60

resto = segundos % 60
```

---

# Precedencia de operadores

Python sigue un orden específico para evaluar expresiones.

1. Paréntesis `()`
2. Potencias `**`
3. Multiplicación `*`
4. División `/`
5. División entera `//`
6. Módulo `%`
7. Suma `+`
8. Resta `-`
9. Comparaciones
10. Operadores lógicos

---

# Ejemplo

```python
resultado = 2 + 3 * 4
```

Python realiza:

```text
3 × 4

↓

12

↓

2 + 12

↓

14
```

---

# Uso de paréntesis

Los paréntesis modifican el orden de evaluación.

```python
resultado = (2 + 3) * 4
```

Resultado:

```python
20
```

Porque primero se calcula:

```text
2 + 3

↓

5

↓

5 × 4

↓

20
```

---

# Expansión técnica

El uso de paréntesis no solo cambia el resultado.

También mejora la legibilidad del código y reduce errores durante el mantenimiento.

Incluso cuando Python puede inferir correctamente la precedencia, muchos equipos prefieren utilizar paréntesis para expresar claramente la intención del cálculo.

---

# AI Engineering

Las operaciones aritméticas aparecen continuamente en proyectos de IA.

| Operador | Caso de uso |
|-----------|-------------|
| `+` | Sumar métricas y contadores |
| `-` | Calcular diferencias de error |
| `*` | Escalar vectores y pesos |
| `/` | Promediar métricas |
| `%` | Distribuir tareas o identificar lotes |
| `**` | Operaciones matemáticas en algoritmos |
| `//` | Calcular cantidad de lotes (*batches*) |

### Caso práctico

Calcular el número de lotes para entrenar un modelo.

```python
dataset = 1050

batch_size = 128

batches = dataset // batch_size

print(batches)
```

Resultado:

```text
8
```

El residuo puede obtenerse mediante:

```python
dataset % batch_size
```

Para conocer cuántos datos quedan en el último lote.

---

# Problemas reales en producción

## Problema 1

Esperar que `/` devuelva un entero.

```python
10 / 5
```

Resultado:

```python
2.0
```

No devuelve `2`, sino un `float`.

---

## Problema 2

Confundir `%` con porcentaje.

```python
10 % 3
```

Resultado:

```python
1
```

El operador `%` calcula el residuo, no un porcentaje.

---

## Problema 3

Olvidar el orden de precedencia.

```python
2 + 3 * 4
```

Resultado:

```python
14
```

No:

```python
20
```

---

## Problema 4

Utilizar `//` esperando obtener decimales.

```python
7 // 2
```

Resultado:

```python
3
```

Los decimales se descartan.

---

# Buenas prácticas

- Utiliza paréntesis cuando una expresión pueda resultar ambigua.
- Emplea `%` para comprobar divisibilidad y calcular residuos.
- Utiliza `//` cuando únicamente necesites el cociente entero.
- Recuerda que `/` siempre devuelve un `float`.
- Escribe expresiones matemáticas simples y legibles en lugar de concentrar muchos operadores en una sola línea.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`//` elimina los decimales"

### Corrección técnica

Más precisamente, `//` realiza una **división entera mediante floor division**. En números positivos suele coincidir con eliminar la parte decimal, pero con números negativos el comportamiento difiere porque redondea hacia menos infinito.

Ejemplo.

```python
print(-7 // 2)
```

Resultado:

```python
-4
```

No:

```text
-3
```

Este comportamiento es importante en algoritmos que trabajan con valores negativos.

---

## Corrección 2. "La precedencia solo importa en operaciones matemáticas"

### Corrección técnica

La precedencia afecta a toda expresión, incluidas comparaciones y operadores lógicos. Comprenderla evita errores difíciles de detectar en condiciones complejas.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre `/` y `//`?

### Qué evalúa

Comprensión de los tipos numéricos y operadores aritméticos.

### Errores comunes

- Pensar que ambos operadores hacen exactamente lo mismo.

### Respuesta de alto impacto

> El operador `/` siempre devuelve una división real de tipo `float`, mientras que `//` realiza una división entera (*floor division*), devolviendo el cociente redondeado hacia menos infinito. Este último resulta especialmente útil para cálculos de paginación, lotes y distribución de recursos.

---

## Pregunta 2

¿Para qué utilizarías el operador `%` en una aplicación real?

### Qué evalúa

Capacidad para relacionar operadores con problemas prácticos.

### Errores comunes

- Asociarlo únicamente con el cálculo de porcentajes.

### Respuesta de alto impacto

> Lo utilizaría para comprobar divisibilidad, detectar números pares e impares, implementar paginación, distribuir cargas de trabajo entre procesos y calcular posiciones cíclicas en estructuras de datos.

---

## Pregunta 3

¿Por qué muchos equipos utilizan paréntesis incluso cuando no son obligatorios?

### Qué evalúa

Buenas prácticas de ingeniería de software.

### Errores comunes

- Pensar únicamente en el resultado matemático.

### Respuesta de alto impacto

> Porque los paréntesis hacen explícita la intención del cálculo, mejoran la legibilidad y reducen errores de mantenimiento. En equipos grandes es preferible escribir código claro antes que depender completamente de la precedencia implícita del lenguaje.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Numeric Types.
- Python Documentation — Expressions.
- Python Documentation — Arithmetic Operations.

## PEPs

- **PEP 8** — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.