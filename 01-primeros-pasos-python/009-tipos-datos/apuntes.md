# Clase 9. Tipos de datos en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender en profundidad los tipos de datos fundamentales de Python, cómo son implementados internamente, cuándo utilizar cada uno en aplicaciones reales, cuáles son sus implicancias en rendimiento, mutabilidad y diseño de software, y cómo aparecen diariamente en proyectos modernos de AI Engineering, APIs, procesamiento de datos y sistemas distribuidos.

---

# Contenido del curso

Los **tipos de datos** determinan cómo Python representa, almacena y manipula la información en memoria.

Elegir correctamente un tipo de dato no solo mejora la legibilidad del código, sino que también influye en:

- rendimiento;
- consumo de memoria;
- facilidad de mantenimiento;
- complejidad del algoritmo;
- escalabilidad del software.

En Python prácticamente todo es un **objeto**, por lo que cada tipo de dato posee atributos, métodos y un comportamiento definido por el Data Model del lenguaje.

---

# Strings (cadenas de caracteres)

Los **strings** representan texto.

Existen tres formas válidas de declararlos.

```python
texto1 = 'Este es un texto'

texto2 = "Este es un texto"

texto3 = """Este es un texto"""
```

También es posible utilizar:

```python
texto4 = '''Este es un texto'''
```

Las cuatro declaraciones generan objetos del mismo tipo.

```python
print(type(texto1))
```

Salida:

```python
<class 'str'>
```

---

## ¿Cuándo utilizar comillas triples?

Las comillas triples son especialmente útiles cuando el texto contiene múltiples líneas.

```python
mensaje = """
Hola.

Este mensaje tiene varias líneas.

Saludos.
"""
```

También permiten escribir texto que contiene comillas simples y dobles sin necesidad de escapar caracteres.

```python
texto = """
Ella dijo:
"Python es increíble"

Y respondió:
'Totalmente de acuerdo.'
"""
```

---

# Expansión técnica

## ¿Cómo funciona realmente un String?

Internamente un string es un objeto inmutable.

```text
Variable

↓

Referencia

↓

Objeto str

↓

Secuencia de caracteres Unicode
```

Una vez creado:

```python
nombre = "Brandol"
```

Python **no modifica** ese objeto.

Cuando hacemos:

```python
nombre += " Changanaqui"
```

NO amplía el objeto existente.

Internamente ocurre algo parecido a:

```text
Objeto antiguo

↓

Se crea un nuevo objeto

↓

La variable apunta al nuevo objeto

↓

El objeto anterior queda disponible para el Garbage Collector si no existen más referencias.
```

Esta característica explica por qué concatenar miles de cadenas mediante `+` resulta ineficiente.

---

## Producción

En aplicaciones modernas es habitual utilizar strings para almacenar:

```python
OPENAI_API_KEY

AZURE_OPENAI_ENDPOINT

MODEL_NAME

DATABASE_URL

JWT_SECRET

REDIS_HOST
```

Por este motivo, comprender cómo funcionan los strings resulta esencial para desarrollar APIs, microservicios y sistemas de IA.

---

# Números

Python incorpora tres tipos numéricos fundamentales.

## Enteros

```python
edad = 30
```

Tipo:

```python
int
```

No poseen parte decimal.

---

## Flotantes

```python
pi = 3.1415926535
```

Tipo:

```python
float
```

Python utiliza el punto (`.`) como separador decimal.

---

## Complejos

```python
z = 5 + 2j
```

Tipo:

```python
complex
```

La letra `j` representa la parte imaginaria.

Los números complejos son utilizados principalmente en:

- procesamiento digital de señales;
- ingeniería eléctrica;
- física;
- simulaciones;
- computación científica.

---

# Expansión técnica

## ¿Cómo almacena Python los enteros?

Los enteros de Python poseen precisión arbitraria.

Esto significa que:

```python
numero = 99999999999999999999999999999999999999999999999999999999999
```

es perfectamente válido.

A diferencia de lenguajes como C o Java, Python no limita los enteros a 32 o 64 bits, sino que aumenta dinámicamente el espacio necesario.

**Ventaja**

- No existe desbordamiento (*integer overflow*) en el uso normal.

**Costo**

- Mayor consumo de memoria para enteros muy grandes.

---

## ¿Por qué los `float` no son exactos?

Los números de punto flotante siguen el estándar IEEE 754.

Por ejemplo:

```python
0.1 + 0.2
```

produce:

```python
0.30000000000000004
```

No es un error de Python.

Es una consecuencia de cómo los números decimales se representan en binario.

### Problema real

En aplicaciones financieras **no debe utilizarse `float` para dinero**.

Debe utilizarse:

```python
from decimal import Decimal
```

---

# Colecciones

Python ofrece distintas estructuras para almacenar múltiples elementos.

---

# Listas

Las listas son colecciones:

- ordenadas;
- mutables;
- indexadas.

