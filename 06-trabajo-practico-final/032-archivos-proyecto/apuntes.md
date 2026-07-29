# Clase 32. Proyecto Integrador: Persistencia de Datos con Archivos (Máquina de Café)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Implementar persistencia de datos en una aplicación Python utilizando archivos de texto, integrar lectura y escritura de archivos con módulos independientes, utilizar constantes, validar entradas mediante diccionarios, recorrer información con `enumerate()` y consolidar una arquitectura modular similar a la utilizada en proyectos reales.

---

# Contenido del curso

En esta segunda parte del proyecto de la **Máquina de Café** se añade una característica fundamental presente en prácticamente cualquier aplicación profesional:

> **Persistencia de datos.**

Hasta ahora los pedidos únicamente existían mientras el programa estaba en ejecución.

Ahora cada pedido será almacenado en un archivo para que permanezca disponible incluso después de cerrar la aplicación.

Esto introduce uno de los conceptos más importantes de cualquier software:

```text
Programa

↓

Guardar información

↓

Cerrar programa

↓

Abrir nuevamente

↓

Recuperar información
```

---

# Arquitectura del proyecto

La aplicación continúa creciendo de forma modular.

```text
maquina_cafe/

│

├── main.py

├── menu.py

├── pedidos.py

└── historial.py
```

Cada módulo mantiene una única responsabilidad.

| Archivo | Responsabilidad |
|----------|-----------------|
| `main.py` | Coordinar el flujo principal |
| `menu.py` | Mostrar el menú |
| `pedidos.py` | Registrar pedidos |
| `historial.py` | Mostrar pedidos almacenados |

Esta organización sigue el principio **Single Responsibility Principle (SRP)**, uno de los pilares del diseño orientado a objetos y de la arquitectura de software moderna.

---

# Utilizar un diccionario para validar opciones

Los cafés disponibles se almacenan en un diccionario.

```python
cafes = {
    "1": "Expreso",
    "2": "Capuchino",
    "3": "Latte",
    "4": "Americano"
}
```

El usuario escribe una opción.

```python
opcion = input("Seleccione un café: ")
```

Posteriormente.

```python
if opcion in cafes:
```

Python verifica si la clave existe dentro del diccionario.

---

# Funcionamiento interno

```text
Usuario

↓

"2"

↓

Diccionario

↓

¿Existe la clave?

↓

Sí

↓

"Capuchino"
```

---

# Obtener el café seleccionado

Una vez validada la clave.

```python
cafe_elegido = cafes[opcion]
```

Python recupera el valor asociado.

```text
"2"

↓

Diccionario

↓

Capuchino
```

No es necesario recorrer todas las opciones mediante múltiples `if`.

---

# ¿Por qué utilizar un diccionario?

Sin diccionario.

```python
if opcion == "1":
    ...

elif opcion == "2":
    ...

elif opcion == "3":
    ...

elif opcion == "4":
    ...
```

Con diccionario.

```python
cafe = cafes[opcion]
```

Además de reducir código, el acceso promedio tiene complejidad **O(1)** gracias al uso de tablas hash.

---

# Constantes

El nombre del archivo se almacena en una constante.

```python
ARCHIVO_PEDIDOS = "pedidos.txt"
```

---

# ¿Por qué utilizar constantes?

Sin constante.

```python
open("pedidos.txt")

...

open("pedidos.txt")

...

open("pedidos.txt")
```

Si el nombre cambia, será necesario modificar todas las referencias.

Con constante.

```python
ARCHIVO_PEDIDOS
```

Solo existe un único punto de modificación.

---

# Convención de nombres

En Python las constantes suelen escribirse completamente en mayúsculas.

```python
ARCHIVO_PEDIDOS

MAX_INTENTOS

PI
```

Esta es una **convención** establecida por **PEP 8**.

Python no impide modificar una constante, pero escribirla en mayúsculas comunica a otros desarrolladores que su valor no debería cambiar.

---

# Guardar pedidos

Cada pedido se almacena utilizando.

```python
with open(
    ARCHIVO_PEDIDOS,
    "a",
    encoding="utf-8"
) as archivo:

    archivo.write(cafe_elegido + "\n")
```

---

# ¿Por qué utilizar el modo `"a"`?

Recordemos los principales modos.

| Modo | Comportamiento |
|------|----------------|
| `"r"` | Leer |
| `"w"` | Sobrescribir |
| `"a"` | Agregar al final |
| `"x"` | Crear archivo nuevo |

En este proyecto necesitamos conservar todos los pedidos.

Por ello se utiliza:

```python
"a"
```

---

# Funcionamiento interno

```text
Archivo

↓

Cursor

↓

Final del archivo

↓

write()

↓

Nuevo pedido
```

Cada nuevo pedido se incorpora al final del archivo.

---

# El carácter `\n`

Cada pedido se escribe así.

```python
archivo.write(
    cafe_elegido + "\n"
)
```

El carácter.

```text
\n
```

representa un salto de línea.

Resultado.

```text
Expreso
Latte
Americano
```

Sin el salto.

```text
ExpresoLatteAmericano
```

