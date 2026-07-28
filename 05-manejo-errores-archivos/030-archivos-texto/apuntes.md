# Clase 30. Manejo de Archivos en Python (`open`, `with`, lectura y escritura)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo leer, escribir, crear y manipular archivos en Python utilizando `open()`, los distintos modos de apertura (`r`, `w`, `a`, `x`), el administrador de contexto `with`, el manejo de codificación mediante `encoding` y las buenas prácticas utilizadas en aplicaciones profesionales.

---

# Contenido del curso

Hasta ahora toda la información utilizada por nuestros programas existía únicamente mientras el programa estaba en ejecución.

Cuando el programa terminaba, los datos desaparecían.

Para conservar información entre ejecuciones es necesario utilizar **archivos**.

Python proporciona funciones integradas que permiten:

- leer archivos;
- escribir archivos;
- crear archivos;
- modificar archivos existentes.

El punto de entrada para todas estas operaciones es la función:

```python
open()
```

---

# ¿Qué es `open()`?

`open()` es una función incorporada de Python que abre un archivo y devuelve un **objeto archivo** (*file object*) sobre el que posteriormente pueden realizarse operaciones de lectura y escritura.

Su sintaxis básica es:

```python
open(nombre_archivo, modo)
```

Ejemplo.

```python
archivo = open("archivo.txt", "r")
```

---

# Funcionamiento interno

```text
Programa

↓

open()

↓

Sistema Operativo

↓

Abrir archivo

↓

Crear objeto archivo

↓

Devolver referencia
```

El objeto devuelto representa una conexión entre el programa y el archivo físico almacenado en el disco.

---

# Modos de apertura

El segundo argumento de `open()` indica cómo se utilizará el archivo.

| Modo | Descripción |
|------|-------------|
| `"r"` | Lectura |
| `"w"` | Escritura (sobrescribe el contenido) |
| `"a"` | Agregar contenido al final (*append*) |
| `"x"` | Crear un archivo nuevo |

---

# Modo lectura (`r`)

```python
archivo = open("archivo.txt", "r")
```

Este modo:

- permite leer;
- no modifica el contenido;
- produce un error si el archivo no existe.

---

# ¿Qué ocurre si el archivo no existe?

```python
archivo = open("datos.txt", "r")
```

Resultado.

```text
FileNotFoundError
```

Python no puede abrir un archivo inexistente en modo lectura.

---

# Manejo del error

```python
try:
    archivo = open("archivo.txt", "r")

    print(archivo.readline())

    archivo.close()

except FileNotFoundError:
    print("No se ha encontrado el archivo.")
```

Resultado.

```text
No se ha encontrado el archivo.
```

El programa continúa ejecutándose sin finalizar abruptamente.

---

# ¿Por qué cerrar un archivo?

Cuando un archivo permanece abierto, el sistema operativo mantiene recursos reservados.

Si olvidamos cerrarlo, pueden producirse problemas como:

- consumo innecesario de memoria;
- bloqueo del archivo;
- pérdida de datos pendientes de escritura.

Para cerrar un archivo se utiliza:

```python
archivo.close()
```

---

# El administrador de contexto `with`

La forma recomendada de trabajar con archivos consiste en utilizar:

```python
with
```

Ejemplo.

```python
with open(
    "archivo.txt",
    "r",
    encoding="utf-8"
) as archivo:

    print(archivo.readline())
```

---

# Funcionamiento interno

```text
Entrar en with

↓

Abrir archivo

↓

Ejecutar bloque

↓

Cerrar archivo automáticamente
```

No es necesario llamar a:

```python
close()
```

Python lo hace automáticamente al abandonar el bloque.

---

# ¿Por qué `with` es la opción recomendada?

Sin `with`.

```python
archivo = open(...)

...

archivo.close()
```

Si ocurre una excepción antes de `close()`, el archivo podría quedar abierto.

Con `with`.

```python
with open(...) as archivo:
```

El archivo siempre será cerrado, incluso si ocurre una excepción.

---

# Leer una línea

```python
with open(
    "archivo.txt",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.readline()
    )
```

`readline()` devuelve únicamente una línea.

---

# Leer varias líneas

```python
print(archivo.readline())

print(archivo.readline())
```

Cada llamada avanza el cursor hasta la siguiente línea.

---

# Funcionamiento interno

```text
Archivo

↓

Cursor

↓

readline()

↓

Mover cursor

↓

Siguiente línea
```

El archivo mantiene internamente la posición actual del cursor.

---

