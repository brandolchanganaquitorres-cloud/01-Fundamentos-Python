# Clase 28. Módulos en Python (`import`, `from ... import`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender qué son los módulos en Python, aprender a dividir un proyecto en múltiples archivos, reutilizar código mediante `import` y `from ... import`, entender cómo funciona internamente el sistema de importación y conocer las buenas prácticas utilizadas en proyectos profesionales.

---

# Contenido del curso

Hasta este punto, todo el código se encontraba dentro de un único archivo.

Sin embargo, cuando un proyecto crece, mantener cientos o miles de líneas en un solo archivo se vuelve difícil de mantener.

Python resuelve este problema mediante los **módulos**.

Un módulo es simplemente un archivo `.py` que contiene código reutilizable.

Puede incluir:

- funciones;
- variables;
- clases;
- constantes.

Posteriormente, dicho código puede utilizarse desde otros archivos del proyecto.

---

# ¿Qué es un módulo?

Supongamos la siguiente estructura.

```text
Proyecto

│

├── main.py

└── operaciones.py
```

El archivo `operaciones.py` contiene la lógica matemática.

```python
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b
```

Mientras tanto, `main.py` únicamente coordina la ejecución del programa.

---

# ¿Por qué utilizar módulos?

Sin módulos.

```text
main.py

↓

5000 líneas

↓

Difícil de mantener
```

Con módulos.

```text
main.py

↓

Coordina

↓

operaciones.py

↓

Base de datos.py

↓

usuarios.py

↓

api.py
```

Cada archivo posee una única responsabilidad.

---

# Importar un módulo completo

La forma más sencilla consiste en utilizar `import`.

```python
import operaciones

print(
    operaciones.sumar(2, 3)
)
```

Resultado.

```text
5
```

---

# Funcionamiento interno

```text
main.py

↓

import operaciones

↓

Buscar archivo

↓

Cargar módulo

↓

Crear espacio de nombres

↓

Disponible como

operaciones
```

Después del `import`, todo el contenido del módulo queda agrupado bajo el nombre:

```python
operaciones
```

---

# Acceder a una función

La sintaxis es:

```python
modulo.funcion()
```

Ejemplo.

```python
operaciones.multiplicar(4, 6)
```

Resultado.

```text
24
```

---

# ¿Cuándo utilizar `import`?

Esta forma resulta recomendable cuando:

- el módulo contiene muchas funciones;
- existen funciones con nombres similares en distintos módulos;
- se desea que el origen de cada función sea evidente.

Por ejemplo.

```python
matematicas.sumar()

finanzas.sumar()
```

El nombre del módulo evita ambigüedades.

---

# Importar funciones específicas

También es posible importar únicamente aquello que se necesita.

```python
from operaciones import (
    sumar,
    restar,
    multiplicar,
    dividir
)
```

Ahora las funciones pueden utilizarse directamente.

```python
print(sumar(2, 3))
```

Resultado.

```text
5
```

---

# Más ejemplos

```python
print(restar(2, 3))
```

Resultado.

```text
-1
```

---

```python
print(multiplicar(2, 3))
```

Resultado.

```text
6
```

---

```python
print(dividir(10, 5))
```

Resultado.

```text
2.0
```

La división devuelve un número de tipo `float`, incluso cuando el resultado es exacto.

---

# Diferencia entre `import` y `from ... import`

| Forma | Uso |
|--------|-----|
| `import operaciones` | Acceso mediante `operaciones.funcion()` |
| `from operaciones import sumar` | Acceso directo mediante `sumar()` |

---

# Funcionamiento interno

Con:

```python
import operaciones
```

Python crea el siguiente espacio de nombres.

```text
operaciones

↓

sumar()

restar()

multiplicar()

dividir()
```

Mientras que con:

```python
from operaciones import sumar
```

Únicamente incorpora la función solicitada al espacio de nombres actual.

```text
main.py

↓

sumar()
```

---

# ¿Qué ocurre realmente cuando usamos `import`?

Cuando Python encuentra:

```python
import operaciones
```

No ejecuta inmediatamente todas las funciones.

El proceso interno es aproximadamente el siguiente.

