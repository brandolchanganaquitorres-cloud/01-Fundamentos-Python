# Clase 7. Variables en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Objetivo:** Comprender qué son las variables en Python, cómo funcionan internamente, cómo nombrarlas correctamente siguiendo los estándares profesionales y por qué constituyen uno de los conceptos fundamentales sobre los que se construye todo el ecosistema de Python.

---

# Contenido del curso

## ¿Qué es una variable en Python?

Una variable es un **nombre (identificador)** que hace referencia a un valor almacenado en memoria. Permite guardar información para reutilizarla posteriormente sin necesidad de escribir el mismo dato una y otra vez.

Su declaración es muy sencilla:

```python
x = "Esta es una variable"

print(x)
```

Salida:

```text
Esta es una variable
```

Cuando Python ejecuta `print(x)`, no imprime la letra **x**, sino el valor asociado a esa variable.

---

## El operador de asignación (`=`)

La asignación se realiza mediante el operador `=`.

```python
x = "Hola Mundo"
```

El operador de asignación siempre funciona de **derecha hacia izquierda**.

```text
"Hola Mundo"

        │

        ▼

        x
```

Es decir:

1. Python evalúa el valor situado a la derecha.
2. Después lo asocia con la variable situada a la izquierda.

No significa igualdad matemática.

En programación:

```python
x = 10
```

se interpreta como:

> Asigna el valor **10** a la variable **x**.

---

## ¿Por qué utilizar variables?

Podríamos escribir:

```python
print("Hola Mundo")
```

Pero en programación profesional casi siempre trabajaremos con variables.

```python
mensaje = "Hola Mundo"

print(mensaje)
```

Esto permite:

- reutilizar información;
- modificar valores desde un único lugar;
- escribir código más mantenible;
- mejorar la legibilidad.

En prácticamente todas las bibliotecas modernas (FastAPI, Pandas, LangChain, OpenAI SDK, etc.) los datos se manipulan mediante variables.

---

## Python distingue mayúsculas y minúsculas

Python es un lenguaje **case sensitive**.

Esto significa que:

```python
x = "Primera variable"

X = "Segunda variable"

print(x)
print(X)
```

Salida:

```text
Primera variable
Segunda variable
```

Aunque visualmente parezcan similares, `x` y `X` son variables completamente diferentes.

---

## Reasignación de variables

Las variables pueden cambiar de valor durante la ejecución.

```python
x = "Hola"

print(x)

x = "Adiós"

print(x)
```

Salida:

```text
Hola
Adiós
```

La segunda asignación reemplaza la anterior.

El orden de ejecución es importante.

---

# Reglas para nombrar variables

Python define reglas sintácticas para los identificadores.

## Nombres válidos

```python
mivariable

mi_variable

_mi_variable

miVariable

OtraVariable

MIVARIABLE

miVariable2
```

Todos son identificadores válidos.

---

## Nombres inválidos

No es posible comenzar con un número.

```python
2variable
```

Tampoco utilizar guiones medios.

```python
mi-variable
```

Ni espacios.

```python
mi variable
```

Visual Studio Code suele marcar estos errores inmediatamente.

---

## Uso de números

Los números pueden formar parte del nombre siempre que no aparezcan al inicio.

Correcto:

```python
usuario1

temperatura2026
```

Incorrecto:

```python
1usuario
```

---

# Convenciones de nombres

Cuando los identificadores contienen varias palabras se utilizan convenciones de estilo.

## camelCase

La primera palabra comienza en minúscula.

Las siguientes comienzan con mayúscula.

```python
nombreCompleto

fechaNacimiento
```

---

## PascalCase

Todas las palabras comienzan con mayúscula.

```python
NombreCompleto

FechaNacimiento
```

---

## snake_case

Todas las palabras permanecen en minúscula y se separan mediante guiones bajos.

```python
nombre_completo

fecha_nacimiento
```

Esta es la convención recomendada para variables y funciones en Python.

---

## Variables en MAYÚSCULAS

Por convención se utilizan para representar constantes.

```python
PI = 3.1415926535

MAX_CONNECTIONS = 100
```

Aunque Python permite modificar estos valores, escribirlos completamente en mayúsculas comunica que **no deberían cambiar**.

---

## Variables con guion bajo inicial

```python
_variable
```

Por convención indican que ese atributo o variable es de uso interno.

No significa que sea realmente privada.

Es simplemente una recomendación para otros desarrolladores.

