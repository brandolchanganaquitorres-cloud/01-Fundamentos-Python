# Clase 11. Manejo de Strings en Python

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo crear, manipular y transformar cadenas de texto en Python utilizando comillas, funciones y métodos esenciales como `len()`, `in`, `not in`, `upper()`, `lower()` y `strip()`, entendiendo además su aplicación en proyectos reales de software e Inteligencia Artificial.

---

# Contenido del curso

Los **strings** (`str`) representan secuencias de caracteres y constituyen uno de los tipos de datos más utilizados en Python.

Prácticamente cualquier aplicación informática trabaja con texto:

- nombres de usuarios;
- contraseñas;
- correos electrónicos;
- mensajes;
- archivos;
- URLs;
- respuestas de APIs;
- prompts para modelos de IA.

Dominar su manipulación es una habilidad indispensable para cualquier desarrollador.

---

# Uso de comillas en Python

Python permite crear cadenas utilizando:

- comillas simples `' '`;
- comillas dobles `" "`;
- comillas triples `""" """` o `''' '''`.

---

## Comillas simples

```python
nombre = 'Brandol'
```

---

## Comillas dobles

```python
curso = "Fundamentos de Python"
```

Ambas producen exactamente el mismo resultado.

La diferencia radica únicamente en facilitar la escritura de determinados textos.

---

# Cómo escribir comillas dentro de un string

Si un texto contiene comillas dobles, conviene utilizar comillas simples para delimitar la cadena.

```python
mensaje = 'Ella dijo: "Hola"'
```

Si el texto contiene un apóstrofe o comillas simples, utiliza comillas dobles.

```python
persona = "I'm Sergi"
```

De esta manera Python interpreta correctamente dónde inicia y termina la cadena.

---

# Error común

El siguiente código genera un error de sintaxis.

```python
mensaje = "Ella dijo "Hola""
```

Resultado:

```text
SyntaxError
```

Python interpreta que la cadena termina antes de tiempo.

---

# Expansión técnica

## ¿Qué ocurre internamente?

Cuando Python encuentra una comilla de apertura, continúa leyendo caracteres hasta localizar la comilla de cierre correspondiente.

```text
"

↓

Inicio del string

↓

Caracteres

↓

"

↓

Fin del string
```

Si aparece una comilla idéntica antes del final esperado, el intérprete considera que la cadena terminó y el resto del texto se convierte en una instrucción inválida.

---

# Comillas triples

Las comillas triples permiten crear cadenas multilínea.

```python
texto = """
Primera línea
Segunda línea
Tercera línea
"""
```

Al imprimir:

```python
print(texto)
```

Resultado:

```text
Primera línea
Segunda línea
Tercera línea
```

Los saltos de línea se conservan automáticamente.

---

# ¿Cuándo utilizar comillas triples?

Son especialmente útiles para:

- mensajes extensos;
- plantillas de correo;
- documentación;
- prompts para modelos de IA;
- consultas SQL largas;
- texto HTML.

Ejemplo:

```python
prompt = """
Eres un asistente experto.

Analiza el siguiente documento.

Devuelve la respuesta en formato JSON.
"""
```

---

# Expansión técnica

En proyectos con LLMs (GPT, Claude, Gemini, etc.), los **prompts** suelen escribirse mediante comillas triples porque permiten mantener una estructura clara y legible.

```python
prompt = """
Resume el documento.

Extrae entidades.

Devuelve Markdown.
"""
```

Este patrón aparece constantemente en aplicaciones desarrolladas con LangChain, LangGraph y OpenAI SDK.

---

# Función `len()`

La función integrada `len()` devuelve el número total de caracteres de una cadena.

```python
palabra = "murciélago"

print(len(palabra))
```

Resultado:

```python
10
```

También cuenta:

- espacios;
- signos;
- números;
- caracteres especiales.

```python
texto = "Hola Mundo"

print(len(texto))
```

Resultado:

```python
10
```

El espacio también cuenta como un carácter.

---

# Expansión técnica

`len()` no modifica la cadena.

