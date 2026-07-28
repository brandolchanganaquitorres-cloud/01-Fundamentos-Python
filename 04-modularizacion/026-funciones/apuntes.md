# Clase 26. Funciones en Python (`def`, parámetros, argumentos, `return` y `pass`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo definir y utilizar funciones en Python, aprender a reutilizar código mediante `def`, trabajar con parámetros y argumentos, utilizar valores por defecto, devolver resultados con `return` y construir código modular siguiendo buenas prácticas de Ingeniería de Software.

---

# Contenido del curso

Una **función** es un bloque de código reutilizable que realiza una tarea específica.

A diferencia del código secuencial, una función **no se ejecuta automáticamente** cuando Python la encuentra. Primero se define y únicamente se ejecuta cuando es invocada.

Las funciones son uno de los pilares de cualquier programa porque permiten:

- reutilizar código;
- reducir duplicación;
- organizar programas grandes;
- facilitar pruebas y mantenimiento;
- dividir problemas complejos en tareas pequeñas.

---

# Definir una función

Las funciones se crean utilizando la palabra reservada `def`.

```python
def mi_funcion():
    print("Hola mundo desde una función")
```

---

# ¿Qué ocurre al ejecutar este código?

Nada.

Python únicamente registra la función en memoria.

El cuerpo todavía no se ejecuta.

```text
Leer archivo

↓

Encontrar def

↓

Guardar función

↓

Continuar leyendo
```

---

# Llamar una función

Para ejecutarla basta con escribir su nombre seguido de paréntesis.

```python
mi_funcion()
```

Resultado.

```text
Hola mundo desde una función
```

---

# Funcionamiento interno

```text
Programa

↓

Llamada a la función

↓

Buscar definición

↓

Ejecutar instrucciones

↓

Regresar al programa
```

Una función puede llamarse tantas veces como sea necesario.

```python
mi_funcion()
mi_funcion()
mi_funcion()
```

Resultado.

```text
Hola mundo desde una función
Hola mundo desde una función
Hola mundo desde una función
```

---

# ¿Por qué utilizar funciones?

Sin funciones.

```python
print("Hola Pedro")
print("Hola María")
print("Hola Juan")
```

Con funciones.

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Pedro")
saludar("María")
saludar("Juan")
```

La lógica se escribe una sola vez y se reutiliza.

---

# Parámetros

Los parámetros son variables definidas en la declaración de la función.

```python
def saludar(nombre):
    print("Hola", nombre)
```

En este caso.

```python
nombre
```

es un parámetro.

---

# Argumentos

Los argumentos son los valores enviados cuando se llama la función.

```python
saludar("Pedro")
```

Aquí.

```python
"Pedro"
```

es el argumento.

---

# Expansión técnica

En la documentación oficial de Python se distingue entre:

- **Parámetro (*parameter*)**: variable declarada en la definición de la función.
- **Argumento (*argument*)**: valor real que se pasa durante la llamada.

Aunque en muchos cursos se usan como sinónimos, esta es la terminología técnica correcta.

---

# Paso de información

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Pedro")
```

Funcionamiento.

```text
Argumento

↓

Parámetro

↓

Variable local

↓

Ejecutar función
```

---

# Múltiples parámetros

```python
def saludar(nombre, apellido):
    print("Hola", nombre, apellido)
```

Llamada.

```python
saludar("Pedro", "Sánchez")
```

Resultado.

```text
Hola Pedro Sánchez
```

---

# El orden importa

```python
saludar("Pedro", "Sánchez")
```

No produce el mismo resultado que.

```python
saludar("Sánchez", "Pedro")
```

Los argumentos se asignan según su posición.

---

# ¿Qué ocurre si falta un argumento?

```python
saludar("Pedro")
```

Resultado.

```text
TypeError
```

Python informa que falta un argumento obligatorio.

---

# Parámetros con valores por defecto

Los parámetros pueden tener un valor predeterminado.

```python
def saludar(
    nombre,
    apellido="",
    nacionalidad="Colombia"
):
    print(
        "Hola",
        nombre,
        apellido,
        "de",
        nacionalidad
    )
```

---

# Ejemplos

```python
saludar(
    "Pedro",
    "Sánchez",
    "España"
)
```

Resultado.

```text
Hola Pedro Sánchez de España
```

---

```python
saludar("María")
```

Resultado.

```text
Hola María de Colombia
```

---

```python
saludar("Ana")
```

Resultado.

```text
Hola Ana de Colombia
```

Cuando un argumento no se proporciona, Python utiliza el valor definido por defecto.

---

# Funcionamiento interno

```text
¿Se recibió argumento?

↓

Sí

↓

Usar argumento
```

```text
↓

No

↓

Usar valor por defecto
```

---

# La sentencia `return`

Las funciones pueden devolver información.

```python
def sumar(a, b):
    return a + b
```

---

# Utilizar el valor devuelto

```python
resultado = sumar(2, 3)

print(resultado)
```

Resultado.

```text
5
```

---

# ¿Qué ocurre si no guardamos el resultado?

```python
sumar(2, 3)
```

La suma se realiza, pero el valor devuelto se descarta.

No podrá utilizarse posteriormente.

---

# Funcionamiento interno de `return`

```text
Llamar función

↓

Ejecutar instrucciones

↓

return

↓

Devolver resultado

↓

Finalizar función

↓

Continuar programa
```

---

# `return` finaliza inmediatamente la función

```python
def ejemplo():
    print("Inicio")
    return
    print("Fin")
```

Resultado.

```text
Inicio
```

Todo el código situado después de `return` dentro de la misma función es inalcanzable.

---

# Funciones sin `return`

```python
def saludar():
    print("Hola")
```

