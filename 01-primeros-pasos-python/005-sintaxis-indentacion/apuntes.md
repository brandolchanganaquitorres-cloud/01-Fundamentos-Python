# Clase 5 — Sintaxis e Indentación en Python con Visual Studio Code

## Objetivos de aprendizaje

Al finalizar esta clase serás capaz de:

- Configurar un entorno de desarrollo para Python en Visual Studio Code mediante perfiles.
- Comprender qué es la sintaxis de Python y por qué es fundamental.
- Entender el papel de la indentación como parte de la sintaxis del lenguaje.
- Crear y ejecutar programas Python desde Visual Studio Code.
- Interpretar y corregir errores relacionados con la indentación.
- Aplicar buenas prácticas de estilo utilizadas en equipos profesionales.

---

# Introducción

Una vez instalado Python, el siguiente paso consiste en preparar un entorno de desarrollo que facilite la escritura, ejecución y depuración del código.

Visual Studio Code permite crear perfiles específicos para distintos lenguajes de programación. En este curso se configura un perfil dedicado a Python con las extensiones necesarias para desarrollar aplicaciones de forma más cómoda.

Además, esta clase introduce dos conceptos fundamentales del lenguaje:

- **Sintaxis**.
- **Indentación**.

A diferencia de muchos lenguajes, la indentación en Python **no es únicamente una cuestión estética**, sino que forma parte de la sintaxis del lenguaje y determina la estructura lógica del programa.

---

# Configuración de Visual Studio Code

## ¿Por qué utilizar un perfil?

Los perfiles permiten mantener configuraciones independientes para distintos tipos de proyectos.

Por ejemplo:

- Python
- JavaScript
- Java
- C#
- DevOps
- Data Science

Cada perfil puede tener:

- extensiones;
- configuraciones;
- temas;
- atajos;
- preferencias independientes.

Esto evita instalar herramientas innecesarias para otros lenguajes.

---

## Crear un perfil de Python

Pasos:

1. Abrir la configuración de Visual Studio Code.
2. Buscar:

```text
Profiles
```

3. Seleccionar:

```text
New Profile
```

4. Asignar el nombre:

```text
Python
```

5. Utilizar la opción:

```text
Copy From
```

6. Seleccionar el perfil sugerido para Python.
7. Pulsar **Create**.

Cuando el perfil esté activo aparecerá el icono correspondiente.

---

# Extensiones utilizadas

El curso instala tres extensiones principales.

## Python

Proporciona soporte oficial para el lenguaje.

Funciones principales:

- ejecución de programas;
- depuración;
- detección del intérprete;
- integración con entornos virtuales.

---

## Pylance

Motor de análisis estático desarrollado por Microsoft.

Permite:

- autocompletado inteligente;
- detección de errores antes de ejecutar;
- navegación por el código;
- ayuda con tipos de datos.

Pylance mejora considerablemente la productividad y es la opción recomendada para desarrollo profesional.

---

## Jupyter

Permite trabajar con notebooks (`.ipynb`).

Aunque en esta etapa del curso apenas se instala, posteriormente será una herramienta fundamental para:

- Ciencia de Datos.
- Machine Learning.
- Deep Learning.
- IA Generativa.
- Exploración de datos.

---

# Crear un archivo Python

Crear una carpeta para la práctica.

Ejemplo:

```text
Sintaxis-indentacion
```

Dentro de ella crear el archivo:

```text
sintaxis.py
```

La extensión `.py` indica a Visual Studio Code que el archivo contiene código Python.

Si el archivo no posee dicha extensión, el editor no activará el soporte específico del lenguaje.

---

# Ejecutar un programa

Una vez abierto el archivo aparecerá el botón:

```text
Run Python File
```

Este botón:

- ejecuta el archivo activo;
- abre automáticamente la terminal integrada;
- muestra la salida del programa.

Internamente equivale a ejecutar:

```powershell
python sintaxis.py
```

desde la terminal.

---

# ¿Qué es la sintaxis?

La sintaxis es el conjunto de reglas que define cómo debe escribirse un programa para que el intérprete pueda comprenderlo.