```python
lista = [0,1,2,3,4,5]
```

Cada elemento posee un índice.

```python
lista[0]
```

↓

```text
0
```

---

## Mutabilidad

Podemos modificar cualquier elemento.

```python
lista[0] = 100
```

---

# Expansión técnica

## ¿Cómo funciona internamente una lista?

Una lista NO almacena directamente los objetos.

Almacena referencias.

```text
Lista

↓

Referencia

↓

Objeto

↓

Referencia

↓

Objeto

↓

Referencia

↓

Objeto
```

Por esta razón una lista puede contener simultáneamente:

```python
datos = [
    30,
    "Python",
    True,
    3.14,
    {"pais": "Perú"}
]
```

---

## Complejidad temporal

| Operación | Complejidad |
|------------|------------:|
| Acceso por índice | O(1) |
| append() | O(1) amortizado |
| insert(0) | O(n) |
| eliminar inicio | O(n) |
| búsqueda | O(n) |

Comprender estas diferencias resulta fundamental cuando se trabaja con grandes volúmenes de datos.

---

# Tuplas

Las tuplas son colecciones:

- ordenadas;
- indexadas;
- inmutables.

```python
coordenadas = (10,20)
```

No pueden modificarse después de su creación.

---

# ¿Cuándo utilizar una tupla?

Cuando los datos representan una entidad que no debe cambiar.

Ejemplos:

```python
RGB = (255,255,255)

VERSION = (3,13)

COORDENADAS = (-12.0464,-77.0428)
```

---

# Expansión técnica

Las tuplas consumen menos memoria que las listas y su inmutabilidad permite ciertas optimizaciones internas.

En sistemas de IA suelen utilizarse para representar configuraciones, coordenadas, dimensiones y valores constantes.

---

# Diccionarios

Los diccionarios almacenan información mediante pares:

```text
clave

↓

valor
```

Ejemplo:

```python
persona = {
    "nombre":"Brandol",
    "edad":30,
    "pais":"Perú"
}
```

Desde Python **3.7** el orden de inserción forma parte de la especificación del lenguaje.

---

# Expansión técnica

Internamente un diccionario se implementa mediante una **tabla hash (Hash Table)**.

```text
Clave

↓

Hash()

↓

Bucket

↓

Valor
```

Esto permite que operaciones como:

```python
persona["edad"]
```

tengan complejidad promedio:

```text
O(1)
```

---

## Caso real

Las respuestas JSON de una API se transforman automáticamente en diccionarios.

```python
respuesta = {
    "model":"gpt-5.5",
    "usage":{
        "input_tokens":124,
        "output_tokens":321
    }
}
```

Este patrón aparece continuamente al trabajar con SDKs de IA, APIs REST y servicios en la nube.

---

# Sets (Conjuntos)

Los conjuntos son colecciones:

- mutables;
- sin elementos duplicados;
- no indexadas.

```python
conjunto = {1,1,2,2,3}

print(conjunto)
```

Salida:

```python
{1,2,3}
```

---

# Expansión técnica

Internamente también utilizan tablas hash.

Su principal ventaja es la velocidad.

| Operación | Complejidad |
|------------|------------:|
| búsqueda | O(1) |
| inserción | O(1) |
| eliminación | O(1) |

---

## Caso real en AI Engineering

Eliminar documentos duplicados antes de generar embeddings.

```python
documentos = list(set(documentos))
```

O eliminar IDs repetidos provenientes de múltiples fuentes de datos antes de indexarlos en una base vectorial.

---

# Booleanos

Los booleanos únicamente pueden tomar dos valores.

```python
True

False
```

Siempre comienzan con mayúscula.

```python
activo = True

premium = False
```

---

# Expansión técnica

Internamente `bool` es una subclase de `int`.

```python
True == 1

False == 0
```

Por ejemplo:

```python
print(True + True)
```

Salida:

```python
2
```

Aunque este comportamiento existe, **no debe utilizarse para escribir código de negocio**, ya que reduce la claridad.

---

# Comparativa de estructuras de datos

| Tipo | Ordenado | Mutable | Duplicados | Acceso |
|------|:---------:|:--------:|:----------:|:-------:|
| str | Sí | No | Sí | Índice |
| list | Sí | Sí | Sí | Índice |
| tuple | Sí | No | Sí | Índice |
| dict | Sí (Python ≥3.7) | Sí | Claves únicas | Clave |
| set | No | Sí | No | No |

---

# Problemas reales en producción

## Problema 1

Utilizar una lista cuando realmente se necesita una búsqueda rápida.

```python
if usuario in usuarios:
```

Con millones de registros esto resulta mucho más lento que utilizar un `set`.

---

## Problema 2

Utilizar `float` para cálculos financieros.

Puede generar errores de precisión acumulados.

---

## Problema 3

Modificar accidentalmente una lista compartida entre múltiples componentes.

