# Clase 3 — Variables de Entorno de Python en Windows

## Objetivo

Comprender qué son las variables de entorno en Windows, cuál es su función dentro del sistema operativo y cómo permiten ejecutar Python desde cualquier terminal o carpeta mediante la configuración de la variable **Path**.

Al finalizar esta clase serás capaz de:

- Comprender el funcionamiento de las variables de entorno.
- Diferenciar las variables de usuario y las variables del sistema.
- Verificar si Python fue agregado correctamente al **Path**.
- Confirmar que Python puede ejecutarse desde cualquier ubicación del sistema.

---

# Conceptos principales

## ¿Qué son las variables de entorno?

Las variables de entorno son configuraciones del sistema operativo que almacenan información utilizada por Windows y por las aplicaciones para funcionar correctamente.

Una de las variables más importantes es **Path**, ya que contiene una lista de directorios donde Windows busca programas ejecutables cuando el usuario escribe un comando en la terminal.

En el contexto de Python, esta configuración permite ejecutar el intérprete sin necesidad de indicar la ruta completa donde está instalado.

---

## ¿Por qué son importantes para Python?

Cuando se instala Python marcando la opción:

```text
Add Python to PATH
```

el instalador agrega automáticamente las rutas necesarias dentro de la variable **Path**.

Esto permite ejecutar comandos como:

```powershell
python
```

desde cualquier:

- PowerShell.
- Símbolo del sistema (CMD).
- Windows Terminal.
- Terminal integrada de Visual Studio Code.

Sin esta configuración sería necesario navegar manualmente hasta la carpeta donde se encuentra el ejecutable antes de poder utilizar Python.

---

## ¿Qué hace la opción Add to PATH?

Durante la instalación, la opción **Add Python to PATH** registra automáticamente las carpetas necesarias dentro de la variable **Path**.

Normalmente se agregan dos rutas:

- La carpeta donde se encuentra el intérprete de Python.
- La carpeta **Scripts**, donde se instalan herramientas como `pip`.

Gracias a ello, Windows puede localizar estos ejecutables automáticamente.

---

## ¿Qué es la variable Path?

La variable **Path** es una variable de entorno que contiene una lista ordenada de directorios.

Cuando el usuario ejecuta un comando como:

```powershell
python
```

Windows busca ese ejecutable siguiendo este proceso:

1. Revisa la carpeta actual.
2. Consulta cada una de las rutas registradas en **Path**.
3. Si encuentra el ejecutable, lo inicia.
4. Si no lo encuentra, devuelve un error indicando que el comando no existe.

---

# Explicación detallada

## ¿Cómo acceder a las variables de entorno?

En Windows, el procedimiento es el siguiente:

1. Abrir el menú Inicio.
2. Escribir:

```text
variable
```

3. Seleccionar:

```text
Variables de entorno
```

o, en inglés:

```text
Edit the system environment variables
```

4. Hacer clic en:

```text
Variables de entorno...
```

---

## Variables de usuario

Se encuentran en la parte superior de la ventana.

Estas variables afectan únicamente al usuario que inició sesión.

Si otro usuario utiliza el mismo equipo, no heredará estas configuraciones.

---

## Variables del sistema

Se encuentran en la parte inferior.

Estas variables afectan a todos los usuarios del equipo.

Normalmente requieren permisos administrativos para modificarse.

---

## ¿Dónde queda registrado Python?

Python suele registrar sus rutas dentro de la variable:

```text
Path
```

Al editar dicha variable deberían observarse dos rutas relacionadas con Python:

- Una correspondiente al intérprete.
- Otra correspondiente a la carpeta **Scripts**.

La presencia de ambas indica que la instalación fue configurada correctamente.

---

## ¿Cómo verificar que Python está correctamente configurado?

Después de revisar la variable **Path**, debe abrirse una nueva terminal.

Ejecutar:

```powershell
python
```

Si la configuración es correcta, se abrirá el intérprete interactivo de Python.

En caso contrario aparecerá un mensaje indicando que el comando no fue encontrado.

---

## ¿Por qué Python funciona desde cualquier carpeta?

Al estar registrado dentro de la variable **Path**, Windows ya conoce la ubicación del ejecutable.

Por ello es posible abrir una terminal en cualquier directorio y ejecutar:

```powershell
python
```

sin necesidad de indicar una ruta completa como:

```powershell
C:\Users\Usuario\AppData\Local\Programs\Python\Python313\python.exe
```

---

# Ejemplos del curso

## Ejecutar Python

```powershell
python
```

---

## Abrir el intérprete interactivo

```text
>>>
```

---

## Salir del intérprete

```python
exit()
```

