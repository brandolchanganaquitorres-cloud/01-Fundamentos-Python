# Clase 4: Ejecución de Python en Windows desde PowerShell

## Objetivos de aprendizaje

Al finalizar esta clase serás capaz de:

- Verificar correctamente la instalación de Python desde PowerShell.
- Comprender cómo intervienen las variables de entorno al ejecutar Python.
- Crear, editar y ejecutar tu primer programa en Python.
- Utilizar el autocompletado de PowerShell para aumentar la productividad.
- Trabajar con el intérprete interactivo de Python (REPL).
- Diferenciar cuándo utilizar un script `.py` y cuándo utilizar la consola interactiva.

---

# Introducción

Una vez instalado Python y configuradas correctamente las variables de entorno, el siguiente paso consiste en ejecutar código.

Existen dos formas principales de hacerlo:

1. Ejecutando archivos `.py`.
2. Utilizando el intérprete interactivo (REPL).

Ambos métodos forman parte del flujo de trabajo diario de cualquier desarrollador de software o AI Engineer.

---

# Verificación de la instalación de Python

Antes de escribir cualquier programa es recomendable comprobar que Python puede ejecutarse correctamente desde la terminal.

Esta comprobación confirma que:

- Python está instalado.
- Las variables de entorno están correctamente configuradas.
- La terminal puede localizar el intérprete desde cualquier directorio.

---

## Abrir PowerShell

Existen dos formas sencillas de abrir PowerShell.

### Método 1

Desde cualquier carpeta:

1. Mantener presionada la tecla **Shift**.
2. Hacer clic derecho.
3. Seleccionar:

```text
Open PowerShell Window Here
```

Este método abre la terminal directamente en la carpeta donde se trabajará.

---

### Método 2

Desde el menú Inicio:

1. Abrir Inicio.
2. Escribir:

```text
PowerShell
```

3. Ejecutar la aplicación.

---

# Comprobar la versión de Python

Para verificar que Python responde correctamente, ejecutar:

```powershell
python --version
```

o

```powershell
python -V
```

Ejemplo:

```text
Python 3.13.2
```

Si el comando funciona desde cualquier carpeta significa que las variables de entorno (`PATH`) están correctamente configuradas.

> **Nota:** El material original menciona `python-version`, pero el comando correcto es `python --version` (o `python -V`). `python-version` no es un comando válido del intérprete estándar de Python.

---

# ¿Por qué son importantes las variables de entorno?

Cuando ejecutas:

```powershell
python
```

Windows busca automáticamente el ejecutable en las rutas registradas en la variable `PATH`.

Gracias a ello puedes ejecutar Python desde cualquier ubicación sin escribir la ruta completa al ejecutable.

Esto aporta varias ventajas:

- Ejecutar scripts desde cualquier carpeta.
- Evitar errores relacionados con la ubicación del intérprete.
- Mejorar la productividad al trabajar desde la terminal.

---

# Crear el primer programa en Python

Los programas de Python se almacenan en archivos con extensión:

```text
.py
```

Cada archivo representa un módulo o script ejecutable.

---

## Crear un archivo desde PowerShell

Para crear un archivo vacío se puede utilizar:

```powershell
New-Item "basico.py"
```

Al ejecutarlo aparecerá el archivo en el directorio actual.

---

# Editar el archivo

Una forma sencilla consiste en abrir el archivo con el Bloc de notas.

Escribir el siguiente código:

```python
print("Hola, mundo")
```

Guardar el archivo antes de ejecutarlo.

---

# La función `print()`

`print()` es una función integrada de Python cuya finalidad es mostrar información en la salida estándar (normalmente la consola).

Sintaxis:

```python
print(valor)
```

Ejemplo:

```python
print("Hola, mundo")
```

Salida:

```text
Hola, mundo
```

Aunque suele ser la primera instrucción que se aprende, `print()` es una herramienta muy utilizada durante el desarrollo para:

- visualizar resultados;
- depurar programas;
- inspeccionar variables;
- comprobar el flujo de ejecución.

---

# Ejecutar un script desde PowerShell

Para ejecutar el archivo creado:

```powershell
python basico.py
```

Resultado esperado:

```text
Hola, mundo
```

Cada vez que ejecutes el comando, Python leerá el contenido del archivo desde el inicio y ejecutará las instrucciones en orden.

---

# Uso del autocompletado en PowerShell

PowerShell incorpora autocompletado mediante la tecla **Tab**.

Ejemplo:

Si el archivo se llama:

```text
basico.py
```

puedes escribir únicamente:

```powershell
python ba
```

y pulsar:

```text
Tab
```

PowerShell completará automáticamente el nombre del archivo.

Esta característica:

- reduce errores tipográficos;
- acelera la escritura de comandos;
- mejora la productividad cuando se trabaja con muchos archivos.

---

# El intérprete interactivo de Python (REPL)

Además de ejecutar archivos, Python dispone de un entorno interactivo denominado **REPL** (*Read-Eval-Print Loop*).

Permite escribir instrucciones una por una y obtener el resultado inmediatamente.

Es una herramienta muy útil para:

- realizar pruebas rápidas;
- experimentar con funciones;
- verificar expresiones;
- aprender la sintaxis del lenguaje.

---

# Abrir el intérprete interactivo

Desde PowerShell ejecutar:

```powershell
python
```

Aparecerá un mensaje similar al siguiente:

```text
Python 3.13.2
>>>
```

El símbolo:

```text
>>>
```

indica que el intérprete está esperando instrucciones.

---

# Ejecutar instrucciones

Dentro del REPL se pueden escribir expresiones directamente.

### Imprimir un texto

```python
print("Hola, mundo")
```

Salida:

```text
Hola, mundo
```