Simplemente devuelve un número entero.

```python
cantidad = len(texto)
```

Este valor puede utilizarse posteriormente para:

- validar formularios;
- limitar longitud de entradas;
- recorrer caracteres;
- controlar tamaños máximos.

---

# Producción

Ejemplo de validación de contraseña.

```python
password = input("Contraseña: ")

if len(password) < 8:
    print("Contraseña demasiado corta")
```

Este tipo de validación aparece prácticamente en cualquier sistema de autenticación.

---

# Operadores `in` y `not in`

Python permite verificar si una cadena contiene otra cadena.

```python
texto = "Este curso es de Python"

print("Python" in texto)
```

Resultado:

```python
True
```

---

También puede comprobarse que una palabra no exista.

```python
print("Java" not in texto)
```

Resultado:

```python
True
```

---

# ¿Qué devuelve `in`?

Siempre devuelve un valor booleano.

```python
True
```

o

```python
False
```

---

# Expansión técnica

Internamente Python busca la secuencia de caracteres indicada dentro del texto.

```text
Texto

↓

Buscar subcadena

↓

Encontrada

↓

True
```

o

```text
No encontrada

↓

False
```

---

# Case Sensitive

Python distingue entre mayúsculas y minúsculas.

```python
texto = "Python"

print("Python" in texto)
```

Resultado:

```python
True
```

Mientras que:

```python
print("python" in texto)
```

Resultado:

```python
False
```

Aunque visualmente parecen similares, para Python son cadenas distintas.

---

# Problema real en producción

Un usuario intenta iniciar sesión.

```text
Correo:

Brandol@correo.com
```

La base de datos almacena:

```text
brandol@correo.com
```

Una comparación directa podría fallar debido a la diferencia entre mayúsculas y minúsculas.

Por ello es habitual normalizar el texto antes de compararlo.

```python
correo = correo.lower()
```

---

# Método `upper()`

Convierte todos los caracteres a mayúsculas.

```python
texto = "Este curso es de fundamentos de Python"

mayuscula = texto.upper()

print(mayuscula)
```

Resultado:

```text
ESTE CURSO ES DE FUNDAMENTOS DE PYTHON
```

---

# Método `lower()`

Convierte todos los caracteres a minúsculas.

```python
minuscula = texto.lower()

print(minuscula)
```

Resultado:

```text
este curso es de fundamentos de python
```

---

# Expansión técnica

Ni `upper()` ni `lower()` modifican el string original.

Crean una nueva cadena.

```python
texto = "Python"

nuevo = texto.upper()
```

Después de ejecutar este código:

```python
texto
```

continúa siendo:

```text
Python
```

Mientras que:

```python
nuevo
```

contiene:

```text
PYTHON
```

Esto ocurre porque los **strings son inmutables**.

---

# Funcionamiento interno

```text
texto

↓

"Python"

↓

upper()

↓

Nuevo objeto

↓

"PYTHON"
```

El objeto original permanece intacto.

---

# Problema común

```python
texto = "Python"

texto.upper()

print(texto)
```

Resultado:

```text
Python
```

Muchos principiantes esperan obtener:

```text
PYTHON
```

Pero olvidan guardar el resultado.

Correcto:

```python
texto = texto.upper()
```

---

# Método `strip()`

Elimina espacios al inicio y al final de una cadena.

```python
texto = "   este es el texto   "

limpio = texto.strip()

print(limpio)
```

Resultado:

```text
este es el texto
```

Los espacios internos permanecen intactos.

---

# Ejemplo

Cadena original.

```text
"   Hola Mundo   "
```

Después de aplicar `strip()`.

```text
"Hola Mundo"
```

---

# Producción

Los espacios invisibles generan numerosos errores.

Ejemplo.

```python
usuario = "admin "

usuario == "admin"
```

Resultado:

```python
False
```

Aplicando:

```python
usuario = usuario.strip()
```

La comparación funciona correctamente.

---

# Aplicaciones reales de `strip()`

Es habitual utilizarlo antes de almacenar información como:

- nombres;
- usuarios;
- correos electrónicos;
- teléfonos;
- códigos promocionales;
- tokens.

Esto evita errores difíciles de detectar.

---

# AI Engineering

El procesamiento de texto constituye la base de prácticamente todos los sistemas de IA.

Estos métodos aparecen constantemente durante la preparación de datos.

| Método | Uso en IA |
|---------|-----------|
| `len()` | Validar longitud de prompts o documentos |
| `in` | Buscar palabras clave |
| `upper()` | Normalización de datos específicos |
| `lower()` | Comparaciones sin distinguir mayúsculas |
| `strip()` | Limpieza de texto antes del procesamiento |

### Caso práctico

Antes de enviar un prompt a un LLM suele eliminarse el espacio sobrante.

```python
prompt = prompt.strip()
```

Después puede verificarse su longitud.

```python
if len(prompt) > 4000:
    print("Prompt demasiado largo")
```

Y comprobar si contiene determinadas instrucciones.

```python
if "JSON" in prompt:
    print("Debe responder en formato JSON")
```

---

# Problemas reales en producción

## Problema 1

Olvidar guardar el resultado de `upper()`.

```python
texto.upper()
```

No modifica la variable.

---

## Problema 2

Comparar cadenas con diferencias de mayúsculas.

```python
"Python"

!=

"python"
```

---

## Problema 3

No eliminar espacios antes de autenticar usuarios.

```text
"admin "

≠

"admin"
```

---

## Problema 4

Suponer que `len()` cuenta únicamente letras.

También contabiliza:

- espacios;
- signos;
- emojis;
- números.

---

# Buenas prácticas

- Utiliza comillas triples para textos multilínea.
- Conserva el resultado de `upper()` y `lower()` asignándolo a una variable.
- Normaliza texto con `lower()` antes de realizar comparaciones cuando el dominio lo permita.
- Aplica `strip()` sobre datos introducidos por el usuario.
- Usa `len()` para validar restricciones de longitud antes de procesar la información.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`upper()` modifica la cadena"

### Corrección técnica

Los strings en Python son **inmutables**. Métodos como `upper()`, `lower()` y `strip()` devuelven una nueva cadena y no alteran el objeto original.

---

## Corrección 2. "`strip()` elimina todos los espacios"

### Corrección técnica

`strip()` únicamente elimina los caracteres del inicio y del final de la cadena. Los espacios entre palabras permanecen sin cambios.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué `upper()` y `lower()` no modifican la variable original?

### Qué evalúa

Conocimiento sobre la inmutabilidad de los strings.

### Errores comunes

- Pensar que el método cambia el objeto existente.

### Respuesta de alto impacto

> En Python, los strings son objetos inmutables. Métodos como `upper()` o `lower()` crean y devuelven una nueva cadena; por ello, si se desea conservar el cambio, es necesario asignar el resultado a una variable.

---

## Pregunta 2

¿En qué situaciones utilizarías `strip()`?

### Qué evalúa

Experiencia en validación y saneamiento de datos.

### Errores comunes

- Limitar su uso a ejemplos académicos.

### Respuesta de alto impacto

> Lo utilizaría antes de validar credenciales, procesar formularios, importar archivos CSV o consumir APIs, ya que elimina espacios invisibles que pueden provocar errores de autenticación o comparaciones incorrectas.

---

## Pregunta 3

¿Por qué una búsqueda con `in` puede devolver `False` aunque la palabra parezca existir?

### Qué evalúa

Comprensión del comportamiento *case sensitive* de Python.

### Errores comunes

- Ignorar las diferencias entre mayúsculas y minúsculas.

### Respuesta de alto impacto

> Porque las comparaciones de cadenas en Python distinguen entre mayúsculas y minúsculas. Si el dominio del problema no requiere esa distinción, primero normalizaría ambas cadenas utilizando `lower()` o `upper()` antes de compararlas.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Text Sequence Type (`str`).
- Python Documentation — Built-in Function `len()`.
- Python Documentation — String Methods.

## PEPs

- PEP 8 — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.