# Clase 25. Diccionarios en Python (`dict`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo funcionan los diccionarios (`dict`) en Python, aprender a crear, acceder, modificar y recorrer pares clave-valor, dominar los métodos más utilizados (`get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `popitem()`, `clear()`) y utilizar diccionarios anidados para modelar información estructurada.

---

# Contenido del curso

Los **diccionarios** (`dict`) son una estructura de datos que almacena información mediante **pares clave-valor** (*key-value pairs*).

Cada clave identifica de forma única un valor asociado.

Desde **Python 3.7**, los diccionarios conservan el **orden de inserción**, aunque siguen siendo estructuras optimizadas para búsquedas rápidas por clave y no para acceso por posición.

Son una de las estructuras más utilizadas en Python porque permiten representar objetos del mundo real de forma clara y flexible.

---

# Crear un diccionario

Los diccionarios se crean utilizando llaves (`{}`).

```python
auto = {
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}

print(auto)
```

Resultado.

```text
{
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2025
}
```

---

# Tipo de dato

```python
print(type(auto))
```

Resultado.

```python
<class 'dict'>
```

---

# ¿Qué es un par clave-valor?

Cada elemento del diccionario está formado por:

```text
Clave

↓

Valor
```

Ejemplo.

```python
"marca": "Renault"
```

- Clave → `"marca"`
- Valor → `"Renault"`

Cada clave identifica un dato específico.

---

# Funcionamiento interno

Conceptualmente, un diccionario funciona como una agenda.

```text
Clave

↓

Buscar

↓

Valor
```

No necesitamos conocer una posición o índice; basta con la clave.

---

# Acceder a un valor

## Utilizando corchetes

```python
print(auto["marca"])
```

Resultado.

```text
Renault
```

---

## Utilizando `get()`

```python
print(auto.get("marca"))
```

Resultado.

```text
Renault
```

Ambos métodos obtienen el mismo valor cuando la clave existe.

---

# Diferencia entre `[]` y `get()`

Existe una diferencia importante cuando la clave no está presente.

```python
print(auto["color"])
```

Resultado.

```text
KeyError
```

---

Con `get()`.

```python
print(auto.get("color"))
```

Resultado.

```python
None
```

`get()` devuelve `None` por defecto en lugar de lanzar una excepción, lo que resulta útil cuando una clave es opcional.

---

# Obtener todas las claves

```python
print(auto.keys())
```

Resultado.

```text
dict_keys(['marca', 'modelo', 'año'])
```

---

# Obtener todos los valores

```python
print(auto.values())
```

Resultado.

```text
dict_values(['Renault', 'Clio', 2025])
```

---

# Expansión técnica

Los objetos devueltos por `keys()` y `values()` son **vistas dinámicas** (*view objects*).

Esto significa que reflejan automáticamente los cambios realizados en el diccionario.

```python
claves = auto.keys()

auto["color"] = "verde"

print(claves)
```

Resultado.

```text
dict_keys(['marca', 'modelo', 'año', 'color'])
```

No se crea una copia independiente.

---

# Verificar si una clave existe

```python
if "marca" in auto:
    print("La clave existe.")
```

Resultado.

```text
La clave existe.
```

El operador `in` comprueba la existencia de la **clave**, no del valor.

---

# Sensibilidad a mayúsculas y minúsculas

Python distingue entre:

```python
"marca"
```

y

```python
"Marca"
```

Son claves completamente diferentes.

Cuando los datos provienen de usuarios, suele ser recomendable normalizar las claves utilizando:

```python
.lower()
```

---

# Modificar un valor

```python
auto["año"] = 2020

print(auto)
```

Resultado.

```text
{
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2020
}
```

---

# Agregar un nuevo par

```python
auto["color"] = "verde"
```

Resultado.

```text
{
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2020,
    'color': 'verde'
}
```

---

# Método `update()`

Permite modificar y agregar varios pares en una sola operación.

```python
auto.update({
    "año": 2022,
    "puertas": 4
})
```

Resultado.

```text
{
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2022,
    'color': 'verde',
    'puertas': 4
}
```

---

