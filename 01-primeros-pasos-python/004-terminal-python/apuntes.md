# Configuración de las Variables de Entorno de Python en Windows

## Objetivos de aprendizaje

Al finalizar esta sección serás capaz de:

- Comprender qué son las variables de entorno en Windows.
- Entender cómo funciona internamente la variable `Path`.
- Verificar si Python fue configurado correctamente durante la instalación.
- Diagnosticar errores relacionados con `python`, `pip` y `py`.
- Configurar manualmente Python cuando sea necesario.
- Comprender por qué esta configuración es fundamental para el desarrollo profesional de software y de aplicaciones de IA.

---

# Introducción

Uno de los primeros pasos después de instalar Python consiste en asegurarse de que el sistema operativo pueda localizar el intérprete desde cualquier terminal.

Aunque durante la instalación existe la opción **"Add Python to PATH"**, comprender qué ocurre detrás de esa casilla es mucho más importante que simplemente marcarla.

Como AI Engineer o Software Engineer, constantemente trabajarás desde:

- PowerShell
- CMD
- Windows Terminal
- Visual Studio Code
- Docker
- Git Bash
- WSL (Windows Subsystem for Linux)
- Scripts de automatización
- CI/CD

Todos estos entornos dependen del mismo mecanismo: **las variables de entorno**.

No comprenderlas suele convertirse en uno de los primeros obstáculos para quienes comienzan a programar.

---

# ¿Qué son las variables de entorno?

Las variables de entorno son pares **clave–valor** que el sistema operativo mantiene en memoria para proporcionar información a los procesos en ejecución.

Ejemplos comunes:

| Variable | Propósito |
|----------|-----------|
| PATH | Ubicación de programas ejecutables |
| TEMP | Directorio de archivos temporales |
| USERPROFILE | Carpeta del usuario actual |
| APPDATA | Configuración de aplicaciones |
| HOMEPATH | Directorio personal |

Cuando cualquier programa necesita ejecutar otro programa, Windows consulta estas variables para localizarlo.

---

# ¿Qué es la variable PATH?

`PATH` es una variable especial que contiene una lista ordenada de directorios donde Windows buscará archivos ejecutables.

Por ejemplo:

```text
C:\Windows\System32
C:\Windows
C:\Program Files\Git\cmd
C:\Python313\
C:\Python313\Scripts\
```

Cada ruta representa una ubicación que Windows recorrerá automáticamente cuando escribas un comando.

---

# Funcionamiento interno de PATH

Cuando escribes:

```powershell
python
```

Windows **no sabe inicialmente dónde se encuentra Python**.

Internamente ocurre el siguiente proceso:

```text
Usuario

↓

PowerShell

↓

Windows

↓

Leer variable PATH

↓

Buscar python.exe en cada directorio

↓

¿Encontrado?

├── Sí → Ejecutar python.exe
└── No → Mostrar error
```

El sistema inspecciona secuencialmente cada carpeta incluida en `PATH` hasta localizar un ejecutable llamado `python.exe`.

Si no lo encuentra, devuelve un error indicando que el comando no existe o no puede localizarse.

---

# ¿Qué hace realmente la opción "Add Python to PATH"?

Durante la instalación de Python aparece la opción:

```text
☑ Add Python to PATH
```

Muchos usuarios la marcan sin conocer su función.

Internamente, el instalador añade automáticamente dos directorios a la variable `PATH`:

```text
C:\Users\<usuario>\AppData\Local\Programs\Python\Python313\
```

y

```text
C:\Users\<usuario>\AppData\Local\Programs\Python\Python313\Scripts\
```

> **Nota:** La versión (`Python313`) variará según la instalación realizada.

### ¿Por qué se agregan dos rutas?

Cada una cumple una función distinta.

| Ruta | Contenido |
|------|-----------|
| Python | Intérprete (`python.exe`) |
| Scripts | Herramientas instaladas con `pip` |

---

# ¿Por qué también se agrega la carpeta Scripts?

Muchos principiantes creen que únicamente necesitan ejecutar Python.

En la práctica, utilizarás constantemente herramientas instaladas mediante `pip`, por ejemplo:

```text
pip
black
pytest
uvicorn
jupyter
streamlit
fastapi
ruff
```