---

### Realizar operaciones matemáticas

```python
3 + 2
```

Resultado:

```text
5
```

Una de las características del REPL es que muestra automáticamente el resultado de las expresiones, sin necesidad de utilizar `print()`.

---

# Salir del intérprete

Para regresar a PowerShell ejecutar:

```python
exit()
```

o

```python
quit()
```

También puede utilizarse el atajo:

```text
Ctrl + Z
```

seguido de:

```text
Enter
```

en Windows.

---

# Script vs REPL

Aunque ambos permiten ejecutar código Python, tienen objetivos distintos.

| Script (.py) | REPL |
|--------------|------|
| Código persistente | Código temporal |
| Se guarda en archivos | No se guarda automáticamente |
| Ideal para proyectos | Ideal para pruebas rápidas |
| Ejecuta múltiples instrucciones | Ejecuta una instrucción cada vez |
| Reutilizable | Experimental |

En un proyecto profesional ambos se utilizan de forma complementaria.

---

# Flujo de ejecución

## Ejecución de un archivo

```text
PowerShell

↓

python basico.py

↓

Python abre el archivo

↓

Lee el código línea por línea

↓

Ejecuta cada instrucción

↓

Finaliza el proceso
```

---

## Uso del REPL

```text
PowerShell

↓

python

↓

REPL

↓

Usuario escribe una instrucción

↓

Python la ejecuta

↓

Muestra el resultado

↓

Espera la siguiente instrucción
```

---

# Problemas frecuentes en producción

## Error 1: `'python' no se reconoce como un comando`

### Causa

Python no está en la variable `PATH`.

### Solución

Verificar las variables de entorno y reiniciar la terminal.

---

## Error 2: `No such file`

### Causa

El archivo `.py` no existe o el nombre es incorrecto.

### Diagnóstico

Listar los archivos del directorio actual:

```powershell
dir
```

---

## Error 3: Error de sintaxis

Ejemplo:

```python
print(Hola)
```

Salida:

```text
NameError
```

### Causa

Las cadenas de texto deben escribirse entre comillas.

Correcto:

```python
print("Hola")
```

---

## Error 4: Ejecutar desde un directorio incorrecto

Si PowerShell no se encuentra en la carpeta donde está el archivo:

```powershell
python basico.py
```

producirá un error indicando que no puede encontrar el archivo.

### Solución

Moverse al directorio correcto con:

```powershell
cd ruta\del\directorio
```

o abrir PowerShell directamente en esa carpeta.

---

# Buenas prácticas

- Verificar siempre la instalación con `python --version`.
- Guardar los scripts con extensión `.py`.
- Utilizar nombres de archivos descriptivos y sin espacios.
- Aprovechar el autocompletado mediante la tecla **Tab**.
- Usar el REPL para pruebas rápidas y los scripts para código reutilizable.
- Mantener una estructura organizada de carpetas para los proyectos.

---

# Relación con la Ingeniería de IA

La ejecución de scripts desde la terminal es una habilidad fundamental para trabajar con herramientas del ecosistema de IA.

A diario ejecutarás comandos como:

```powershell
python app.py
```

```powershell
python train.py
```

```powershell
python rag.py
```

```powershell
python main.py
```

o iniciarás servidores mediante:

```powershell
uvicorn main:app --reload
```

Comprender cómo se ejecutan los programas desde la terminal facilita posteriormente el uso de frameworks como FastAPI, LangChain, herramientas de automatización y procesos de entrenamiento de modelos.

---

# Correcciones y actualización respecto al contenido original

## Corrección 1: Comando para consultar la versión

El material original indica:

```powershell
python-version
```

Este comando es incorrecto.

La forma correcta es:

```powershell
python --version
```

o

```powershell
python -V
```

---

## Corrección 2: Creación de archivos en PowerShell

El contenido original utiliza:

```powershell
new item "basico.py"
```

La sintaxis habitual en PowerShell es:

```powershell
New-Item "basico.py"
```

PowerShell no distingue mayúsculas de minúsculas, pero el nombre del cmdlet incluye un guion (`-`).

---

## Corrección 3: Nombres de archivos

Aunque Windows permite caracteres acentuados en los nombres de archivo, en proyectos de desarrollo se recomienda utilizar nombres sin espacios ni tildes, por ejemplo:

```text
basico.py
```

en lugar de:

```text
básico.py
```

Esto evita problemas de compatibilidad entre sistemas operativos y herramientas de automatización.

---

# Preguntas técnicas de entrevista

## 1. ¿Cuál es la diferencia entre ejecutar un archivo `.py` y utilizar el REPL?

**Qué evalúa:** Comprensión de los distintos modos de ejecución de Python y sus casos de uso.

**Error común:** Pensar que ambos se utilizan indistintamente sin considerar persistencia, reutilización y propósito.

---

## 2. ¿Por qué `print()` sigue siendo útil en proyectos profesionales?

**Qué evalúa:** Conocimiento de técnicas básicas de depuración y observabilidad durante el desarrollo.

**Error común:** Considerar que `print()` solo sirve para ejercicios introductorios.

---

## 3. ¿Qué ventajas ofrece el autocompletado de PowerShell al trabajar con proyectos grandes?

**Qué evalúa:** Productividad en la línea de comandos y buenas prácticas al interactuar con el sistema operativo.

**Error común:** Ignorar herramientas del shell que reducen errores y aceleran el flujo de trabajo.

---

# Recursos oficiales

- Documentación oficial de Python: https://docs.python.org/3/tutorial/interpreter.html
- Tutorial oficial de Python: https://docs.python.org/3/tutorial/
- PowerShell Documentation (Microsoft Learn): https://learn.microsoft.com/powershell/
```