---

# Importar la función de pedidos

En `main.py`.

```python
from pedidos import pedir_cafe
```

Posteriormente.

```python
if opcion == "1":
    pedir_cafe()
```

El archivo principal únicamente coordina la ejecución.

Toda la lógica permanece encapsulada dentro de `pedidos.py`.

---

# Leer el historial

Se crea un nuevo módulo.

```text
historial.py
```

Su responsabilidad consiste únicamente en mostrar los pedidos almacenados.

---

# Abrir el archivo

```python
with open(
    ARCHIVO_PEDIDOS,
    "r",
    encoding="utf-8"
) as archivo:

    pedidos = archivo.readlines()
```

---

# ¿Qué devuelve `readlines()`?

A diferencia de:

```python
read()
```

que devuelve una única cadena,

```python
readlines()
```

devuelve una lista.

Ejemplo.

```python
[
    "Expreso\n",
    "Latte\n",
    "Americano\n"
]
```

Cada elemento corresponde a una línea del archivo.

---

# Funcionamiento interno

```text
Archivo

↓

Leer línea

↓

Guardar en lista

↓

Leer siguiente línea

↓

...

↓

Lista completa
```

---

# Manejar archivos inexistentes

Puede ocurrir que el usuario consulte el historial antes de realizar el primer pedido.

En ese caso.

```python
open(..., "r")
```

genera.

```text
FileNotFoundError
```

Por ello se utiliza.

```python
try:
    ...

except FileNotFoundError:
    ...
```

---

# Flujo del historial

```text
Intentar abrir archivo

↓

¿Existe?
```

```text
Sí

↓

Leer pedidos
```

```text
No

↓

Mostrar mensaje
```

Esto evita que la aplicación termine abruptamente.

---

# Mostrar el historial

Una vez obtenida la lista.

```python
for i, pedido in enumerate(
    pedidos,
    1
):
    ...
```

---

# ¿Qué hace `enumerate()`?

`enumerate()` genera dos valores en cada iteración.

- índice;
- elemento.

Ejemplo.

```python
pedidos = [
    "Expreso",
    "Latte",
    "Americano"
]
```

Resultado.

```text
1  Expreso

2  Latte

3  Americano
```

---

# Funcionamiento interno

```text
Lista

↓

enumerate()

↓

(1, "Expreso")

↓

(2, "Latte")

↓

(3, "Americano")
```

El segundo argumento.

```python
enumerate(
    pedidos,
    1
)
```

indica que la numeración debe comenzar en:

```text
1
```

En lugar del valor predeterminado:

```text
0
```

---

# El método `strip()`

Cada línea leída contiene el salto de línea.

```text
"Expreso\n"
```

Para eliminarlo.

```python
pedido.strip()
```

Resultado.

```text
Expreso
```

---

# ¿Qué hace realmente `strip()`?

Elimina los caracteres en blanco situados al principio y al final de la cadena.

Por ejemplo.

Antes.

```text
"   Latte\n"
```

Después.

```text
"Latte"
```

---

# Flujo completo del historial

```text
Abrir archivo

↓

readlines()

↓

Lista

↓

enumerate()

↓

strip()

↓

Mostrar pedidos
```

---

# Archivo vacío

También puede ocurrir que el archivo exista, pero no contenga información.

En ese caso.

```python
if pedidos:
```

resulta falso.

El programa informa.

```text
Aún no hay pedidos.
```

Con ello se cubren tres escenarios.

| Situación | Resultado |
|-----------|-----------|
| Archivo inexistente | `FileNotFoundError` |
| Archivo vacío | Mensaje indicando que no hay pedidos |
| Archivo con datos | Mostrar historial |

---

# Arquitectura final del proyecto

```text
Usuario

↓

main.py

↓

pedir_cafe()

↓

pedidos.py

↓

pedidos.txt

↓

historial.py

↓

Mostrar historial
```

Este patrón representa una arquitectura por capas muy utilizada en aplicaciones empresariales.

---

# AI Engineering

Aunque el proyecto utiliza un archivo de texto, el patrón arquitectónico es el mismo empleado por aplicaciones modernas de IA.

```text
Usuario

↓

Aplicación

↓

Modelo

↓

Persistencia
```

La diferencia es únicamente el medio de almacenamiento.

| Proyecto del curso | Proyecto profesional |
|--------------------|----------------------|
| `pedidos.txt` | Base de datos PostgreSQL |
| Archivo TXT | MongoDB |
| Archivo TXT | Redis |
| Archivo TXT | Vector Database |
| Archivo TXT | Amazon S3 / Azure Blob Storage |

La lógica de lectura y escritura permanece prácticamente igual.

---

## Caso práctico

Un chatbot podría almacenar el historial de conversaciones utilizando el mismo patrón.

```python
with open(
    "historial_chat.txt",
    "a",
    encoding="utf-8"
) as archivo:

    archivo.write(
        mensaje + "\n"
    )
```

Posteriormente.

```python
with open(
    "historial_chat.txt",
    "r",
    encoding="utf-8"
) as archivo:

    conversaciones = archivo.readlines()
```

