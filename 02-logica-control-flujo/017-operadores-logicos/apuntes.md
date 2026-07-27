# Clase 17. Operadores de Comparación y Operadores Lógicos en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo comparar valores y combinar condiciones mediante operadores de comparación y operadores lógicos, entendiendo cómo Python evalúa expresiones booleanas y cómo estas controlan el flujo de ejecución de un programa.

---

# Contenido del curso

Los **operadores de comparación** permiten comparar dos valores y obtener un resultado booleano (`True` o `False`).

Los **operadores lógicos** permiten combinar varias comparaciones para construir condiciones más complejas.

Estos operadores son la base de:

- estructuras `if`;
- bucles `while`;
- validaciones;
- autenticación;
- reglas de negocio;
- filtros;
- permisos;
- Inteligencia Artificial.

---

# Variables de ejemplo

Durante toda la clase utilizaremos:

```python
x = 5
y = 3
z = 5
```

---

# Operador de igualdad (`==`)

Compara si dos valores son iguales.

```python
print(x == y)
```

Resultado:

```python
False
```

Porque:

```text
5

≠

3
```

---

## Igualdad verdadera

```python
print(x == z)
```

Resultado:

```python
True
```

---

# Diferencia entre `=` y `==`

Es uno de los errores más comunes cuando se comienza a programar.

| Operador | Función |
|-----------|----------|
| `=` | Asigna un valor |
| `==` | Compara dos valores |

Ejemplo.

```python
x = 10
```

Significa:

```text
Asignar 10 a x
```

Mientras que:

```python
x == 10
```

Significa:

```text
¿x es igual a 10?
```

El resultado será:

```python
True
```

o

```python
False
```

---

# Operador de desigualdad (`!=`)

Comprueba si dos valores son distintos.

```python
print(x != y)
```

Resultado:

```python
True
```

Porque:

```text
5

≠

3
```

---

## Comparación falsa

```python
print(x != z)
```

Resultado:

```python
False
```

Porque ambos contienen el mismo valor.

---

# Operador mayor que (`>`)

Comprueba si el valor izquierdo es mayor.

```python
print(x > y)
```

Resultado:

```python
True
```

---

# Operador menor que (`<`)

```python
print(x < y)
```

Resultado:

```python
False
```

---

# Operador mayor o igual (`>=`)

Acepta dos escenarios:

- el valor es mayor;
- el valor es igual.

```python
print(x >= y)
```

Resultado:

```python
True
```

---

```python
print(x >= z)
```

Resultado:

```python
True
```

Aunque ambos sean iguales, la condición sigue siendo verdadera.

---

# Operador menor o igual (`<=`)

```python
print(x <= z)
```

Resultado:

```python
True
```

---

```python
print(x <= y)
```

Resultado:

```python
False
```

---

# Resumen de operadores de comparación

| Operador | Significado |
|-----------|-------------|
| `==` | Igual que |
| `!=` | Distinto de |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

Todos devuelven un objeto de tipo:

```python
bool
```

---

# Expansión técnica

Cuando Python encuentra una comparación ocurre el siguiente proceso:

```text
Operando izquierdo

↓

Operador de comparación

↓

Operando derecho

↓

Evaluación

↓

True o False
```

Ese resultado puede almacenarse en una variable o utilizarse directamente en una condición.

```python
es_mayor = x > y
```

---

# Operadores lógicos

Los operadores lógicos permiten combinar varias condiciones.

Python incorpora tres operadores principales:

- `and`
- `or`
- `not`

---

# Operador `and`

Devuelve `True` únicamente cuando **todas las condiciones** son verdaderas.

```python
print(x > y and y > z)
```

Evaluación.

```text
5 > 3

↓

True
```

```text
3 > 5

↓

False
```

Resultado final.

```python
False
```

Porque una de las condiciones no se cumple.

---

# Tabla de verdad de `and`

| A | B | Resultado |
|---|---|------------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# Producción

Permitir acceso únicamente cuando se cumplan dos requisitos.

```python
usuario_activo = True

es_admin = True

print(usuario_activo and es_admin)
```

Solo un administrador activo obtendrá acceso.

---

# Operador `or`

Devuelve `True` cuando **al menos una condición** es verdadera.

```python
print(x > y or y > z)
```

Resultado:

```python
True
```

Porque la primera condición ya es verdadera.

---

# Tabla de verdad de `or`

| A | B | Resultado |
|---|---|------------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# Producción

Permitir acceso mediante dos métodos distintos.

```python
es_admin = False

es_supervisor = True

print(es_admin or es_supervisor)
```

Resultado:

```python
True
```

Basta con que uno de los permisos sea válido.

---

# Operador `not`

Invierte un valor booleano.

```python
print(not True)
```

Resultado:

```python
False
```

---

```python
print(not False)
```

Resultado:

```python
True
```

---

# Negando condiciones

También puede utilizarse sobre expresiones completas.

```python
print(not (x > y))
```

Evaluación.

```text
5 > 3

↓

True

↓

not

↓

False
```

---

# Expansión técnica

Internamente Python evalúa primero la expresión.

```text
Comparación

↓

Resultado booleano

↓

Aplicar not

↓

Invertir resultado
```