# Diferencia entre asignación directa y `update()`

| Método | Modifica un par | Modifica varios pares |
|---------|-----------------|-----------------------|
| `diccionario["clave"] = valor` | ✅ Sí | ❌ No |
| `update()` | ✅ Sí | ✅ Sí |

`update()` resulta especialmente útil cuando varios cambios provienen de otra estructura de datos.

---

# Método `pop()`

Elimina una clave específica.

```python
auto.pop("puertas")
```

Resultado.

```text
{
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2022,
    'color': 'verde'
}
```

---

# Expansión técnica

`pop()` devuelve el valor eliminado.

```python
color = auto.pop("color")

print(color)
```

Resultado.

```text
verde
```

Esto permite extraer un dato y seguir utilizándolo.

---

# Método `popitem()`

Elimina el último par insertado.

```python
auto.popitem()
```

Desde Python 3.7 elimina el último elemento añadido al diccionario.

---

# Método `clear()`

Vacía completamente el diccionario.

```python
auto.clear()

print(auto)
```

Resultado.

```text
{}
```

---

# Recorrer un diccionario

## Solo las claves

```python
for clave in auto:
    print(clave)
```

---

También puede escribirse de forma explícita.

```python
for clave in auto.keys():
    print(clave)
```

Ambas formas producen el mismo resultado.

---

# Solo los valores

```python
for valor in auto.values():
    print(valor)
```

---

# Claves y valores simultáneamente

```python
for clave, valor in auto.items():
    print(clave, valor)
```

Resultado.

```text
marca Renault
modelo Clio
año 2025
```

---

# Funcionamiento interno de `items()`

```text
Diccionario

↓

items()

↓

(clave, valor)

↓

Desempaquetado

↓

clave

valor
```

El desempaquetado automático hace que este sea el patrón más utilizado para recorrer diccionarios.

---

# Diccionarios anidados

Un diccionario puede contener otros diccionarios como valores.

```python
familia = {
    "hijo1": {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2": {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3": {
        "nombre": "Marcelo",
        "edad": 6
    }
}
```

---

# Acceder a datos anidados

```python
print(
    familia["hijo1"]["nombre"]
)
```

Resultado.

```text
Pedro
```

Cada nivel de corchetes permite acceder a un nivel adicional de la estructura.

---

# Funcionamiento interno

```text
familia

↓

"hijo1"

↓

{
    nombre,
    edad
}

↓

"nombre"

↓

"Pedro"
```

---

# ¿Cuándo utilizar un diccionario?

Los diccionarios son ideales cuando:

- los datos tienen propiedades con nombre;
- se necesita acceder rápidamente mediante una clave;
- cada elemento posee múltiples atributos;
- se representan objetos o registros.

Ejemplos:

- usuarios;
- productos;
- configuraciones;
- respuestas JSON;
- perfiles;
- inventarios.

---

# Diccionario frente a lista

| Característica | Lista | Diccionario |
|---------------|--------|-------------|
| Acceso principal | Índice | Clave |
| Elementos identificados | Posición | Nombre |
| Orden de inserción | ✅ Sí | ✅ Sí (Python 3.7+) |
| Valores duplicados | ✅ Sí | ✅ Sí |
| Claves duplicadas | No aplica | ❌ No |

---

# AI Engineering

Los diccionarios son probablemente la estructura de datos más utilizada en aplicaciones de IA.

| Caso | Uso |
|------|-----|
| APIs | Respuestas JSON |
| OpenAI SDK | Mensajes de chat |
| LangChain | Estado de agentes |
| RAG | Metadatos de documentos |
| Machine Learning | Configuración de modelos |
| Automatización | Parámetros de ejecución |

### Caso práctico

Representar un mensaje para un modelo de lenguaje.

```python
mensaje = {
    "role": "user",
    "content": "¿Qué es Python?"
}
```

Este formato basado en pares clave-valor es común en APIs modernas de IA.

---

# Problemas reales en producción

## Problema 1

Acceder a una clave inexistente.

```python
usuario["correo"]
```

Resultado.

```text
KeyError
```