# Leer todo el archivo

```python
with open(
    "archivo.txt",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.read()
    )
```

Resultado.

```text
Todo el contenido del archivo...
```

`read()` devuelve el contenido completo desde la posición actual del cursor.

---

# ¿Por qué utilizar `encoding="utf-8"`?

Los archivos de texto contienen caracteres codificados.

Cuando existen letras como:

```text
á
é
í
ó
ú
ñ
```

pueden aparecer símbolos incorrectos si la codificación utilizada no coincide con la del archivo.

Por ello se recomienda especificar explícitamente:

```python
encoding="utf-8"
```

---

# Funcionamiento interno

```text
Archivo

↓

Bytes

↓

UTF-8

↓

Texto Unicode

↓

Python
```

UTF-8 es actualmente el estándar más utilizado para almacenar texto.

---

# Modo escritura (`w`)

```python
with open(
    "archivo.txt",
    "w",
    encoding="utf-8"
) as archivo:

    archivo.write("Hola mundo")
```

Resultado.

```text
Hola mundo
```

---

# ¿Qué hace realmente `"w"`?

Si el archivo existe.

```text
Contenido anterior

↓

Abrir con "w"

↓

Eliminar contenido

↓

Escribir nuevo contenido
```

Todo el contenido previo desaparece.

---

# Modo agregar (`a`)

```python
with open(
    "archivo.txt",
    "a",
    encoding="utf-8"
) as archivo:

    archivo.write("\n")
    archivo.write("Nueva línea")
```

Resultado.

```text
Contenido anterior
Nueva línea
```

El contenido existente se conserva.

---

# El carácter `\n`

```python
archivo.write("\n")
```

Representa un salto de línea.

Sin él.

```text
HolaMundo
```

Con él.

```text
Hola
Mundo
```

---

# Funcionamiento interno

```text
Cursor

↓

Final del archivo

↓

write()

↓

Agregar texto
```

El modo `a` siempre escribe al final del archivo.

---

# Modo creación (`x`)

```python
open("archivo.txt", "x")
```

Este modo crea un archivo nuevo.

Si el archivo ya existe.

Resultado.

```text
FileExistsError
```

---

# Crear un archivo automáticamente

```python
try:

    with open(
        "archivo.txt",
        "r",
        encoding="utf-8"
    ) as archivo:

        print(archivo.read())

except FileNotFoundError:

    print("Archivo inexistente.")

    open("archivo.txt", "x")
```

Si el archivo no existe, Python lo crea.

---

# Escribir después de crear

```python
with open(
    "archivo.txt",
    "a",
    encoding="utf-8"
) as archivo:

    archivo.write(
        "Hola mundo"
    )
```

---

# Leer nuevamente

```python
with open(
    "archivo.txt",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.read()
    )
```

---

# Flujo completo

```text
Intentar leer

↓

¿Existe?
```

```text
Sí

↓

Leer
```

```text
No

↓

Crear

↓

Escribir

↓

Leer
```

---

# ¿Dónde busca Python los archivos?

Por defecto, Python busca los archivos utilizando el **directorio de trabajo actual** (*Current Working Directory*).

Ejemplo.

```text
proyecto/

│

├── main.py

└── archivo.txt
```

Si ambos archivos están en la misma carpeta.

```python
open("archivo.txt")
```

funciona correctamente.

---

# Archivos en subcarpetas

```text
proyecto/

│

├── main.py

└── datos/

    └── usuarios.txt
```

La ruta debe indicarse.

```python
open(
    "datos/usuarios.txt"
)
```

---

# AI Engineering

El manejo de archivos aparece constantemente en aplicaciones de IA.

| Caso | Uso |
|------|-----|
| RAG | Leer documentos PDF, TXT y Markdown |
| Fine-Tuning | Cargar conjuntos de entrenamiento |
| Embeddings | Leer documentos antes de vectorizarlos |
| Automatización | Generar reportes |
| APIs | Guardar registros (*logs*) |
| Machine Learning | Leer archivos CSV y JSON |

### Caso práctico

Leer un archivo antes de generar embeddings.

```python
with open(
    "manual.txt",
    "r",
    encoding="utf-8"
) as archivo:

    texto = archivo.read()
```

Posteriormente.

```text
texto

↓

Embeddings

↓

Base vectorial
```

Este patrón constituye el primer paso de muchos sistemas RAG modernos.

---

# Problemas reales en producción

## Problema 1

Olvidar cerrar el archivo.

```python
archivo = open(...)
```

Si nunca se ejecuta:

