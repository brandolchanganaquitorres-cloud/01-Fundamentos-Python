# Clase 19. La Sentencia `match` en Python (Pattern Matching)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender el funcionamiento de la sentencia `match` introducida en Python 3.10, aprender a utilizar `case` y el caso por defecto (`_`) para simplificar estructuras condicionales, y conocer cuándo utilizar `match` en lugar de múltiples sentencias `if` y `elif`.

---

# Contenido del curso

La sentencia **`match`** permite comparar un valor contra múltiples posibilidades y ejecutar el bloque correspondiente cuando encuentra una coincidencia.

Fue incorporada en **Python 3.10** como una nueva estructura de control de flujo.

Su sintaxis recuerda al `switch` de otros lenguajes, pero Python implementa un sistema mucho más potente denominado **Structural Pattern Matching** (*coincidencia estructural de patrones*).

En esta clase veremos su uso básico para comparar valores simples.

---

# Sintaxis básica

```python
match expresion:
    case valor1:
        # código
    case valor2:
        # código
    case _:
        # caso por defecto
```

Python evalúa la expresión una única vez y la compara con cada `case` en orden.

Cuando encuentra una coincidencia, ejecuta el bloque correspondiente.

---

# Primer ejemplo

```python
dia = 1

match dia:
    case 1:
        print("Hoy es lunes")
    case 2:
        print("Hoy es martes")
    case 3:
        print("Hoy es miércoles")
    case _:
        print("No coincide")
```

Resultado:

```text
Hoy es lunes
```

---

# Cambiando el valor

```python
dia = 2
```

Resultado:

```text
Hoy es martes
```

---

```python
dia = 3
```

Resultado:

```text
Hoy es miércoles
```

---

# Caso no contemplado

```python
dia = 9
```

Resultado:

```text
No coincide
```

El bloque:

```python
case _:
```

captura cualquier valor que no haya coincidido con los casos anteriores.

---

# Expansión técnica

Internamente Python sigue el siguiente flujo.

```text
match

↓

Evaluar expresión

↓

Comparar con case 1

↓

¿Coincide?
```

Si la respuesta es **No**:

```text
↓

Comparar con case 2

↓

¿Coincide?
```

El proceso continúa hasta encontrar una coincidencia o llegar al caso `_`.

---

# ¿Qué representa `case _`?

El carácter `_` funciona como un **comodín (wildcard)**.

Significa:

> "Acepta cualquier otro valor."

Es equivalente al `else` de una estructura `if`.

```python
case _:
    print("Valor no reconocido")
```

---

# `match` frente a `if`

La misma lógica escrita con `if`.

```python
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
else:
    print("No coincide")
```

Con `match`.

```python
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case _:
        print("No coincide")
```

---

# ¿Cuándo utilizar `match`?

`match` resulta especialmente útil cuando se compara **una misma variable** contra múltiples valores posibles.

Ejemplos:

- días de la semana;
- estados de un pedido;
- códigos de respuesta;
- comandos de un programa;
- opciones de un menú.

---

# Comparando cadenas de texto

`match` también puede utilizarse con strings.

```python
dia = "lunes"

match dia:
    case "lunes":
        print("Hoy es lunes")
    case "martes":
        print("Hoy es martes")
    case "miércoles":
        print("Hoy es miércoles")
    case _:
        print("No coincide")
```

Resultado:

```text
Hoy es lunes
```

---

# Comparación sensible a mayúsculas

Las comparaciones siguen siendo **case sensitive**.

```python
dia = "Lunes"
```

No coincide con:

```python
case "lunes":
```

Porque:

```text
"Lunes"

≠

"lunes"
```

Cuando sea necesario ignorar diferencias de capitalización puede utilizarse:

```python
match dia.lower():
```

---

# Expansión técnica

A diferencia de un `if`, `match` evalúa la expresión **una sola vez**.

```text
Expresión

↓

Evaluación única

↓

Comparaciones sucesivas
```

En un `if` tradicional la variable suele compararse repetidamente.

```python
if dia == 1:
elif dia == 2:
elif dia == 3:
```

Cada condición vuelve a evaluar la misma variable.

---

# Importante: `match` no reemplaza siempre a `if`

`match` es excelente para comparar un único valor.

Sin embargo, cuando las condiciones incluyen operadores lógicos o comparaciones distintas, `if` sigue siendo la mejor opción.

Ejemplo.

```python
if edad >= 18 and tiene_documento:
```

No sería una buena candidata para convertirse en un `match`.

---

# AI Engineering

Aunque `match` todavía no aparece con tanta frecuencia como `if`, puede mejorar la organización de ciertos sistemas de IA.