Todas ellas se almacenan normalmente dentro de:

```text
Scripts\
```

Si esa carpeta no forma parte de `PATH`, los comandos anteriores no funcionarán aunque estén correctamente instalados.

---

# Variables de Usuario vs Variables del Sistema

Windows distingue dos ámbitos para las variables de entorno.

## Variables de Usuario

Afectan únicamente al usuario que ha iniciado sesión.

Características:

- No requieren privilegios administrativos.
- Son la opción recomendada para instalaciones personales.
- No modifican el entorno de otros usuarios del equipo.

---

## Variables del Sistema

Se aplican globalmente.

Características:

- Requieren permisos administrativos.
- Todos los usuarios del equipo las comparten.
- Son habituales en servidores y equipos corporativos.

---

# ¿Dónde registra Python sus rutas?

Depende del tipo de instalación.

## Instalación para un único usuario

Generalmente modifica:

```text
Variables de Usuario
```

---

## Instalación para todos los usuarios

Generalmente modifica:

```text
Variables del Sistema
```

Por ello es completamente normal encontrar Python registrado en cualquiera de los dos bloques.

---

# Cómo abrir las Variables de Entorno

1. Abrir el menú Inicio.
2. Escribir:

```text
Variables de entorno
```

o en inglés:

```text
Edit the system environment variables
```

3. Seleccionar el resultado correspondiente.
4. Pulsar:

```text
Environment Variables...
```

Se abrirá la ventana de configuración.

---

# Cómo verificar la variable PATH

Dentro de la ventana:

1. Seleccionar `Path`.
2. Pulsar **Editar**.

Deberías encontrar rutas similares a:

```text
C:\Users\<usuario>\AppData\Local\Programs\Python\Python313\
```

y

```text
C:\Users\<usuario>\AppData\Local\Programs\Python\Python313\Scripts\
```

Si ambas existen, la instalación normalmente está correctamente configurada.

---

# Verificación desde PowerShell

La forma más fiable de validar la configuración consiste en abrir una **nueva** ventana de PowerShell y ejecutar:

```powershell
python
```

Si aparece el prompt interactivo:

```python
>>>
```

el intérprete fue localizado correctamente.

Salir mediante:

```python
exit()
```

o

```python
quit()
```

---

# Verificación de la versión instalada

Una comprobación más práctica consiste en consultar la versión:

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

---

# Verificar el lanzador oficial de Python

En Windows, el instalador también suele instalar el **Python Launcher**, accesible mediante:

```powershell
py
```

Consultar la versión:

```powershell
py --version
```

Este lanzador permite gestionar varias versiones de Python instaladas simultáneamente y es especialmente útil en entornos de desarrollo profesionales.

---

# ¿Qué ocurre si PATH no está configurado?

Al ejecutar:

```powershell
python
```

podrías obtener errores como:

```text
'python' no se reconoce como un comando...
```

o

```text
Command not found
```

Esto indica que Windows no pudo localizar `python.exe` en ninguna de las rutas registradas.

---

# Configuración manual de PATH

Si Python no fue agregado automáticamente, puede hacerse manualmente.

Agregar:

```text
C:\Users\<usuario>\AppData\Local\Programs\Python\Python313\
```

y:

```text
C:\Users\<usuario>\AppData\Local\Programs\Python\Python313\Scripts\
```

Después de guardar los cambios:

1. Cerrar todas las terminales abiertas.
2. Abrir una nueva PowerShell.
3. Verificar nuevamente:

```powershell
python --version
```

---

# Funcionamiento interno después de configurar PATH

Antes:

```text
PowerShell

↓

¿Dónde está python.exe?

↓

No encontrado

↓

Error
```

Después:

```text
PowerShell

↓

Leer PATH

↓

Encontrar python.exe

↓

Cargar el intérprete

↓

Ejecutar Python
```

Todo este proceso ocurre automáticamente y suele completarse en unos pocos milisegundos.

---

# Problemas frecuentes en producción

## Error 1: PATH actualizado pero PowerShell sigue fallando

### Causa

La terminal fue abierta antes de modificar las variables de entorno.

### Solución

Cerrar completamente:

- PowerShell
- CMD
- Windows Terminal
- Visual Studio Code