---

# Precedencia de operadores lógicos

Cuando una expresión combina varios operadores, Python sigue un orden de evaluación.

1. Paréntesis `()`
2. Comparaciones (`==`, `>`, `<`, etc.)
3. `not`
4. `and`
5. `or`

---

# Uso de paréntesis

Aunque Python conozca la precedencia, utilizar paréntesis mejora considerablemente la legibilidad.

Ejemplo.

```python
resultado = (x > y) and (z == x)
```

El código resulta más fácil de leer y mantener.

---

# AI Engineering

Las comparaciones y operadores lógicos aparecen constantemente en aplicaciones de IA.

| Operador | Caso de uso |
|-----------|-------------|
| `==` | Verificar estados de ejecución |
| `!=` | Detectar cambios en respuestas |
| `>` | Comparar puntuaciones de similitud |
| `<` | Filtrar resultados por umbral |
| `>=` | Validar límites mínimos |
| `<=` | Limitar tamaño de documentos |
| `and` | Cumplir múltiples requisitos antes de ejecutar un modelo |
| `or` | Permitir varias condiciones de entrada |
| `not` | Detectar ausencia de información |

### Caso práctico

Antes de enviar un documento a un modelo de lenguaje.

```python
if documento and len(documento) <= 4000:
    print("Documento válido")
```

La solicitud solo continúa si:

- existe contenido;
- no supera el tamaño permitido.

---

# Problemas reales en producción

## Problema 1

Confundir `=` con `==`.

Incorrecto.

```python
if x = 5:
```

Resultado.

```text
SyntaxError
```

Correcto.

```python
if x == 5:
```

---

## Problema 2

Olvidar utilizar paréntesis en condiciones complejas.

```python
a > b and c == d or e
```

Aunque Python puede evaluarlo, la intención resulta poco clara.

Es preferible.

```python
(a > b and c == d) or e
```

---

## Problema 3

Utilizar `and` cuando realmente se necesita `or`.

```python
es_admin and es_editor
```

Obliga a que ambas condiciones sean verdaderas.

En muchos escenarios el requisito correcto es:

```python
es_admin or es_editor
```

---

## Problema 4

Aplicar `not` sobre una condición equivocada.

Incorrecto.

```python
not x > y
```

Aunque Python lo interpreta como `not (x > y)`, escribir los paréntesis mejora la claridad.

```python
not (x > y)
```

---

# Buenas prácticas

- Utiliza `==` únicamente para comparar valores.
- Nunca confundas `=` con `==`.
- Escribe condiciones utilizando paréntesis cuando existan varias comparaciones.
- Usa `and` cuando todas las condiciones sean obligatorias.
- Usa `or` cuando cualquiera de las condiciones sea suficiente.
- Emplea `not` únicamente cuando mejore la claridad del código.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`and` siempre evalúa ambas condiciones"

### Corrección técnica

Python utiliza **evaluación de cortocircuito (*short-circuit evaluation*)**.

Ejemplo.

```python
False and funcion_costosa()
```

La función **nunca se ejecuta**, porque el resultado ya está determinado por el primer operando.

Del mismo modo:

```python
True or funcion_costosa()
```

La función tampoco se ejecuta.

Este comportamiento mejora el rendimiento y evita errores innecesarios.

---

## Corrección 2. "`not` solo sirve con `True` y `False`"

### Corrección técnica

`not` puede aplicarse sobre cualquier expresión que Python pueda evaluar como verdadera o falsa.

Ejemplo.

```python
lista = []

print(not lista)
```

Resultado.

```python
True
```

Porque una lista vacía es un valor *falsy*.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre `=` y `==`?

### Qué evalúa

Comprensión de asignación frente a comparación.

### Errores comunes

- Confundir ambos operadores.

### Respuesta de alto impacto

> `=` asigna un valor a una variable, mientras que `==` compara dos valores y devuelve un booleano. Confundir ambos operadores suele provocar errores de sintaxis o lógica en el programa.

---

## Pregunta 2

¿Qué significa que los operadores `and` y `or` utilizan evaluación de cortocircuito?

### Qué evalúa

Conocimiento del funcionamiento interno del lenguaje.

### Errores comunes

- Creer que Python siempre evalúa todas las condiciones.

### Respuesta de alto impacto

> Python deja de evaluar una expresión cuando el resultado ya puede determinarse. Por ejemplo, en `False and funcion()`, la función nunca se ejecuta porque el resultado será `False` independientemente del segundo operando. Esto mejora el rendimiento y evita ejecuciones innecesarias.

---

## Pregunta 3

¿Cuándo utilizarías `and` y cuándo `or`?

### Qué evalúa

Capacidad para modelar reglas de negocio.

### Errores comunes

- Intercambiar ambos operadores.

### Respuesta de alto impacto

> Utilizaría `and` cuando todas las condiciones deban cumplirse simultáneamente, por ejemplo para validar permisos múltiples. Utilizaría `or` cuando cualquiera de las condiciones sea suficiente para continuar, como permitir acceso mediante distintos roles.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Comparisons.
- Python Documentation — Boolean Operations.
- Python Documentation — Truth Value Testing.

## PEPs

- **PEP 8** — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.