```text
Encontrar import

↓

Buscar archivo

↓

Compilar si es necesario

↓

Ejecutar el módulo una única vez

↓

Guardar en memoria

↓

Registrar en sys.modules

↓

Entregar referencia
```

Esto significa que un mismo módulo no se vuelve a cargar cada vez que aparece un nuevo `import`.

Python reutiliza la versión ya cargada.

---

# El sistema de caché de módulos

Supongamos.

```python
import operaciones

import operaciones

import operaciones
```

El archivo **no se ejecuta tres veces**.

Python detecta que ya está cargado.

```text
Primer import

↓

Cargar módulo

↓

Guardar en caché
```

Los siguientes `import`.

```text
Consultar caché

↓

Reutilizar módulo existente
```

Este comportamiento mejora significativamente el rendimiento de aplicaciones grandes.

---

# Organización de proyectos

Una aplicación sencilla podría organizarse así.

```text
calculadora/

│

├── main.py

├── operaciones.py

├── interfaz.py

└── configuracion.py
```

Cada archivo tiene una responsabilidad específica.

---

# Arquitectura profesional

En proyectos reales suele encontrarse una estructura similar.

```text
proyecto/

│

├── main.py

├── api/

│   ├── rutas.py

│   ├── autenticacion.py

│   └── respuestas.py

│

├── modelos/

├── servicios/

├── utilidades/

├── configuracion/

└── pruebas/
```

Los módulos permiten escalar el proyecto sin convertir un archivo en miles de líneas de código.

---

# Importar múltiples funciones

Es posible importar varias funciones simultáneamente.

```python
from operaciones import (
    sumar,
    restar,
    multiplicar,
    dividir
)
```

Esto reduce la cantidad de código repetitivo cuando solo se necesitan unas pocas funciones.

---

# ¿Qué ocurre si dos módulos tienen funciones con el mismo nombre?

Supongamos.

```python
from matematicas import sumar

from finanzas import sumar
```

La segunda importación reemplaza a la primera dentro del espacio de nombres actual.

Para evitar este problema suele preferirse.

```python
import matematicas

import finanzas
```

Y utilizar.

```python
matematicas.sumar()

finanzas.sumar()
```

---

# Alias con `as`

Python permite asignar un alias durante la importación.

```python
import operaciones as op
```

Posteriormente.

```python
print(op.sumar(2, 3))
```

Resultado.

```text
5
```

También puede utilizarse con funciones.

```python
from operaciones import sumar as suma
```

Ahora.

```python
print(suma(5, 8))
```

---

# ¿Cuándo utilizar alias?

Los alias son útiles cuando:

- el nombre del módulo es muy largo;
- existen conflictos de nombres;
- se siguen convenciones ampliamente adoptadas por la comunidad.

Ejemplos habituales.

```python
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
```

---

# AI Engineering

Los módulos son esenciales en cualquier proyecto de IA.

Una arquitectura simplificada podría ser.

```text
Proyecto IA

│

├── main.py

├── prompts.py

├── embeddings.py

├── llm.py

├── rag.py

├── herramientas.py

├── utilidades.py

└── configuracion.py
```

Cada módulo encapsula una responsabilidad concreta.

### Caso práctico

```python
from llm import generar_respuesta

from rag import recuperar_documentos

from embeddings import generar_embedding
```

Esta organización facilita el mantenimiento, las pruebas y la evolución del sistema.

---

# Problemas reales en producción

## Problema 1

Colocar todo el proyecto en un único archivo.

```text
main.py

↓

8000 líneas
```

El código resulta difícil de comprender, probar y mantener.

---

## Problema 2

Importaciones circulares.

```text
usuarios.py

↓

import pedidos
```

```text
pedidos.py

↓

import usuarios
```

Esto puede producir errores porque ambos módulos dependen mutuamente durante la carga.

Una solución habitual consiste en extraer el código compartido a un tercer módulo.

---

## Problema 3

Importar todo mediante `*`

```python
from operaciones import *
```

Aunque es válido, dificulta saber de dónde proviene cada función y aumenta el riesgo de conflictos de nombres.

---

## Problema 4

Ejecutar código al importar un módulo.

```python
print("Iniciando...")
```

