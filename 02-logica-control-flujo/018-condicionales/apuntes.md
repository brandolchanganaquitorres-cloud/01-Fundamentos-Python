# Clase 18. Condicionales en Python (`if`, `else`, `pass`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo controlar el flujo de un programa mediante estructuras condicionales (`if`, `else`), combinar condiciones utilizando operadores lógicos, comparar distintos tipos de datos, construir condicionales anidados y utilizar correctamente `pass` como marcador temporal de implementación.

---

# Contenido del curso

Los **condicionales** permiten que un programa tome decisiones dependiendo de si una condición es verdadera (`True`) o falsa (`False`).

Gracias a ellos un programa puede:

- ejecutar diferentes bloques de código;
- validar información;
- controlar permisos;
- responder a acciones del usuario;
- automatizar decisiones.

Todo condicional comienza evaluando una expresión booleana.

---

# La sentencia `if`

La estructura más simple es:

```python
if condicion:
    # código
```

El bloque interno únicamente se ejecuta cuando la condición es verdadera.

---

# Condición verdadera

```python
if 5 > 3:
    print("5 es mayor que 3")
```

Resultado:

```text
5 es mayor que 3
```

---

# Condición falsa

```python
if 2 > 3:
    print("2 es mayor que 3")
```

Resultado:

```text
(no imprime nada)
```

El programa simplemente continúa con la siguiente instrucción.

---

# Expansión técnica

Internamente Python sigue este flujo.

```text
Condición

↓

¿True?

↓

Sí

↓

Ejecutar bloque
```

o

```text
Condición

↓

¿True?

↓

No

↓

Omitir bloque
```

---

# Utilizando variables

Las condiciones normalmente comparan variables.

```python
x = 5
y = 3

if x > y:
    print("x es mayor que y")
```

Resultado:

```text
x es mayor que y
```

---

# Múltiples `if`

Dos estructuras `if` consecutivas son completamente independientes.

```python
if x > y:
    print("Mayor")

if x < y:
    print("Menor")
```

Cada condición se evalúa por separado.

Una puede ejecutarse y la otra no.

---

# Expansión técnica

Muchos principiantes creen que un segundo `if` depende automáticamente del primero.

No es así.

Python interpreta:

```text
Primer if

↓

Evaluar

↓

Continuar

↓

Segundo if

↓

Evaluar
```

Cada uno representa una decisión independiente.

---

# La sentencia `else`

`else` define el camino alternativo cuando la condición del `if` resulta falsa.

```python
if x > y:
    print("Mayor")
else:
    print("No es mayor")
```

Si el `if` no se ejecuta, Python entra automáticamente al bloque `else`.

---

# Ejemplo

```python
x = 5
y = 5

if x > y:
    print("Mayor")
else:
    print("No es mayor")
```

Resultado:

```text
No es mayor
```

---

# `if` anidados

Es posible colocar un `if` dentro de otro.

```python
if x > y:
    print("Mayor")
else:
    if x == y:
        print("Son iguales")
    else:
        print("Menor")
```

Resultado:

```text
Son iguales
```

---

# Funcionamiento interno

```text
Primer if

↓

¿True?

↓

No

↓

Entrar al else

↓

Segundo if

↓

Evaluar nueva condición
```

Cada nuevo nivel representa una decisión adicional.

---

# Comparar cadenas de texto

Los operadores de comparación también funcionan sobre strings.

```python
a = "Python"
b = "JavaScript"

if a == b:
    print("Son iguales")
else:
    print("Son diferentes")
```

Resultado:

```text
Son diferentes
```

---

# Comparación múltiple

```python
a = "Python"
b = "JavaScript"
c = "Python"

if a == c:
    if a != b:
        print("a es igual a c, pero diferente de b")
```

Resultado:

```text
a es igual a c, pero diferente de b
```

---

# Expansión técnica

Las comparaciones entre cadenas son **sensibles a mayúsculas y minúsculas**.

```python
"Python" == "python"
```

Resultado:

```python
False
```

Cuando sea necesario ignorar diferencias de capitalización, puede normalizarse el texto.

```python
a.lower() == b.lower()
```

---

# Operador `and`

Permite exigir que varias condiciones sean verdaderas.

```python
x = 5
y = 3
z = 1

if x > y and x > z:
    print("x es el mayor")
```

Resultado:

```text
x es el mayor
```

---

# Funcionamiento

```text
Condición 1

↓

True
```

```text
Condición 2

↓

True
```

```text
True AND True

↓

True
```

---

# Operador `or`

Permite que una sola condición sea suficiente.

```python
x = 5
y = 3
z = 10

if x > y or x > z:
    print("Al menos una condición es verdadera")
```

Resultado:

```text
Al menos una condición es verdadera
```

---

# Expansión técnica

Python utiliza **evaluación de cortocircuito (Short-Circuit Evaluation)**.

Ejemplo.

```python
if usuario is not None and usuario.activo:
```

Si:

```python
usuario is None
```

Python **no evalúa**:

```python
usuario.activo
```

Esto evita errores como:

```text
AttributeError
```

y mejora el rendimiento del programa.

---

# La importancia de la indentación

Python utiliza la indentación para definir bloques de código.

Correcto.

```python
if x > y:
    print("Mayor")
```

Incorrecto.

```python
if x > y:
print("Mayor")
```

Resultado:

```text
IndentationError
```

La indentación forma parte de la sintaxis del lenguaje.

---

# ¿Cuántos espacios utilizar?

La recomendación oficial (PEP 8) es utilizar **4 espacios por nivel de indentación**.

