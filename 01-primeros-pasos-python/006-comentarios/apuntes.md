# Clase 6 — Comentarios en Python

## Objetivos de aprendizaje

Al finalizar esta clase serás capaz de:

- Comprender qué son los comentarios y cuál es su propósito.
- Escribir comentarios de una línea correctamente.
- Diferenciar entre comentarios reales y cadenas multilínea.
- Desactivar temporalmente instrucciones para realizar pruebas y depuración.
- Aplicar buenas prácticas de documentación sin generar código innecesariamente verboso.

---

# Introducción

Los comentarios son uno de los mecanismos más simples del lenguaje, pero también uno de los más importantes para escribir software mantenible.

Un comentario **no modifica el comportamiento del programa**, ya que el intérprete de Python lo ignora completamente durante la ejecución.

Su objetivo es facilitar la comprensión del código por parte del propio desarrollador y del resto del equipo.

En proyectos profesionales, un buen comentario puede ahorrar horas de análisis, mientras que un comentario innecesario puede dificultar la lectura del código.

---

# ¿Qué es un comentario?

Un comentario es texto incluido dentro del código fuente que **no forma parte del programa ejecutable**.

Python lo ignora completamente durante la interpretación.

Su propósito es:

- documentar decisiones de diseño;
- explicar lógica compleja;
- dejar contexto para otros desarrolladores;
- desactivar temporalmente código durante pruebas.

---

# Comentarios de una línea

Python utiliza el carácter:

```python
#
```

Todo lo que aparezca después de este símbolo será ignorado hasta el final de la línea.

Ejemplo:

```python
# Este es un comentario

print("Hola Mundo")
```

Salida:

```text
Hola Mundo
```

El comentario no produce ninguna salida ni afecta la ejecución del programa.

---

# Comentarios al final de una instrucción

También es posible comentar al final de una línea de código.

Ejemplo:

```python
print("Hola Mundo")  # Imprime un saludo en la consola
```

Python ejecuta la instrucción `print()` e ignora todo lo que aparece después del `#`.

Este tipo de comentario suele utilizarse para aclarar una instrucción cuya intención no resulta evidente.

---

# ¿Qué ocurre si escribes texto sin comentar?

Ejemplo:

```python
Esta es una línea de código
```

El intérprete intentará interpretar ese texto como código Python y generará un error.

Para convertirlo en comentario basta con escribir:

```python
# Esta es una línea de código
```

Ahora el intérprete lo ignorará completamente.

---

# Comentarios multilínea

El contenido original presenta dos formas de escribir comentarios multilínea.

Sin embargo, es importante distinguir entre la práctica mostrada en el curso y el funcionamiento real del lenguaje.

---

## Opción 1: Un `#` por línea (recomendado)

```python
# Este es un comentario
# que ocupa varias líneas.
# Python ignorará todas ellas.
```

Esta es la forma recomendada por la guía oficial de estilo **PEP 8**.

Cada línea es un comentario independiente y el comportamiento es completamente explícito.

---

## Opción 2: Comillas triples (`""" """`)

Ejemplo mostrado en el curso:

```python
"""
Este será un comentario
multilínea.
"""

print("Hola Mundo")
```

El programa imprime:

```text
Hola Mundo
```

Aunque el resultado parece el mismo, técnicamente **esto no es un comentario**.

---

# Funcionamiento interno de las comillas triples

Las comillas triples crean un **string multilínea**.

Ejemplo:

```python
"""
Hola
"""
```

Internamente Python interpreta algo equivalente a:

```python
str("Hola")
```

Como la cadena no se asigna a ninguna variable ni se utiliza posteriormente, el intérprete simplemente la descarta.

Por esta razón muchas personas la utilizan como si fuera un comentario.

---

# Diferencia entre comentarios y cadenas multilínea

| `#` | `""" """` |
|------|-----------|
| Comentario real | Cadena de texto |
| El intérprete la ignora | El intérprete crea un objeto `str` y luego lo descarta |
| Recomendado para documentar | Se utiliza principalmente para *docstrings* |
| Recomendado por PEP 8 | No recomendado como comentario general |

Esta diferencia suele aparecer en entrevistas técnicas y es importante comprenderla.

---

# ¿Qué son los Docstrings?

Aunque el curso no lo menciona, las comillas triples tienen un propósito específico en Python.

Se utilizan para escribir **docstrings**, es decir, documentación oficial de:

- módulos;
- funciones;
- clases;
- métodos.

Ejemplo:

```python
def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b
```

El texto puede consultarse posteriormente mediante:

```python
help(sumar)
```

Por ello, utilizar `""" """` como comentario general no es la práctica recomendada.

---

# Desactivar temporalmente código

Una de las aplicaciones más frecuentes de los comentarios consiste en desactivar instrucciones sin eliminarlas.

Ejemplo:

```python
print("Línea 1")

# print("Línea 2")

print("Línea 3")
```

Salida:

```text
Línea 1
Línea 3
```

La segunda instrucción permanece en el archivo, pero Python no la ejecuta.

---

# ¿Cuándo resulta útil?

Durante el desarrollo es habitual comentar temporalmente una línea para:

- aislar un error;
- probar una funcionalidad específica;
- comparar comportamientos;
- depurar un programa.

Posteriormente conviene eliminar el código comentado cuando deje de ser necesario.

---

# Flujo de ejecución

```text
Archivo .py

↓

Python lee una línea

↓

¿Empieza con #?

├── Sí → Ignorar línea
└── No

↓

Interpretar como código Python

↓

Ejecutar
```

---

# Buenas prácticas

## Comentar cuando...

- la lógica no es evidente;
- existe una decisión de diseño importante;
- es necesario documentar una limitación;
- se deja una referencia para futuras modificaciones.

---

## Evitar comentar...

```python
x = x + 1  # Incrementa x en uno
```

Este comentario no aporta información adicional.

El propio código ya expresa claramente lo que hace.

---

## Preferir comentarios que expliquen el "por qué"

En lugar de:

```python
# Multiplica por 100
precio = precio * 100
```

Es preferible:

```python
# La API externa espera el precio en céntimos.
precio = precio * 100
```

El segundo comentario aporta contexto que no puede deducirse únicamente leyendo el código.

---

# Problemas frecuentes en producción

## Error 1: Código comentado durante meses

Es habitual encontrar bloques completos comentados.

Esto genera:

- confusión;
- duplicación;
- dificultad para mantener el proyecto.

### Solución

Si el código ya no es necesario, eliminarlo.

Git conserva el historial de cambios.

---

## Error 2: Comentar código en lugar de utilizar Git

Muchos desarrolladores principiantes hacen esto:

```python
# Versión antigua
# ...

# Nueva versión
# ...
```

En proyectos profesionales esto no es recomendable.

El historial debe mantenerse mediante Git, no mediante comentarios.

---

## Error 3: Comentarios desactualizados

El código cambia, pero el comentario permanece igual.

Esto resulta más peligroso que no tener comentarios.

Siempre deben mantenerse sincronizados con el comportamiento real del programa.

---

# Buenas prácticas

- Escribir comentarios únicamente cuando aporten contexto.
- Preferir comentarios breves y precisos.
- Utilizar `#` para comentarios normales.
- Reservar `""" """` para docstrings.
- Eliminar código comentado cuando deje de ser útil.
- No utilizar comentarios para almacenar versiones antiguas del código.

---

# Relación con la Ingeniería de IA

Los comentarios son especialmente importantes en proyectos de IA debido a la complejidad de muchos algoritmos.

Ejemplo:

```python
# Se utiliza cosine similarity porque el modelo genera embeddings normalizados.
similaridad = cosine_similarity(v1, v2)
```

Este tipo de explicación ayuda a comprender decisiones técnicas que no son evidentes leyendo únicamente el código.

En proyectos con LangChain, LangGraph, FastAPI o modelos de Machine Learning es frecuente documentar:

- decisiones de arquitectura;
- estrategias de recuperación (RAG);
- prompts complejos;
- parámetros de entrenamiento;
- integraciones con APIs externas.

---

# Correcciones y actualización respecto al contenido original

## Corrección 1: Las comillas triples no son comentarios

El material del curso indica que pueden utilizarse como comentarios multilínea.

Técnicamente esto es incorrecto.

Las comillas triples crean una cadena de texto (*string*). Cuando dicha cadena no se asigna a ninguna variable, Python simplemente la descarta.

Su uso principal es la creación de **docstrings**, no de comentarios generales.

---

## Corrección 2: Comentar código para desactivarlo

El curso propone comentar líneas para realizar pruebas.

Esto es válido para cambios temporales.

Sin embargo, en proyectos profesionales no debe utilizarse para conservar versiones antiguas del código. Esa función corresponde a Git.

---

# Preguntas técnicas de entrevista

## 1. ¿Cuál es la diferencia entre un comentario (`#`) y una cadena delimitada por comillas triples?

**Qué evalúa:** Comprensión del funcionamiento interno del intérprete y del propósito de los docstrings.

**Error común:** Responder que ambos son exactamente lo mismo.

---

## 2. ¿Qué son los docstrings y para qué se utilizan?

**Qué evalúa:** Conocimiento de documentación interna en Python.

**Error común:** Pensar que son simplemente comentarios multilínea.

---

## 3. ¿Cuándo un comentario aporta valor y cuándo debería eliminarse?

**Qué evalúa:** Capacidad para escribir código mantenible y seguir buenas prácticas.

**Error común:** Comentar cada línea del programa o conservar grandes bloques de código comentado.

---

# Recursos oficiales

- PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/
- PEP 257 – Docstring Conventions: https://peps.python.org/pep-0257/
- Documentación oficial de Python: https://docs.python.org/3/tutorial/
```