y volver a abrirlos.

---

## Error 2: Existe más de una instalación de Python

Síntomas:

```powershell
python --version
```

devuelve una versión distinta de la esperada.

### Diagnóstico

Comprobar qué ejecutable se está utilizando:

```powershell
where python
```

Windows mostrará todas las rutas encontradas.

### Solución

Eliminar instalaciones antiguas o ajustar el orden de las rutas en `PATH`.

---

## Error 3: `pip` funciona pero `python` no

### Causa

Solo la carpeta `Scripts` fue agregada al `PATH`.

### Solución

Agregar también la carpeta que contiene `python.exe`.

---

## Error 4: `python` abre Microsoft Store

En versiones recientes de Windows existe un alias denominado **App Execution Alias**.

Si Python no está instalado correctamente, Windows puede redirigir el comando `python` hacia Microsoft Store.

### Solución

- Instalar Python desde el instalador oficial.
- Verificar que las rutas estén presentes en `PATH`.
- Si es necesario, desactivar el alias desde **Configuración → Aplicaciones → Alias de ejecución de aplicaciones**.

---

# Buenas prácticas

- Instalar Python desde el instalador oficial.
- Activar siempre **Add Python to PATH**.
- Verificar la instalación con `python --version`.
- Confirmar el funcionamiento de `pip`.
- Utilizar `py` cuando se administren múltiples versiones de Python en Windows.
- Evitar duplicar rutas en `PATH`.
- Reiniciar las terminales después de modificar variables de entorno.

---

# Relación con la Ingeniería de IA

Comprender `PATH` resulta esencial porque numerosas herramientas del ecosistema de IA dependen de este mecanismo.

```text
PATH
│
├── python
├── pip
├── uv
├── git
├── node
├── npm
├── docker
├── kubectl
├── az
├── aws
├── gcloud
├── n8n
├── uvicorn
├── streamlit
├── jupyter
├── fastapi
└── code
```

Si cualquiera de estas herramientas no está registrada correctamente en `PATH`, no podrá ejecutarse desde la terminal, afectando flujos de desarrollo, automatización y despliegue.

---

# Correcciones y actualización respecto al contenido original

## Corrección 1: Verificación recomendada

El material original propone ejecutar:

```powershell
python
```

Aunque es válido, en la práctica profesional resulta más eficiente verificar primero la instalación mediante:

```powershell
python --version
```

o

```powershell
py --version
```

Esto confirma que el intérprete es accesible sin entrar en el modo interactivo.

---

## Corrección 2: Inclusión del Python Launcher (`py`)

El contenido original no menciona `py`, una herramienta instalada por defecto en Windows que facilita la gestión de múltiples versiones de Python y es ampliamente utilizada en entornos profesionales.

---

## Corrección 3: Alias de Microsoft Store

El material original omite un problema frecuente en Windows modernos: el redireccionamiento del comando `python` hacia Microsoft Store mediante los **App Execution Aliases**, una causa habitual de confusión para principiantes.

---

# Preguntas técnicas de entrevista

## 1. ¿Qué ocurre internamente cuando ejecutas `python` desde PowerShell?

**Qué evalúa:** Comprensión del proceso de resolución de ejecutables mediante la variable `PATH`.

**Error común:** Responder únicamente que "se abre Python" sin explicar cómo Windows localiza el ejecutable.

---

## 2. ¿Cuál es la diferencia entre las Variables de Usuario y las Variables del Sistema?

**Qué evalúa:** Conocimiento de la administración del entorno en Windows.

**Error común:** Pensar que ambas tienen exactamente el mismo comportamiento.

---

## 3. ¿Por qué el instalador añade tanto la carpeta principal de Python como la carpeta `Scripts` al `PATH`?

**Qué evalúa:** Comprensión de la estructura de instalación de Python y del funcionamiento de herramientas instaladas mediante `pip`.

**Error común:** Creer que solo `python.exe` necesita estar accesible desde la terminal.

---

# Recursos oficiales

- Documentación oficial de Python: https://docs.python.org/3/
- Uso de Python en Windows: https://docs.python.org/3/using/windows.html
- Variables de entorno en Windows (Microsoft Learn): https://learn.microsoft.com/windows/