o

```powershell
Ctrl + Z
Enter
```

---

# Explicación técnica

## ¿Cómo busca Windows un ejecutable?

Cuando el usuario ejecuta:

```powershell
python
```

Windows realiza internamente el siguiente proceso:

```text
Usuario

│

▼

Comando "python"

│

▼

Buscar en carpeta actual

│

▼

Buscar en cada directorio listado en PATH

│

▼

¿Existe python.exe?

│

├── Sí → Ejecutar Python

└── No → Mostrar error
```

---

## Ejemplo conceptual del contenido de PATH

```text
C:\Windows\System32

C:\Windows

C:\Program Files\Git\bin

C:\Users\Brandol\AppData\Local\Programs\Python\Python313\

C:\Users\Brandol\AppData\Local\Programs\Python\Python313\Scripts\
```

Cuando se ejecuta:

```powershell
python
```

Windows revisa cada una de estas carpetas hasta localizar el ejecutable.

---

# Casos de uso reales

## Microsoft

Visual Studio Code utiliza el **Path** para detectar automáticamente las instalaciones de Python disponibles en el sistema.

---

## OpenAI

Las herramientas basadas en Python requieren que el intérprete esté accesible desde la terminal para ejecutar SDKs, scripts y automatizaciones.

---

## Anthropic

Las utilidades de desarrollo y automatización ejecutadas desde la consola dependen de una configuración correcta del **Path**.

---

## Amazon

Los ingenieros utilizan múltiples herramientas de línea de comandos cuya detección depende de las variables de entorno.

---

## Google

Muchos SDKs y herramientas de desarrollo utilizan variables de entorno para localizar ejecutables y archivos de configuración.

---

# Aplicación empresarial

Las variables de entorno son fundamentales para:

- Desarrollo Backend.
- Automatización.
- DevOps.
- Data Engineering.
- Machine Learning.
- IA Generativa.
- Integración de SDKs.
- Ejecución de herramientas CLI.
- Contenedores Docker.
- CI/CD.

Sin una correcta configuración del entorno, numerosas herramientas no podrán localizar los ejecutables necesarios.

---

# Actualizaciones importantes (Estado del arte)

## Contenido del curso

- Variables de entorno.
- Variable **Path**.
- Variables de usuario.
- Variables del sistema.
- Verificación de Python.

---

## Actualización moderna

En proyectos profesionales es habitual utilizar, además del **Path** del sistema:

- Entornos virtuales (`venv`) para aislar dependencias por proyecto.
- Herramientas modernas como `uv`, que gestionan automáticamente intérpretes y entornos.
- Variables de entorno específicas para aplicaciones (por ejemplo, claves API o configuraciones), almacenadas en archivos `.env` y cargadas mediante bibliotecas como `python-dotenv`.

Aunque el curso se centra en el **Path**, es importante diferenciarlo de las variables de configuración de una aplicación.

---

# Comandos más utilizados por profesionales Senior

| Comando | Frecuencia de uso | Nivel de importancia | Explicación |
|----------|------------------|----------------------|-------------|
| `python` | ⭐⭐⭐⭐⭐ Muy utilizado | Muy alta | Inicia el intérprete de Python. |
| `python --version` | ⭐⭐⭐⭐⭐ Muy utilizado | Muy alta | Verifica la versión instalada. |
| `where python` (Windows) | ⭐⭐⭐⭐ Frecuente | Alta | Muestra la ubicación del ejecutable de Python. |
| `echo %PATH%` (CMD) | ⭐⭐⭐⭐ Frecuente | Alta | Muestra el contenido de la variable Path en el Símbolo del sistema. |
| `$env:Path` (PowerShell) | ⭐⭐⭐⭐ Frecuente | Alta | Muestra el valor actual de la variable Path en PowerShell. |

---

# Buenas prácticas

## Qué hacer

- Activar **Add Python to PATH** durante la instalación.
- Verificar el funcionamiento desde una terminal nueva.
- Revisar la variable **Path** únicamente cuando sea necesario.
- Mantener una única entrada válida para cada instalación de Python.

---

## Qué NO hacer

- Eliminar rutas del **Path** sin conocer su función.
- Agregar rutas duplicadas innecesariamente.
- Modificar variables del sistema sin permisos o sin comprender su impacto.
- Editar el **Path** manualmente si el instalador ya lo configuró correctamente.

---

## Errores comunes

- Olvidar activar **Add Python to PATH** durante la instalación.
- Abrir una terminal que ya estaba abierta antes de instalar Python (es necesario abrir una nueva para que tome los cambios).
- Confundir la variable **Path** con otras variables de entorno.

---