Todo el código situado en el nivel superior del archivo se ejecuta durante la importación.

Si el módulo solo debe definir funciones y clases, conviene evitar efectos secundarios innecesarios.

---

# Buenas prácticas

- Organiza el proyecto en módulos pequeños y cohesionados.
- Asigna a cada módulo una única responsabilidad.
- Prefiere `import modulo` cuando la procedencia de las funciones deba ser explícita.
- Utiliza `from ... import ...` únicamente cuando necesites pocas funciones y el contexto sea claro.
- Evita `from modulo import *` en proyectos profesionales.
- Aprovecha alias (`as`) cuando mejoren la legibilidad o sigan convenciones del ecosistema.
- Mantén los nombres de los módulos en minúsculas siguiendo `snake_case`, como recomienda PEP 8.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "Un módulo solo contiene funciones"

### Corrección técnica

Un módulo puede contener prácticamente cualquier objeto de Python:

- funciones;
- clases;
- variables;
- constantes;
- excepciones;
- decoradores;
- documentación.

Incluso puede ejecutar código cuando es importado.

---

## Corrección 2. "`from ... import ...` es siempre mejor porque escribe menos"

### Corrección técnica

No necesariamente.

Aunque reduce la cantidad de texto, también elimina información sobre el origen de las funciones. En proyectos grandes suele preferirse `import modulo` porque hace el código más explícito y reduce conflictos entre nombres.

---

## Corrección 3. "Cada vez que se ejecuta `import`, Python vuelve a leer el archivo"

### Corrección técnica

No. Python mantiene un registro de los módulos ya cargados en `sys.modules`. Si el módulo ya fue importado durante la ejecución del programa, reutiliza la instancia existente en lugar de volver a cargar el archivo, salvo que se utilice explícitamente `importlib.reload()`.

---

## Corrección 4. "Un módulo es simplemente un archivo"

### Corrección técnica

Aunque físicamente un módulo suele corresponder a un archivo `.py`, desde el punto de vista del intérprete un módulo es un **objeto** cargado en memoria. Una vez importado, puede consultarse con `type()`.

```python
import operaciones

print(type(operaciones))
```

Resultado.

```python
<class 'module'>
```

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre `import modulo` y `from modulo import funcion`?

### Qué evalúa

Comprensión del sistema de importación y del espacio de nombres.

### Errores comunes

- Responder únicamente que uno "es más corto".

### Respuesta de alto impacto

> `import modulo` incorpora el módulo completo y obliga a acceder mediante `modulo.funcion()`, dejando claro el origen de cada llamada. `from modulo import funcion` importa únicamente los nombres solicitados al espacio de nombres actual, lo que hace el código más conciso, pero puede generar conflictos si existen funciones con el mismo nombre.

---

## Pregunta 2

¿Por qué Python no vuelve a cargar un módulo en cada `import`?

### Qué evalúa

Conocimiento del funcionamiento interno del intérprete.

### Errores comunes

- Pensar que el archivo se lee en cada importación.

### Respuesta de alto impacto

> Porque Python mantiene una caché de módulos en `sys.modules`. La primera vez que un módulo se importa se carga y ejecuta; las siguientes importaciones reutilizan el objeto ya existente en memoria, mejorando el rendimiento y garantizando que el estado del módulo se conserve durante la ejecución.

---

## Pregunta 3

¿Por qué `from modulo import *` suele desaconsejarse?

### Qué evalúa

Conocimiento de buenas prácticas y mantenibilidad.

### Errores comunes

- Responder únicamente que "consume más memoria".

### Respuesta de alto impacto

> Porque incorpora todos los nombres públicos del módulo al espacio de nombres actual, dificultando identificar su procedencia y aumentando la probabilidad de colisiones entre nombres. En proyectos profesionales se prefieren importaciones explícitas o el uso del nombre del módulo para mantener el código más claro y fácil de mantener.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Modules.
- Python Documentation — The Import System.
- Python Documentation — Packages.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 302** — New Import Hooks.
- **PEP 328** — Imports: Multi-Line and Absolute/Relative Imports.
- **PEP 451** — A ModuleSpec Type for the Import System.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.
```