| Caso | Uso |
|------|-----|
| Modelos de IA | Seleccionar el proveedor (`OpenAI`, `Claude`, `Gemini`) |
| APIs | Procesar distintos códigos de respuesta |
| Agentes | Elegir herramientas según el comando recibido |
| Chatbots | Identificar la intención del usuario |
| Automatizaciones | Ejecutar acciones según el estado del flujo |

### Caso práctico

Seleccionar un proveedor de modelos.

```python
proveedor = "openai"

match proveedor:
    case "openai":
        print("Usando GPT")
    case "anthropic":
        print("Usando Claude")
    case "google":
        print("Usando Gemini")
    case _:
        print("Proveedor no soportado")
```

Este patrón resulta más legible que múltiples comparaciones sobre la misma variable.

---

# Problemas reales en producción

## Problema 1

Utilizar `match` en versiones anteriores a Python 3.10.

```python
match valor:
```

Resultado.

```text
SyntaxError
```

Debe utilizarse Python **3.10 o superior**.

---

## Problema 2

Olvidar el caso por defecto.

```python
match estado:
    case "OK":
        print("Correcto")
```

Si el valor no coincide, simplemente no se ejecutará ningún bloque.

En muchos casos conviene incluir:

```python
case _:
```

para manejar entradas inesperadas.

---

## Problema 3

Intentar utilizar `match` para condiciones complejas.

Incorrecto.

```python
match edad:
    case edad > 18:
```

`match` no fue diseñado para sustituir todas las expresiones booleanas.

Cuando la decisión depende de comparaciones complejas, operadores lógicos o rangos de valores, `if` continúa siendo la herramienta adecuada.

---

## Problema 4

Olvidar que la comparación de cadenas distingue mayúsculas y minúsculas.

```python
"Lunes"
```

No coincide con:

```python
case "lunes":
```

Debe normalizarse previamente cuando sea necesario.

---

# Buenas prácticas

- Utiliza `match` cuando una única variable pueda tomar varios valores conocidos.
- Incluye siempre un `case _` para manejar valores inesperados.
- Reserva `if` para condiciones complejas con operadores lógicos o comparaciones múltiples.
- Normaliza cadenas (`lower()`) cuando la capitalización no sea relevante.
- Comprueba que el proyecto utilice Python 3.10 o una versión superior antes de incorporar `match`.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`match` es simplemente un `switch`"

### Corrección técnica

No exactamente. Aunque su uso básico se parece a un `switch`, `match` implementa **Structural Pattern Matching**, una característica mucho más potente capaz de comparar estructuras complejas como tuplas, listas, diccionarios y objetos. En esta clase únicamente se utiliza la forma más sencilla basada en valores.

---

## Corrección 2. "`match` reemplaza completamente a `if`"

### Corrección técnica

No. `match` es una herramienta especializada para comparar patrones. Las condiciones basadas en operadores lógicos (`and`, `or`, `not`), comparaciones numéricas o expresiones booleanas siguen resolviéndose de forma más natural mediante `if`.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuándo utilizarías `match` en lugar de una cadena de `if` y `elif`?

### Qué evalúa

Capacidad para seleccionar la estructura de control más adecuada.

### Errores comunes

- Pensar que `match` debe utilizarse siempre que existan varias condiciones.

### Respuesta de alto impacto

> Utilizaría `match` cuando una única expresión pueda tomar varios valores claramente definidos, como estados, comandos o códigos de respuesta. Esto mejora la legibilidad y facilita añadir nuevos casos sin repetir la misma comparación.

---

## Pregunta 2

¿Qué función cumple `case _`?

### Qué evalúa

Comprensión del flujo de ejecución.

### Errores comunes

- Creer que es obligatorio o que representa un valor especial.

### Respuesta de alto impacto

> `case _` actúa como un comodín que captura cualquier valor que no haya coincidido con los casos anteriores. Cumple un papel equivalente al `else` de una estructura condicional y permite manejar entradas inesperadas de forma explícita.

---

## Pregunta 3

¿Por qué `match` requiere Python 3.10 o superior?

### Qué evalúa

Conocimiento de la evolución del lenguaje y compatibilidad de versiones.

### Errores comunes

- Pensar que es una sintaxis disponible desde versiones anteriores.

### Respuesta de alto impacto

> Porque la sentencia `match` fue introducida oficialmente en Python 3.10 mediante PEP 634. Intentar utilizarla en versiones anteriores produce un error de sintaxis, por lo que siempre es importante verificar la versión del intérprete antes de incorporarla a un proyecto.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `match` Statement.
- Python Documentation — Compound Statements.

## PEPs

- **PEP 634** — Structural Pattern Matching: Specification.
- **PEP 635** — Structural Pattern Matching: Motivation and Rationale.
- **PEP 636** — Structural Pattern Matching: Tutorial.
- **PEP 8** — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.