# Ejemplos empresariales

## Nivel Junior

Verificar que Python pueda ejecutarse desde la terminal antes de comenzar un proyecto.

---

## Nivel Mid

Configurar correctamente las variables de entorno en un equipo de desarrollo para garantizar que todas las herramientas CLI funcionen sin problemas.

---

## Nivel Senior

Diseñar procedimientos automatizados para estandarizar las variables de entorno en estaciones de trabajo y servidores, asegurando consistencia entre entornos de desarrollo, pruebas y producción.

---

# Ejercicio práctico

1. Abrir la configuración de variables de entorno de Windows.
2. Localizar la variable **Path**.
3. Confirmar que existen las rutas correspondientes a Python.
4. Abrir una nueva PowerShell.
5. Ejecutar:

```powershell
python
```

6. Salir del intérprete utilizando:

```python
exit()
```

---

# Ejercicio de nivel Senior

Documenta un procedimiento corporativo para validar la instalación de Python en equipos Windows, incluyendo la revisión del **Path**, la comprobación desde la terminal y un listado de errores frecuentes con sus posibles soluciones.

---

# Preguntas de entrevista técnica

## ¿Qué es una variable de entorno?

**Respuesta:** Es una configuración del sistema operativo utilizada por Windows y las aplicaciones para almacenar información necesaria durante la ejecución, como rutas de búsqueda de programas.

---

## ¿Cuál es la función de la variable Path?

**Respuesta:** Contener una lista de directorios donde Windows busca ejecutables cuando el usuario escribe un comando en la terminal.

---

## ¿Qué hace la opción Add Python to PATH?

**Respuesta:** Agrega las carpetas del intérprete y de los scripts de Python a la variable **Path**, permitiendo ejecutar Python desde cualquier ubicación.

---

## ¿Qué ocurre si Python no está en el Path?

**Respuesta:** El sistema no encontrará el ejecutable al escribir `python` y mostrará un error indicando que el comando no existe.

---

# Relación con IA

Una correcta configuración del **Path** es indispensable para trabajar posteriormente con:

- OpenAI SDK.
- Anthropic SDK.
- LangChain.
- LangGraph.
- CrewAI.
- AutoGen.
- MCP.
- Azure AI.
- AWS SDK.
- FastAPI.
- Herramientas de automatización y desarrollo ejecutadas desde la línea de comandos.

---

# Herramientas relacionadas

- Python
- Windows
- PowerShell
- CMD
- Windows Terminal
- Visual Studio Code
- Git
- GitHub
- pip
- venv

---

# Recursos adicionales

## Documentación oficial

- Python Documentation (Variables de entorno e instalación)
- Microsoft Learn (Variables de entorno en Windows)

## Libros

- *Automate the Boring Stuff with Python* — Al Sweigart.
- *Python Crash Course* — Eric Matthes.

## Repositorios GitHub

- python/cpython

## Cursos

- Fundamentos de Python.
- Git y GitHub.
- Windows Terminal.

---

# Glosario

| Término | Definición |
|----------|------------|
| Variable de entorno | Configuración del sistema utilizada por aplicaciones y el sistema operativo. |
| Path | Variable que contiene las rutas donde Windows busca ejecutables. |
| Intérprete | Programa que ejecuta código Python. |
| Ejecutable | Archivo que puede ser ejecutado por el sistema operativo. |
| PowerShell | Consola moderna de Windows para administración y automatización. |
| CMD | Símbolo del sistema clásico de Windows. |
| Scripts | Carpeta donde se instalan herramientas ejecutables de Python, como `pip`. |

---

# Resumen Ejecutivo

En esta clase se explicó el funcionamiento de las variables de entorno de Windows, con especial énfasis en la variable **Path**, que permite ejecutar Python desde cualquier terminal sin indicar la ruta completa del ejecutable. Se revisó cómo acceder a la configuración de variables de entorno, la diferencia entre variables de usuario y del sistema, y el procedimiento para verificar que Python haya quedado correctamente registrado tras la instalación.

---

# Notas personales

> _Espacio para escribir observaciones, comandos útiles o incidencias encontradas durante la configuración del entorno._

---

# Checklist

- [ ] Comprendí qué son las variables de entorno.
- [ ] Comprendí la función de la variable **Path**.
- [ ] Revisé las variables de entorno en Windows.
- [ ] Identifiqué la diferencia entre variables de usuario y del sistema.
- [ ] Confirmé que Python aparece en el **Path**.
- [ ] Verifiqué que `python` funciona desde la terminal.
- [ ] Pude salir correctamente del intérprete de Python.
- [ ] Estoy listo para continuar con la siguiente clase.