Este principio constituye la base de numerosos sistemas de memoria para asistentes conversacionales.

---

# Problemas reales en producción

## Problema 1

Utilizar `"w"` cuando se pretende conservar información.

```python
open(
    "pedidos.txt",
    "w"
)
```

Cada nueva ejecución eliminará completamente el historial.

---

## Problema 2

No manejar `FileNotFoundError`.

```python
open(
    "pedidos.txt",
    "r"
)
```

Si el archivo aún no existe, la aplicación finalizará con una excepción.

---

## Problema 3

No utilizar `strip()`.

```python
print(pedido)
```

La salida contendrá líneas en blanco adicionales debido al carácter `\n`.

---

## Problema 4

Duplicar el nombre del archivo en varios módulos.

```python
open("pedidos.txt")

...

open("pedidos.txt")
```

Si el nombre cambia, será necesario modificar múltiples archivos.

Una constante compartida reduce este riesgo.

---

## Problema 5

Guardar datos estructurados en texto plano cuando el proyecto crece.

Aunque un archivo `.txt` es suficiente para proyectos educativos, en aplicaciones reales suele migrarse a formatos como JSON, SQLite o bases de datos relacionales cuando aumentan el volumen de datos y las necesidades de consulta.

---

# Buenas prácticas

- Centraliza rutas y nombres de archivos en constantes.
- Utiliza siempre `with open()` para garantizar el cierre automático del archivo.
- Especifica `encoding="utf-8"` al trabajar con texto.
- Utiliza `"a"` cuando necesites conservar el contenido existente.
- Captura `FileNotFoundError` cuando el archivo pueda no existir.
- Usa `enumerate()` para mostrar listas numeradas sin gestionar índices manualmente.
- Aplica `strip()` antes de mostrar líneas leídas desde un archivo para eliminar caracteres residuales.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`if opcion in cafes` busca en todo el diccionario"

### Corrección técnica

La expresión:

```python
if opcion in cafes:
```

verifica únicamente si `opcion` existe como **clave** del diccionario. Es equivalente a:

```python
if opcion in cafes.keys():
```

pero más concisa y eficiente. No comprueba los valores asociados.

---

## Corrección 2. "`enumerate()` devuelve el índice y el contenido"

### Corrección técnica

Más precisamente, `enumerate()` devuelve un iterador de tuplas con la forma:

```python
(indice, elemento)
```

Estas tuplas se desempaquetan automáticamente en el bucle:

```python
for indice, elemento in enumerate(...):
```

---

## Corrección 3. "`strip()` elimina el salto de línea"

### Corrección técnica

`strip()` elimina **todos los caracteres de espacio en blanco** al inicio y al final de la cadena, incluidos:

- espacios;
- tabulaciones (`\t`);
- retornos de carro (`\r`);
- saltos de línea (`\n`).

No elimina espacios situados en el interior del texto.

---

## Corrección 4. "Las constantes no pueden modificarse"

### Corrección técnica

Python no posee constantes verdaderas a nivel del lenguaje. Escribir un nombre en mayúsculas es una **convención** que indica que el valor no debería cambiar. Técnicamente sigue siendo una variable y puede reasignarse.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué utilizar un diccionario para representar un menú es mejor que una cadena de `if` y `elif`?

### Qué evalúa

Selección adecuada de estructuras de datos.

### Errores comunes

- Responder únicamente que "es más corto".

### Respuesta de alto impacto

> Un diccionario modela directamente la relación entre una opción y su resultado mediante pares clave-valor. Esto reduce código repetitivo, facilita añadir nuevas opciones y permite búsquedas promedio de complejidad O(1) gracias a la implementación basada en tablas hash.

---

## Pregunta 2

¿Cuál es la diferencia entre `read()`, `readline()` y `readlines()`?

### Qué evalúa

Conocimiento del manejo de archivos.

### Errores comunes

- Confundir el tipo de dato devuelto por cada método.

### Respuesta de alto impacto

> `read()` devuelve una única cadena con todo el contenido restante del archivo. `readline()` devuelve solo la siguiente línea y avanza el cursor. `readlines()` devuelve una lista donde cada elemento corresponde a una línea del archivo, incluyendo el salto de línea original.

---

## Pregunta 3

¿Por qué es recomendable almacenar rutas de archivos en constantes?

### Qué evalúa

Buenas prácticas de mantenimiento y configuración.

### Errores comunes

- Pensar que solo mejora la estética del código.

### Respuesta de alto impacto

> Centralizar las rutas en constantes evita duplicación, reduce errores durante cambios futuros y facilita la configuración del sistema. Si el nombre o la ubicación del archivo cambia, basta con modificar una única referencia en lugar de buscar todas las apariciones dispersas por el proyecto.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — File Objects.
- Python Documentation — `enumerate()`.
- Python Documentation — String Methods (`strip()`).
- Python Documentation — Built-in Functions.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 20** — The Zen of Python.
- **PEP 343** — The `with` Statement.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.
- *Architecture Patterns with Python* — Harry Percival y Bob Gregory.