Si la clave puede ser opcional, suele ser preferible utilizar `get()`.

---

## Problema 2

Suponer que `keys()` devuelve una lista.

```python
claves = auto.keys()
```

`keys()` devuelve una vista dinámica (`dict_keys`), no una lista. Si se necesita una lista, debe convertirse explícitamente.

```python
claves = list(auto.keys())
```

---

## Problema 3

Utilizar claves duplicadas.

```python
datos = {
    "id": 1,
    "id": 2
}
```

Resultado.

```text
{'id': 2}
```

La última asignación reemplaza a la anterior.

---

## Problema 4

Modificar un diccionario mientras se recorre.

```python
for clave in auto:
    auto["nuevo"] = 1
```

Esto puede producir un error de ejecución porque el tamaño del diccionario cambia durante la iteración.

---

# Buenas prácticas

- Utiliza nombres descriptivos para las claves.
- Prefiere `get()` cuando una clave pueda no existir.
- Utiliza `items()` cuando necesites clave y valor simultáneamente.
- Emplea `update()` para realizar múltiples modificaciones de forma clara.
- Aprovecha los diccionarios anidados para representar relaciones jerárquicas.
- Evita modificar la estructura del diccionario mientras lo recorres.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "Los diccionarios son colecciones ordenadas"

### Corrección técnica

Es importante matizar esta afirmación. Desde Python **3.7**, los diccionarios **preservan el orden de inserción**, pero su propósito principal no es mantener un orden como una lista, sino ofrecer acceso eficiente mediante claves gracias a su implementación basada en tablas hash.

---

## Corrección 2. "`get()` y `[]` hacen exactamente lo mismo"

### Corrección técnica

No. Ambos recuperan un valor cuando la clave existe, pero difieren cuando la clave no está presente. `[]` genera un `KeyError`, mientras que `get()` devuelve `None` o un valor predeterminado si se proporciona como segundo argumento.

Ejemplo.

```python
print(auto.get("color", "No definido"))
```

Resultado.

```text
No definido
```

---

## Corrección 3. "`keys()` y `values()` devuelven listas"

### Corrección técnica

No. Devuelven objetos de tipo `dict_keys` y `dict_values`, que son vistas dinámicas sobre el contenido del diccionario. Estas vistas reflejan automáticamente cualquier modificación posterior del diccionario.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuándo utilizarías un diccionario en lugar de una lista?

### Qué evalúa

Capacidad para seleccionar la estructura de datos adecuada.

### Errores comunes

- Responder únicamente "porque tiene claves".

### Respuesta de alto impacto

> Utilizaría un diccionario cuando los datos tengan atributos identificados por nombre y necesite acceder a ellos mediante claves en lugar de posiciones. Esto hace que el código sea más expresivo y permite búsquedas rápidas sin depender del orden de los elementos.

---

## Pregunta 2

¿Cuál es la diferencia entre `get()` y acceder mediante corchetes?

### Qué evalúa

Comprensión del manejo de claves inexistentes.

### Errores comunes

- Pensar que ambos métodos siempre producen el mismo resultado.

### Respuesta de alto impacto

> Ambos recuperan el valor asociado a una clave existente, pero si la clave no está presente, `[]` lanza un `KeyError`, mientras que `get()` devuelve `None` o un valor por defecto. En aplicaciones donde las claves son opcionales, `get()` suele ser la opción más segura.

---

## Pregunta 3

¿Por qué los diccionarios ofrecen búsquedas eficientes por clave?

### Qué evalúa

Comprensión del funcionamiento interno de Python.

### Errores comunes

- Atribuirlo únicamente a una optimización general del lenguaje.

### Respuesta de alto impacto

> Porque los diccionarios están implementados mediante tablas hash. Python calcula el valor hash de la clave y lo utiliza para localizar rápidamente la posición donde está almacenado el valor asociado, evitando recorrer todos los elementos del diccionario en la mayoría de los casos.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `dict`.
- Python Documentation — Mapping Types.
- Python Documentation — Dictionary View Objects.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 468** — Preserving the Order of Keyword Arguments.
- **PEP 509** — Dictionary Versioning.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.