```python
archivo.close()
```

el sistema operativo mantiene el recurso abierto.

La solución recomendada es utilizar siempre:

```python
with open(...)
```

---

## Problema 2

Abrir un archivo con `"w"` creyendo que agregará información.

```python
open("datos.txt", "w")
```

Todo el contenido anterior será eliminado.

Si se desea conservar la información existente debe utilizarse:

```python
"a"
```

---

## Problema 3

No especificar la codificación.

```python
open("archivo.txt")
```

En algunos sistemas operativos pueden aparecer errores relacionados con caracteres especiales.

Es recomendable indicar explícitamente:

```python
encoding="utf-8"
```

---

## Problema 4

Leer archivos muy grandes utilizando `read()`.

```python
texto = archivo.read()
```

Esto carga todo el archivo en memoria.

Cuando el archivo tiene varios gigabytes, el consumo de memoria puede ser muy elevado.

En estos casos suele preferirse leer línea por línea mediante:

```python
readline()
```

o iterar directamente sobre el archivo.

---

# Buenas prácticas

- Utiliza siempre `with open(...)` en lugar de `open()` seguido de `close()`.
- Especifica `encoding="utf-8"` para trabajar con texto.
- Utiliza `"r"` para leer, `"w"` para sobrescribir, `"a"` para agregar y `"x"` para crear archivos nuevos.
- Captura excepciones específicas como `FileNotFoundError` cuando el archivo pueda no existir.
- Evita utilizar `read()` en archivos muy grandes si no es necesario cargar todo el contenido en memoria.
- Organiza las rutas de los archivos de forma explícita cuando trabajes con subdirectorios.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`open()` abre directamente el archivo"

### Corrección técnica

`open()` no devuelve el contenido del archivo.

Devuelve un **objeto archivo** (*file object*) que permite realizar operaciones posteriores como leer, escribir o mover el cursor.

---

## Corrección 2. "`with` solo sirve para archivos"

### Corrección técnica

No.

`with` es un **administrador de contexto** (*context manager*) que puede utilizarse con muchos otros recursos:

- archivos;
- conexiones de bases de datos;
- sockets;
- bloqueos (*locks*);
- sesiones HTTP;
- conexiones SSH.

Su función consiste en garantizar la correcta adquisición y liberación de recursos.

---

## Corrección 3. "`readline()` lee la siguiente línea"

### Corrección técnica

Más precisamente, `readline()` lee desde la posición actual del cursor hasta encontrar un salto de línea (`\n`) o el final del archivo. Cada llamada avanza el cursor, por lo que las siguientes lecturas continúan desde esa nueva posición.

---

## Corrección 4. "`x` crea un archivo vacío"

### Corrección técnica

El modo `"x"` crea un archivo únicamente si no existe previamente. Si el archivo ya está presente, Python genera una excepción `FileExistsError`, evitando sobrescribir accidentalmente información existente.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué se recomienda utilizar `with open()` en lugar de `open()` y `close()`?

### Qué evalúa

Conocimiento del manejo seguro de recursos.

### Errores comunes

- Responder únicamente que "es más corto".

### Respuesta de alto impacto

> `with` implementa el protocolo de administradores de contexto y garantiza que el archivo se cierre automáticamente al finalizar el bloque, incluso si ocurre una excepción. Esto evita fugas de recursos y hace que el código sea más seguro y mantenible.

---

## Pregunta 2

¿Cuál es la diferencia entre los modos `"w"` y `"a"`?

### Qué evalúa

Comprensión de la escritura en archivos.

### Errores comunes

- Pensar que ambos agregan contenido.

### Respuesta de alto impacto

> El modo `"w"` sobrescribe completamente el contenido existente o crea el archivo si no existe. El modo `"a"` conserva el contenido actual y escribe únicamente al final del archivo, por lo que es la opción adecuada para registros o historiales.

---

## Pregunta 3

¿Por qué es importante especificar `encoding="utf-8"`?

### Qué evalúa

Conocimiento sobre codificación de texto.

### Errores comunes

- Pensar que UTF-8 solo afecta a caracteres en español.

### Respuesta de alto impacto

> UTF-8 define cómo se representan los caracteres en bytes. Es el estándar de facto para el intercambio de texto y garantiza que caracteres especiales, acentos y símbolos Unicode se interpreten correctamente en distintos sistemas operativos y aplicaciones.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `open()`.
- Python Documentation — File Objects.
- Python Documentation — Context Managers.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 343** — The `with` Statement.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.