La mayoría de los editores modernos realizan esta indentación automáticamente.

---

# La sentencia `pass`

En ocasiones todavía no conocemos la implementación de un bloque.

Python no permite dejar un bloque vacío.

Incorrecto.

```python
if x == y:
```

Resultado.

```text
IndentationError
```

---

# Utilizando `pass`

```python
if x == y:
    pass
```

El programa continúa ejecutándose normalmente.

---

# ¿Para qué sirve `pass`?

`pass` actúa como un **marcador temporal (placeholder)**.

Permite construir primero la estructura del programa y completar posteriormente la lógica.

---

# Producción

Durante el desarrollo suele escribirse primero la arquitectura.

```python
def procesar_pago():

    pass
```

Posteriormente se implementa la funcionalidad.

Este enfoque es habitual cuando varios desarrolladores trabajan simultáneamente sobre un mismo proyecto.

---

# AI Engineering

Los condicionales controlan prácticamente todos los flujos de una aplicación basada en IA.

| Estructura | Caso de uso |
|------------|-------------|
| `if` | Validar que exista un prompt antes de enviarlo al modelo |
| `else` | Ejecutar una respuesta alternativa cuando falle una validación |
| `and` | Exigir múltiples requisitos antes de llamar a un LLM |
| `or` | Permitir varias formas de autenticación o entrada |
| `pass` | Definir la estructura inicial de un agente antes de implementarlo |

### Caso práctico

Validar un documento antes de enviarlo a un modelo.

```python
documento = "Manual.pdf"

if documento and documento.endswith(".pdf"):
    print("Documento válido")
else:
    print("Formato incorrecto")
```

Este patrón aparece con frecuencia en pipelines de procesamiento documental y sistemas RAG.

---

# Problemas reales en producción

## Problema 1

Olvidar la indentación.

```python
if usuario:
print(usuario)
```

Resultado.

```text
IndentationError
```

---

## Problema 2

Anidar demasiados `if`.

```python
if A:
    if B:
        if C:
            if D:
```

El código se vuelve difícil de mantener.

En estos casos conviene simplificar la lógica o dividir el problema en funciones.

---

## Problema 3

Comparar cadenas ignorando diferencias de mayúsculas.

```python
usuario == "admin"
```

Si el usuario escribe:

```text
Admin
```

La comparación fallará.

Debe normalizarse previamente cuando el dominio lo permita.

---

## Problema 4

Olvidar utilizar `pass` durante el desarrollo.

```python
if condicion:
```

Produce:

```text
IndentationError
```

---

# Buenas prácticas

- Escribe condiciones simples y fáciles de entender.
- Utiliza nombres de variables descriptivos para que la condición sea legible.
- Evita anidar muchos niveles de `if`; considera dividir la lógica en funciones.
- Respeta siempre la indentación de cuatro espacios.
- Utiliza `pass` únicamente como solución temporal mientras desarrollas la implementación.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`else` pertenece siempre al último `if` escrito"

### Corrección técnica

`else` se asocia con el `if` que comparte **el mismo nivel de indentación**, no necesariamente con el último que aparece visualmente. Una indentación incorrecta puede cambiar completamente el flujo del programa.

---

## Corrección 2. "`pass` hace que el programa ignore el bloque"

### Corrección técnica

`pass` no omite la evaluación de la condición. La condición se evalúa normalmente; simplemente, cuando se entra al bloque, no se ejecuta ninguna acción.

---

## Corrección 3. "Los `if` anidados son la mejor forma de expresar lógica compleja"

### Corrección técnica

Aunque son válidos, un exceso de anidamiento reduce la legibilidad. En proyectos profesionales suele preferirse simplificar las condiciones, utilizar cláusulas de salida temprana (*guard clauses*) o dividir la lógica en funciones pequeñas y especializadas.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué Python utiliza la indentación para definir bloques de código?

### Qué evalúa

Comprensión de la sintaxis y filosofía del lenguaje.

### Errores comunes

- Pensar que la indentación es únicamente una recomendación estética.

### Respuesta de alto impacto

> En Python la indentación forma parte de la sintaxis del lenguaje. Define explícitamente los bloques de ejecución, elimina la necesidad de llaves y obliga a mantener un estilo de código consistente y legible entre todos los desarrolladores.

---

## Pregunta 2

¿Cuándo utilizarías un `if` anidado y cuándo preferirías otra solución?

### Qué evalúa

Capacidad para escribir código mantenible.

### Errores comunes

- Anidar múltiples niveles sin necesidad.

### Respuesta de alto impacto

> Utilizaría un `if` anidado únicamente cuando exista una dependencia lógica entre condiciones. Si el nivel de anidamiento comienza a crecer, prefiero dividir la lógica en funciones o utilizar cláusulas de salida temprana para mejorar la legibilidad y facilitar el mantenimiento.

---

## Pregunta 3

¿Para qué sirve realmente la sentencia `pass`?

### Qué evalúa

Conocimiento de la sintaxis del lenguaje y del flujo de desarrollo.

### Errores comunes

- Creer que `pass` detiene la ejecución o ignora la condición.

### Respuesta de alto impacto

> `pass` es una instrucción nula que permite definir un bloque sintácticamente válido sin implementar todavía su lógica. Se utiliza como marcador temporal durante el desarrollo, especialmente cuando primero se diseña la estructura del programa y luego se completa la implementación.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `if` Statement.
- Python Documentation — Compound Statements.
- Python Documentation — The `pass` Statement.

## PEPs

- **PEP 8** — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.