---

# Expansión técnica

## ¿Cómo funcionan realmente las variables en Python?

El curso explica que una variable es una "cajita en memoria".

Esta explicación resulta útil para principiantes, pero técnicamente es una simplificación.

En Python:

> **Las variables no almacenan directamente los datos.**

Las variables almacenan **referencias** a objetos.

Ejemplo:

```python
x = "Hola"
```

Internamente ocurre algo parecido a:

```text
Variable

x

│

▼

┌─────────────┐
│   "Hola"    │
└─────────────┘
```

La variable apunta al objeto.

No contiene el objeto.

Este modelo recibe el nombre de **Object Reference Model**.

Comprenderlo será fundamental cuando estudies listas, diccionarios, clases y funciones.

---

## Objetos en Python

Todo en Python es un objeto.

Por ejemplo:

```python
x = 5
```

El entero `5` es un objeto.

```python
texto = "Python"
```

La cadena también es un objeto.

```python
lista = [1, 2, 3]
```

La lista igualmente es un objeto.

Las variables únicamente mantienen una referencia hacia ellos.

---

## ¿Cómo comprobarlo?

Podemos consultar el identificador del objeto.

```python
x = "Hola"

print(id(x))
```

Salida (ejemplo):

```text
140342519534256
```

Ese número representa la identidad del objeto durante su ciclo de vida.

---

## ¿Qué ocurre cuando reasignamos una variable?

```python
x = "Hola"

x = "Python"
```

Internamente:

```text
Antes

x

↓

"Hola"



Después

x

↓

"Python"
```

La variable deja de apuntar al objeto anterior y pasa a referenciar uno nuevo.

Si ninguna otra variable apunta al objeto `"Hola"`, Python podrá liberarlo posteriormente mediante el recolector de basura (*Garbage Collector*).

---

## ¿Qué tipo de dato tiene una variable?

En realidad, la variable no tiene tipo.

El tipo pertenece al objeto.

Podemos comprobarlo con:

```python
x = 5

print(type(x))
```

Salida:

```text
<class 'int'>
```

Otro ejemplo:

```python
x = "Hola"

print(type(x))
```

Salida:

```text
<class 'str'>
```

Esto convierte a Python en un lenguaje de **tipado dinámico**.

---

## Tipado dinámico

Una misma variable puede referenciar objetos de distintos tipos durante la ejecución.

```python
dato = 10

dato = "Python"

dato = [1, 2, 3]
```

Aunque es posible, en proyectos profesionales no suele recomendarse reutilizar una variable para representar conceptos diferentes.

---

## Convenciones oficiales (PEP 8)

La guía oficial de estilo de Python recomienda:

### Variables

```python
snake_case
```

Ejemplo:

```python
nombre_usuario

edad_cliente
```

---

### Constantes

```python
UPPER_CASE
```

Ejemplo:

```python
MAX_RETRIES

API_KEY
```

---

### Clases

```python
PascalCase
```

Ejemplo:

```python
ClientePremium

FacturaElectronica
```

---

### Evitar camelCase

Aunque Python lo admite, PEP 8 recomienda utilizar `snake_case` para variables y funciones.

---

## Palabras reservadas

No pueden utilizarse como nombres de variables.

Ejemplo:

```python
class = "Python"
```

Resultado:

```text
SyntaxError
```

Otros ejemplos:

```python
if

for

while

return

import

def

True

False

None
```

Puedes consultar todas las palabras reservadas con:

```python
import keyword

print(keyword.kwlist)
```

---

# Problemas reales en producción

## Problema 1

Variables con nombres poco descriptivos.

```python
x = 25

y = 500
```

Semanas después nadie recuerda qué representan.

Es preferible:

```python
edad_cliente = 25

saldo_disponible = 500
```

---

## Problema 2

Reutilizar una variable para conceptos distintos.

```python
dato = "Brandol"

dato = 1500

dato = []
```

Complica el mantenimiento y el debugging.

---

## Problema 3

Mezclar convenciones.

```python
NombreCliente

edad_cliente

saldoCliente

TOTAL
```

El código pierde consistencia.

---

## Problema 4

Variables excesivamente largas.

```python
numero_total_de_clientes_activos_registrados_en_el_sistema
```

Aunque es válido, dificulta la lectura.

Debe buscarse un equilibrio entre claridad y brevedad.

---

# Relación con AI Engineering

