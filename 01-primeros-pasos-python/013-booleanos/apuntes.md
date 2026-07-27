# Clase 13. Booleanos, Casting e Identificación de Tipos en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender qué son los valores booleanos, cómo se generan mediante comparaciones y conversiones de tipos, interpretar el concepto de *truthy* y *falsy*, y utilizar `isinstance()` para validar tipos de datos antes de procesarlos en aplicaciones reales.

---

# Contenido del curso

Los **booleanos** (`bool`) representan el tipo de dato lógico de Python y únicamente pueden almacenar dos valores:

- `True`
- `False`

Toda decisión que toma un programa termina reduciéndose a una evaluación booleana.

Los booleanos aparecen constantemente en:

- estructuras `if`;
- bucles `while`;
- validaciones;
- autenticación;
- permisos;
- comparaciones;
- manejo de errores.

Dominar este tipo de dato es fundamental para controlar el flujo de ejecución de un programa.

---

# Declaración de booleanos

Los booleanos se escriben siempre con la primera letra en mayúscula.

```python
b = True
f = False

print(b)
print(f)
```

Resultado:

```python
True
False
```

---

# Error común

Escribir:

```python
true
```

o

```python
false
```

produce:

```text
NameError
```

Porque Python interpreta esas palabras como nombres de variables y no como valores booleanos.

---

# Verificar el tipo con `type()`

```python
valor = True

print(type(valor))
```

Resultado:

```python
<class 'bool'>
```

---

# Expansión técnica

En Python, `bool` es una clase incorporada del lenguaje.

Internamente:

```text
Variable

↓

Objeto

↓

Clase bool

↓

True o False
```

Esto significa que los booleanos también son objetos, igual que los enteros, cadenas o listas.

---

# Booleanos mediante comparaciones

La forma más habitual de obtener un booleano es realizar una comparación.

```python
print(5 > 3)
```

Resultado:

```python
True
```

---

```python
print(3 > 5)
```

Resultado:

```python
False
```

---

# Comparaciones frecuentes

```python
5 == 5
```

Resultado:

```python
True
```

```python
5 != 8
```

Resultado:

```python
True
```

```python
10 < 2
```

Resultado:

```python
False
```

Todas las expresiones anteriores producen un valor booleano.

---

# Expansión técnica

Cuando Python evalúa una comparación ocurre el siguiente proceso:

```text
Operando izquierdo

↓

Operador de comparación

↓

Operando derecho

↓

Evaluación lógica

↓

True o False
```

El resultado puede utilizarse inmediatamente para controlar el flujo del programa.

---

# Producción

Validar si un usuario tiene acceso.

```python
edad = 20

print(edad >= 18)
```

Resultado:

```python
True
```

Posteriormente ese resultado puede emplearse en una estructura `if`.

---

# Casting con `bool()`

La función `bool()` convierte otros tipos de datos en un valor booleano.

```python
print(bool("Hola mundo"))
```

Resultado:

```python
True
```

---

# Valores que producen `True`

En general, los objetos que contienen información se consideran verdaderos.

Ejemplos:

```python
bool("Hola")
```

```python
bool(123)
```

```python
bool(["manzana", "pera"])
```

Todos producen:

```python
True
```

---

# Valores que producen `False`

Los objetos vacíos o equivalentes a ausencia de valor se consideran falsos.

```python
bool("")
```

Resultado:

```python
False
```

---

```python
bool(0)
```

Resultado:

```python
False
```

---

```python
bool([])
```

Resultado:

```python
False
```

---

```python
bool(None)
```

Resultado:

```python
False
```

---

# Expansión técnica

Este comportamiento recibe el nombre de **truthy** y **falsy**.

No significa que el objeto sea literalmente `True` o `False`.

Significa que Python sabe interpretarlo como verdadero o falso cuando necesita evaluar una condición.

```text
Objeto

↓

Evaluación lógica

↓

True o False
```

Este mecanismo permite escribir código más limpio y expresivo.

---

# Ejemplo

En lugar de escribir:

```python
if len(lista) > 0:
    print("Hay elementos")
```

Puede escribirse simplemente:

```python
if lista:
    print("Hay elementos")
```

Si la lista está vacía, Python la interpreta automáticamente como `False`.

---

# Producción

Validar una respuesta recibida desde una API.

```python
respuesta = []

if respuesta:
    print("Procesar datos")
```

Si la API devuelve una lista vacía, el bloque no se ejecutará.

Este patrón aparece frecuentemente al consumir servicios REST y GraphQL.

---

# El valor `None`

`None` representa la ausencia de valor.

```python
usuario = None

print(bool(usuario))
```

Resultado:

```python
False
```

---

# Expansión técnica

`None` no significa:

- cero;
- cadena vacía;
- lista vacía.

Es un objeto especial utilizado para indicar que una variable no tiene ningún valor asignado.

Se emplea constantemente en funciones, APIs y bases de datos.

---

# Función `isinstance()`

Permite comprobar si un objeto pertenece a un tipo determinado.

```python
numero = 5

print(isinstance(numero, int))
```

Resultado:

```python
True
```

---

```python
numero = 5.5

print(isinstance(numero, int))
```

Resultado:

```python
False
```

---

# ¿Qué devuelve `isinstance()`?

Siempre devuelve un booleano.

```text
True
```

o

```text
False
```

---

# Expansión técnica

Internamente Python compara el tipo real del objeto con el tipo solicitado.

```text
Objeto

↓

Tipo real

↓

Comparación

↓

True o False
```

Es una forma segura de validar datos antes de utilizarlos.

---

# ¿Por qué usar `isinstance()` y no `type()`?

Aunque ambas funciones permiten trabajar con tipos de datos, tienen propósitos distintos.

| Función | Propósito |
|----------|-----------|
| `type()` | Obtener el tipo exacto del objeto |
| `isinstance()` | Verificar si un objeto pertenece a un tipo determinado |

En aplicaciones reales suele preferirse `isinstance()` para realizar validaciones antes de procesar datos.

---

# AI Engineering

La validación de tipos es una práctica habitual en sistemas de IA.

| Función | Caso de uso |
|----------|-------------|
| `bool()` | Validar si un prompt, documento o respuesta contiene información |
| `isinstance()` | Verificar que los datos recibidos desde una API tengan el tipo esperado |
| Comparaciones | Evaluar reglas de negocio antes de ejecutar un modelo |
| `None` | Detectar respuestas inexistentes o errores en consultas |

### Caso práctico

Antes de enviar información a un modelo de lenguaje:

```python
if documento and isinstance(documento, str):
    print("Documento válido")
```

Con ello se verifica que:

- exista contenido;
- sea una cadena de texto.

---

# Problemas reales en producción

## Problema 1

Comparar una lista vacía mediante su longitud.

```python
if len(lista) > 0:
```

Es correcto, pero menos expresivo que:

```python
if lista:
```

---

## Problema 2

Intentar operar con un valor `None`.

```python
usuario = None

print(usuario.upper())
```

Resultado:

```text
AttributeError
```

Debe comprobarse previamente que exista un valor válido.

---

## Problema 3

No validar el tipo recibido desde una API.

```python
edad = "30"

edad + 10
```

Resultado:

```text
TypeError
```

Una validación previa mediante `isinstance()` o una conversión adecuada evita este tipo de errores.

---

## Problema 4

Escribir `true` o `false` en lugar de `True` y `False`.

Produce:

```text
NameError
```

---

# Buenas prácticas

- Escribe siempre `True` y `False` con mayúscula inicial.
- Utiliza comparaciones para obtener booleanos en lugar de asignarlos manualmente cuando sea posible.
- Aprovecha el comportamiento *truthy* y *falsy* para simplificar condiciones.
- Valida tipos con `isinstance()` antes de procesar datos externos.
- Comprueba si una variable es `None` antes de acceder a sus métodos cuando exista la posibilidad de que no tenga valor.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`bool()` solo convierte valores booleanos"

### Corrección técnica

`bool()` puede convertir prácticamente cualquier objeto de Python. El resultado dependerá de si dicho objeto se considera *truthy* o *falsy*.

---

## Corrección 2. "`None` es equivalente a una cadena vacía"

### Corrección técnica

`None` representa la ausencia de valor y es un objeto distinto de `""`, `0` o `[]`, aunque todos se evalúen como `False` en un contexto booleano.

---

## Corrección 3. "`type()` e `isinstance()` son equivalentes"

### Corrección técnica

No cumplen la misma función. `type()` devuelve el tipo exacto del objeto, mientras que `isinstance()` responde si el objeto pertenece al tipo indicado, siendo la opción recomendada para validaciones.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Qué diferencia existe entre un objeto `False` y un objeto considerado *falsy*?

### Qué evalúa

Comprensión del modelo booleano de Python.

### Errores comunes

- Pensar que `0`, `None` o `[]` son literalmente `False`.

### Respuesta de alto impacto

> `False` es un valor booleano. En cambio, un objeto *falsy* no es necesariamente un booleano, sino un objeto que Python interpreta como falso cuando evalúa una condición, como `0`, `None`, `""` o una lista vacía.

---

## Pregunta 2

¿Cuándo utilizarías `isinstance()`?

### Qué evalúa

Buenas prácticas de validación.

### Errores comunes

- Utilizar `type()` para todas las comprobaciones.

### Respuesta de alto impacto

> Utilizaría `isinstance()` para validar datos provenientes de usuarios, APIs o archivos antes de procesarlos, ya que permite comprobar si un objeto pertenece al tipo esperado y facilita escribir código más robusto.

---

## Pregunta 3

¿Por qué `if lista:` suele ser preferible a `if len(lista) > 0:`?

### Qué evalúa

Conocimiento del comportamiento *truthy* y *falsy*.

### Errores comunes

- Creer que ambas formas son obligatorias.

### Respuesta de alto impacto

> Porque Python evalúa automáticamente las colecciones vacías como `False` y las no vacías como `True`. Utilizar `if lista:` produce un código más limpio, idiomático y alineado con las buenas prácticas del lenguaje.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Boolean Type (`bool`).
- Python Documentation — Built-in Functions (`bool`, `isinstance`, `type`).
- Python Documentation — Truth Value Testing.

## PEPs

- PEP 8 — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.