Ejemplos de reglas sintácticas:

- uso correcto de paréntesis;
- uso de comillas;
- uso de los dos puntos (`:`);
- orden de las instrucciones;
- indentación.

Si alguna regla se incumple, Python genera un error de sintaxis.

---

# ¿Qué es la indentación?

La indentación consiste en desplazar una línea hacia la derecha mediante espacios.

En muchos lenguajes la indentación únicamente mejora la legibilidad.

En Python es diferente.

La indentación **forma parte de la sintaxis** y define qué instrucciones pertenecen a un mismo bloque de código.

Por ello, una indentación incorrecta impide ejecutar el programa.

---

# Primer bloque de código con `if`

Ejemplo:

```python
if 5 > 3:
    print("Cinco es mayor que tres")
```

En este ejemplo:

- `if` inicia un bloque condicional.
- Los dos puntos (`:`) indican que comienza un bloque.
- La línea indentada pertenece al bloque del `if`.

Salida:

```text
Cinco es mayor que tres
```

---

# Importancia de los dos puntos (`:`)

En Python, las estructuras que crean bloques deben finalizar con dos puntos.

Ejemplos:

```python
if condicion:
```

```python
for elemento in lista:
```

```python
while condicion:
```

```python
def funcion():
```

```python
class Persona:
```

Los dos puntos indican al intérprete que la siguiente línea deberá estar indentada.

---

# Funcionamiento interno de la indentación

Cuando Python encuentra:

```python
if 5 > 3:
```

espera inmediatamente un bloque indentado.

Internamente ocurre algo similar a:

```text
Leer condición

↓

Encontrar ':'

↓

Esperar bloque indentado

↓

Ejecutar instrucciones del bloque

↓

Continuar con el resto del programa
```

Si dicho bloque no existe, el programa genera un error.

---

# Error por falta de indentación

Ejemplo incorrecto:

```python
if 5 > 3:
print("Cinco es mayor que tres")
```

Resultado:

```text
IndentationError
```

El intérprete esperaba una línea indentada después del `if`, pero encontró una instrucción al mismo nivel.

---

# Errores por exceso de indentación

El curso menciona que agregar demasiadas tabulaciones puede provocar confusión.

Esto es correcto.

Sin embargo, conviene distinguir dos situaciones:

## Caso 1

La indentación adicional pertenece realmente a un nuevo bloque.

No existe ningún problema.

## Caso 2

La indentación adicional no corresponde a ningún bloque.

Python producirá un error como:

```text
IndentationError: unexpected indent
```

Por tanto, no se trata únicamente de una cuestión de estilo.

La indentación debe representar correctamente la estructura lógica del programa.

---

# Bloques anidados

Es posible colocar un bloque dentro de otro.

Ejemplo:

```python
if 5 > 3:
    if 5 > 3:
        print("Cinco es mayor que tres")

    print("Cuatro es mayor que tres")
```

Cada nuevo bloque incrementa un nivel de indentación.

Visualmente:

```text
if

└── if

    └── print

└── print
```

Esto facilita comprender la jerarquía del programa.

---

# ¿Espacios o tabulaciones?

El contenido del curso habla de "tabulación".

Sin embargo, la recomendación oficial de Python (PEP 8) es utilizar **cuatro espacios por nivel de indentación**.

Ejemplo recomendado:

```python
if condicion:
    print("Hola")
```

No es recomendable mezclar:

- espacios;
- tabulaciones (`Tab`).

Mezclar ambos puede producir errores difíciles de detectar.

La mayoría de editores modernos, incluido Visual Studio Code, convierten automáticamente la tecla **Tab** en cuatro espacios.

---

# ¿Cómo detecta Visual Studio Code estos errores?

Las extensiones instaladas, especialmente **Pylance**, realizan un análisis estático del código.

Esto significa que muchas veces el editor detecta errores **antes de ejecutar el programa**.

Por ello aparecen:

- subrayados rojos;
- advertencias;
- sugerencias de corrección.

Esta retroalimentación temprana reduce considerablemente el tiempo de depuración.