Aunque no exista un `return` explícito, Python devuelve automáticamente:

```python
None
```

Ejemplo.

```python
resultado = saludar()

print(resultado)
```

Resultado.

```text
Hola
None
```

---

# La sentencia `pass`

Durante el desarrollo es frecuente definir funciones cuya implementación aún no existe.

```python
def calcular():
    pass
```

`pass` permite mantener una sintaxis válida sin ejecutar ninguna acción.

---

# ¿Por qué es necesario?

Esto produce un error.

```python
def calcular():
```

Resultado.

```text
IndentationError
```

Python espera al menos una instrucción dentro del bloque.

---

# ¿Cuándo utilizar funciones?

Las funciones son recomendables cuando:

- una tarea se repite varias veces;
- un bloque de código tiene una responsabilidad clara;
- se desea reutilizar lógica;
- un algoritmo puede dividirse en partes independientes.

---

# AI Engineering

Las funciones son la base sobre la que se construyen prácticamente todas las aplicaciones de IA.

| Caso | Uso |
|------|-----|
| OpenAI SDK | Enviar solicitudes al modelo |
| RAG | Recuperar documentos |
| Embeddings | Generar vectores |
| LangChain | Herramientas (*tools*) |
| APIs | Validar datos de entrada |
| Automatización | Procesar archivos |

### Caso práctico

Encapsular la llamada a un modelo de lenguaje.

```python
def generar_respuesta(prompt):
    return cliente.responses.create(
        model="gpt-5",
        input=prompt
    )
```

En lugar de repetir la llamada en todo el proyecto, se centraliza en una única función.

---

# Problemas reales en producción

## Problema 1

Funciones demasiado largas.

```python
def procesar():
    ...
```

Con cientos de líneas resulta difícil probar, mantener y reutilizar el código.

Se recomienda que cada función tenga una única responsabilidad.

---

## Problema 2

Olvidar utilizar el valor devuelto.

```python
sumar(5, 8)
```

Si el resultado no se asigna o utiliza, se pierde.

---

## Problema 3

Modificar variables globales desde una función.

```python
contador += 1
```

El uso excesivo de variables globales dificulta el mantenimiento y aumenta el riesgo de errores.

Es preferible recibir los datos mediante parámetros y devolver nuevos valores con `return`.

---

## Problema 4

Usar `print()` en lugar de `return`.

```python
def sumar(a, b):
    print(a + b)
```

Esta función muestra el resultado, pero no permite reutilizarlo en otros cálculos.

En la mayoría de los casos debe utilizarse:

```python
return a + b
```

---

# Buenas prácticas

- Asigna nombres descriptivos a las funciones utilizando `snake_case`.
- Diseña funciones con una única responsabilidad.
- Devuelve resultados mediante `return` en lugar de depender de `print()`.
- Utiliza parámetros con valores por defecto solo cuando realmente sean opcionales.
- Evita depender de variables globales.
- Escribe funciones pequeñas, reutilizables y fáciles de probar.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "Argumento es lo que la función espera y parámetro es lo que se envía"

### Corrección técnica

La terminología presentada en el curso está invertida respecto a la utilizada por la documentación oficial de Python.

La definición correcta es:

- **Parámetro**: variable declarada en la definición de la función.

```python
def saludar(nombre):
```

`nombre` es un parámetro.

- **Argumento**: valor enviado durante la llamada.

```python
saludar("Pedro")
```

`"Pedro"` es el argumento.

En conversaciones informales ambos términos suelen intercambiarse, pero en documentación técnica y entrevistas conviene utilizar la nomenclatura correcta.

---

## Corrección 2. "Si no guardas el resultado de `return`, la función no devuelve nada"

### Corrección técnica

La función **sí devuelve el valor**. Lo que ocurre es que el programa lo descarta porque no se almacena ni se utiliza.

---

## Corrección 3. "`pass` sirve únicamente para evitar errores"

### Corrección técnica

Además de mantener la sintaxis válida, `pass` se utiliza como marcador temporal (*placeholder*) durante el diseño de APIs, clases y funciones que serán implementadas posteriormente.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre `print()` y `return`?

### Qué evalúa

Comprensión del flujo de datos dentro de una función.

### Errores comunes

- Pensar que ambos hacen lo mismo.

### Respuesta de alto impacto

> `print()` únicamente envía información a la salida estándar y no permite reutilizar ese resultado. `return` devuelve un valor al punto donde fue llamada la función, permitiendo almacenarlo, combinarlo con otras operaciones o utilizarlo en cualquier parte del programa.

---

## Pregunta 2

¿Por qué es recomendable dividir un programa en funciones pequeñas?

### Qué evalúa

Conocimientos de diseño de software.

### Errores comunes

- Responder únicamente "porque el código queda más ordenado".

### Respuesta de alto impacto

> Las funciones pequeñas favorecen la reutilización, simplifican las pruebas unitarias, reducen el acoplamiento y facilitan el mantenimiento. Además, cuando cada función tiene una única responsabilidad, es más sencillo localizar errores y modificar el comportamiento sin afectar otras partes del sistema.

---

## Pregunta 3

¿Qué ocurre cuando una función no tiene un `return` explícito?

### Qué evalúa

Comprensión del comportamiento interno de Python.

### Errores comunes

- Responder que la función no devuelve nada.

### Respuesta de alto impacto

> En Python toda función devuelve un valor. Si no existe un `return` explícito, el intérprete retorna automáticamente `None`. Este comportamiento permite que todas las llamadas a funciones produzcan un resultado consistente.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Defining Functions.
- Python Documentation — The `return` Statement.
- Python Documentation — Compound Statements.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 257** — Docstring Conventions.
- **PEP 3102** — Keyword-Only Arguments.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.