En sistemas grandes esto provoca efectos secundarios difíciles de depurar.

---

## Problema 4

Intentar acceder por índice a un `set`.

```python
mi_set[0]
```

Produce:

```text
TypeError
```

Porque los conjuntos no mantienen posiciones.

---

# Aplicación en AI Engineering

Los tipos de datos aparecen constantemente en sistemas de IA modernos.

| Tipo | Ejemplo real |
|------|--------------|
| `str` | Prompts, API Keys, nombres de modelos, URLs |
| `int` | Tokens, batch size, epochs |
| `float` | Temperature, Top-P, learning rate |
| `list` | Conversaciones (`messages`), documentos recuperados, embeddings por lotes |
| `tuple` | Coordenadas, tamaños de imagen, dimensiones de tensores |
| `dict` | JSON de APIs, configuración de modelos, respuestas de SDKs |
| `set` | Eliminación de IDs duplicados, documentos repetidos |
| `bool` | Feature flags, validaciones, control de flujo |

### Caso práctico: Flujo típico de un sistema RAG

```text
Usuario
      │
      ▼
Prompt (str)
      │
      ▼
Configuración (dict)
      │
      ▼
Documentos recuperados (list)
      │
      ▼
IDs únicos (set)
      │
      ▼
Parámetros del modelo
temperature (float)
max_tokens (int)
stream (bool)
      │
      ▼
Respuesta del LLM (dict → JSON)
```

Este patrón es habitual en aplicaciones construidas con FastAPI, LangChain, LangGraph, SDKs de OpenAI/Anthropic/Gemini y bases de datos vectoriales.

---

# Buenas prácticas

- Utiliza `tuple` para datos inmutables.
- Utiliza `list` cuando necesites modificar el contenido.
- Utiliza `set` para eliminar duplicados y acelerar búsquedas.
- Utiliza `dict` para representar entidades y respuestas JSON.
- Evita utilizar `float` para operaciones financieras; emplea `decimal.Decimal`.
- No elijas una estructura por costumbre: elige la que mejor represente el problema.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "Todas las formas de declarar un string funcionan igual"

### Corrección técnica

Aunque generan objetos `str`, las **comillas triples no son un tipo diferente de cadena**. Son una sintaxis que facilita escribir cadenas multilínea y docstrings. No deben confundirse con comentarios multilínea.

---

## Corrección 2. "Los diccionarios son ordenados"

### Corrección técnica

Esta afirmación es correcta **únicamente para Python 3.7 o superior**, donde el orden de inserción forma parte de la especificación del lenguaje. En versiones anteriores era un detalle de implementación y no una garantía.

---

## Corrección 3. "Los sets son desordenados"

### Corrección técnica

Desde la perspectiva del lenguaje, un `set` **no garantiza un orden de iteración**. Aunque en ejecuciones concretas pueda parecer estable, nunca debe dependerse de ese comportamiento en código de producción.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué Python utiliza tablas hash para implementar diccionarios y conjuntos?

**Qué evalúa:** Conocimiento de estructuras de datos y complejidad algorítmica.

**Errores comunes:** Pensar que son listas con otra sintaxis.

**Respuesta de alto impacto:**

> Tanto `dict` como `set` se implementan sobre tablas hash, lo que permite operaciones promedio de búsqueda, inserción y eliminación en O(1). Esa eficiencia explica su uso masivo en APIs, cachés, deduplicación y procesamiento de datos.

---

## Pregunta 2

¿Cuándo elegirías una tupla en lugar de una lista?

**Qué evalúa:** Diseño de modelos de datos.

**Errores comunes:** Responder únicamente "porque no cambia".

**Respuesta de alto impacto:**

> Utilizaría una tupla cuando la inmutabilidad forme parte del dominio del problema, por ejemplo coordenadas, versiones o configuraciones constantes. Además de comunicar intención, reduce modificaciones accidentales y puede ofrecer optimizaciones internas.

---

## Pregunta 3

¿Por qué `0.1 + 0.2` no devuelve exactamente `0.3`?

**Qué evalúa:** Comprensión de representación numérica.

**Errores comunes:** Decir que es un error de Python.

**Respuesta de alto impacto:**

> No es un error de Python, sino una consecuencia del estándar IEEE 754. Muchos decimales no pueden representarse exactamente en binario, por lo que pequeñas imprecisiones son inevitables. En dominios financieros se recomienda `decimal.Decimal`.

---

## Recursos recomendados

### Documentación oficial

- Python Documentation — Built-in Types.
- Python Documentation — Data Model.
- Python Documentation — Standard Types.
- Python Documentation — `decimal`.

### PEPs

- PEP 8 — Style Guide for Python Code.
- PEP 393 — Flexible String Representation.
- PEP 468 — Preserving Keyword Argument Order.
- PEP 520 — Preserving Class Attribute Definition Order.

### Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.
- *High Performance Python* — Micha Gorelick y Ian Ozsvald.