---

# Flujo de ejecución

```text
Escribir código

↓

Pylance analiza la sintaxis

↓

¿Hay errores?

├── Sí → Mostrar advertencias
└── No

↓

Run Python File

↓

Python ejecuta el programa

↓

Mostrar salida en la terminal
```

---

# Problemas frecuentes en producción

## Error 1

```text
IndentationError
```

### Causa

Falta de indentación o alineación incorrecta.

### Solución

Revisar el nivel de indentación de cada bloque.

---

## Error 2

```text
SyntaxError
```

### Causa

Olvidar los dos puntos (`:`) al finalizar un `if`, `for`, `while`, `def` o `class`.

Ejemplo incorrecto:

```python
if 5 > 3
```

Correcto:

```python
if 5 > 3:
```

---

## Error 3

Mezclar espacios y tabulaciones.

### Síntomas

Errores aparentemente inexplicables de indentación.

### Prevención

Configurar Visual Studio Code para utilizar cuatro espacios automáticamente.

---

# Buenas prácticas

- Utilizar perfiles específicos para cada tecnología.
- Instalar únicamente las extensiones necesarias.
- Nombrar los archivos con nombres descriptivos.
- Utilizar cuatro espacios por nivel de indentación.
- No mezclar espacios y tabulaciones.
- Aprovechar las advertencias de Pylance antes de ejecutar el programa.
- Mantener una estructura visual consistente en todo el proyecto.

---

# Relación con la Ingeniería de IA

La indentación será una habilidad utilizada constantemente al desarrollar aplicaciones de IA.

Ejemplos:

```python
if response.status_code == 200:
    print(response.json())
```

```python
for document in documents:
    embeddings.append(model.embed(document))
```

```python
for agent in agents:
    if agent.is_active:
        agent.run()
```

Frameworks como:

- FastAPI;
- LangChain;
- LangGraph;
- CrewAI;
- AutoGen;
- Semantic Kernel;

utilizan de forma intensiva estructuras de control e indentación.

Una mala indentación provoca errores inmediatos y dificulta el mantenimiento del código.

---

# Correcciones y actualización respecto al contenido original

## Corrección 1: Tabulación vs cuatro espacios

El material habla de utilizar "una tabulación por nivel".

La recomendación oficial de Python (PEP 8) es utilizar **cuatro espacios** por nivel de indentación. Visual Studio Code suele convertir automáticamente la tecla **Tab** en cuatro espacios, por lo que ambos enfoques coinciden visualmente.

---

## Corrección 2: Rol de Copilot

El curso menciona que VS Code puede sugerir líneas mediante Copilot.

Es importante aclarar que **GitHub Copilot no forma parte del soporte básico de Python** ni es necesario para aprender el lenguaje. Es una herramienta opcional de asistencia basada en IA.

---

## Corrección 3: Run Python File

El botón **Run Python File** no ejecuta el código por sí mismo.

Internamente lanza un comando equivalente a:

```powershell
python nombre_del_archivo.py
```

utilizando la terminal integrada de Visual Studio Code.

---

# Preguntas técnicas de entrevista

## 1. ¿Por qué la indentación es obligatoria en Python mientras que en otros lenguajes no?

**Qué evalúa:** Comprensión del diseño sintáctico de Python y del concepto de bloques de código.

**Error común:** Responder que la indentación es únicamente una cuestión estética.

---

## 2. ¿Qué diferencia existe entre un `IndentationError` y un `SyntaxError`?

**Qué evalúa:** Capacidad para interpretar errores del intérprete.

**Error común:** Considerar ambos errores como equivalentes.

---

## 3. ¿Qué ventajas aporta Pylance durante el desarrollo?

**Qué evalúa:** Conocimiento del análisis estático y de herramientas modernas de desarrollo.

**Error común:** Pensar que Pylance únicamente proporciona autocompletado.

---

# Recursos oficiales

- PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/
- Visual Studio Code Python Extension: https://code.visualstudio.com/docs/python/python-tutorial
- Pylance: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
- Documentación oficial de Python: https://docs.python.org/3/
```