Las variables son uno de los pilares de cualquier aplicación de IA.

Ejemplos habituales:

```python
prompt = "Resume el siguiente texto..."

temperature = 0.2

max_tokens = 1000

embedding_model = "text-embedding-3-small"

api_key = os.getenv("OPENAI_API_KEY")
```

En frameworks como LangChain, FastAPI, CrewAI o Semantic Kernel prácticamente toda la información se intercambia mediante variables: prompts, respuestas del modelo, configuraciones, embeddings, conexiones a bases de datos y claves de API.

Adoptar nombres descriptivos facilita la comprensión de flujos complejos y reduce errores en sistemas de producción.

---

# Buenas prácticas

- Utiliza nombres que describan claramente el propósito de la variable.
- Sigue la convención `snake_case` para variables y funciones.
- Reserva `UPPER_CASE` para constantes.
- Evita abreviaturas ambiguas.
- No reutilices una variable para representar conceptos diferentes.
- Mantén un estilo uniforme en todo el proyecto.
- Prefiere nombres significativos antes que nombres cortos.

---

# Errores conceptuales detectados en el curso

## Corrección 1. Una variable no es exactamente una "cajita en memoria"

El curso utiliza esta analogía para facilitar el aprendizaje.

### Corrección técnica

En Python, una variable es un **nombre que referencia un objeto**. No almacena directamente el valor.

Este detalle es fundamental para comprender posteriormente temas como mutabilidad, paso de argumentos, listas, diccionarios y clases.

---

## Corrección 2. Variables en MAYÚSCULAS

El curso indica que las variables en mayúsculas se utilizan para constantes.

### Corrección técnica

Python **no posee constantes nativas**. Es una convención establecida por la guía PEP 8.

Es perfectamente posible escribir:

```python
PI = 3.14

PI = 4
```

El intérprete no genera ningún error.

---

## Corrección 3. Guion bajo inicial

El curso menciona que el guion bajo inicial marca variables privadas.

### Corrección técnica

No crea privacidad real.

El prefijo `_` únicamente comunica a otros desarrolladores que ese elemento es de uso interno y no forma parte de la interfaz pública del módulo o clase.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué se dice que las variables en Python almacenan referencias y no valores?

### Qué evalúa

Comprensión del modelo de objetos de Python.

### Errores comunes

- Decir que la variable contiene físicamente el dato.
- Confundir memoria con referencia.

### Respuesta de alto impacto

> En Python las variables son identificadores que apuntan a objetos almacenados en memoria. La variable no contiene el objeto; mantiene una referencia hacia él. Este modelo explica el comportamiento de la mutabilidad, el paso de parámetros y la reasignación de variables.

---

## Pregunta 2

¿Qué significa que Python sea un lenguaje *case sensitive*?

### Qué evalúa

Conocimiento de la sintaxis del lenguaje.

### Errores comunes

- Pensar que `x` y `X` representan la misma variable.

### Respuesta de alto impacto

> Python distingue entre letras mayúsculas y minúsculas en los identificadores. Por ello, `usuario`, `Usuario` y `USUARIO` son tres variables completamente diferentes y pueden coexistir dentro del mismo programa.

---

## Pregunta 3

¿Por qué PEP 8 recomienda `snake_case` para variables?

### Qué evalúa

Conocimiento de estándares de desarrollo.

### Errores comunes

- Responder únicamente "porque es más bonito".

### Respuesta de alto impacto

> PEP 8 busca uniformidad y legibilidad en el ecosistema Python. Utilizar `snake_case` permite que el código mantenga un estilo consistente con la biblioteca estándar y con la mayoría de proyectos de código abierto, facilitando la colaboración entre desarrolladores.

---

## Pregunta 4

¿Por qué no existen constantes reales en Python?

### Qué evalúa

Comprensión del lenguaje y de sus convenciones.

### Errores comunes

- Afirmar que una variable en mayúsculas es inmutable.

### Respuesta de alto impacto

> Python no implementa un mecanismo para impedir la reasignación de variables. Las constantes se representan únicamente mediante la convención `UPPER_CASE` definida en PEP 8; el intérprete no impide modificar su valor.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Variables y Assignment Statements.
- Python Documentation — Built-in Functions.
- Python Documentation — `id()` y `type()`.

## PEPs

- PEP 8 — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Python Cookbook* — David Beazley y Brian K. Jones.
- *Effective Python* — Brett Slatkin.

---