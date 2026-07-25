# Clase 2 — Instalación y Configuración del Entorno de Desarrollo para Python

## Objetivo

Preparar un entorno de desarrollo profesional para programar en Python mediante la instalación y configuración de las herramientas fundamentales del curso:

- Google Chrome.
- Visual Studio Code.
- Python.
- Git.

Al finalizar esta clase, el entorno quedará correctamente configurado para desarrollar aplicaciones en Python desde la primera práctica.

---

# Conceptos principales

## ¿Qué es un entorno de desarrollo?

Un entorno de desarrollo es el conjunto de herramientas de software que permiten escribir, ejecutar, depurar, administrar y compartir código de manera eficiente.

En este curso se utilizarán cuatro herramientas principales:

| Herramienta | Función |
|------------|----------|
| Google Chrome | Navegador para acceder al curso y consultar documentación oficial. |
| Visual Studio Code | Editor de código donde se desarrollarán los programas en Python. |
| Python | Lenguaje de programación utilizado durante todo el curso. |
| Git | Sistema de control de versiones para gestionar el código fuente. |

Estas herramientas trabajan de forma complementaria.

---

## Orden recomendado de instalación

Para evitar problemas posteriores, se recomienda instalar las herramientas en el siguiente orden:

1. Google Chrome.
2. Visual Studio Code.
3. Python.
4. Git.

---

## Repositorio del curso en GitHub

Todo el material necesario para la instalación se encuentra centralizado en el repositorio del curso.

Desde allí pueden obtenerse:

- enlaces oficiales de descarga;
- documentación;
- extensiones recomendadas para Visual Studio Code;
- recursos adicionales del curso.

Se recomienda mantener este repositorio abierto durante el desarrollo del curso.

---

# Explicación detallada

## Instalación de Google Chrome

Google Chrome será utilizado como navegador principal para:

- acceder al curso;
- consultar documentación oficial;
- visualizar recursos externos.

No requiere configuraciones especiales para este curso.

---

## Instalación de Visual Studio Code

Visual Studio Code (VS Code) será el editor principal donde se escribirá el código Python.

La página oficial detecta automáticamente el sistema operativo:

- Windows
- Linux
- macOS

y ofrece el instalador correspondiente.

---

## Opciones importantes durante la instalación

Durante el proceso de instalación aparecen diversas opciones.

Las dos configuraciones realmente importantes son:

### Registrar Code como editor

Permite abrir archivos compatibles mediante el menú contextual del sistema operativo (clic derecho).

Esto facilita trabajar con cualquier archivo desde el explorador.

---

### Add to PATH

Esta opción agrega Visual Studio Code a las variables de entorno del sistema operativo.

Gracias a ello será posible ejecutar VS Code desde cualquier terminal simplemente escribiendo:

```bash
code .
```

sin importar la carpeta en la que se encuentre el usuario.

---

### ¿Qué significa agregar un programa al PATH?

El PATH es una variable de entorno del sistema operativo.

Contiene una lista de directorios donde el sistema busca programas ejecutables.

Cuando VS Code se agrega al PATH, el sistema sabe dónde encontrar el ejecutable llamado:

```text
code
```

por lo que podrá abrirse desde cualquier terminal.

---

### Opciones opcionales

Las siguientes opciones no son obligatorias:

- Crear acceso directo en el escritorio.
- Agregar accesos en el menú contextual.
- Otras opciones de integración.

Pueden activarse según preferencia personal.

---

## Instalación de Python

El siguiente paso consiste en instalar Python desde la página oficial.

La página detecta automáticamente el sistema operativo y ofrece la versión más reciente disponible.

Durante la grabación del curso la versión era:

```text
Python 3.13.7
```

Si existe una versión más reciente, el procedimiento de instalación continúa siendo exactamente el mismo.

---

## Configuración importante durante la instalación

Antes de presionar:

```text
Install Now
```

deben activarse dos opciones.

### Add Python to PATH

Esta es la opción más importante.

Agrega el ejecutable de Python a las variables de entorno.

Gracias a ello será posible ejecutar Python desde cualquier terminal mediante:

```bash
python
```

o

```bash
python --version
```

---

### Privilegios de administrador para py.exe

Permite que el lanzador de Python (`py.exe`) pueda ejecutarse con permisos elevados cuando sea necesario.

---

### ¿Por qué es tan importante Add Python to PATH?

Si esta opción no se activa:

- Windows no encontrará el ejecutable.
- La terminal mostrará errores al escribir:

```bash
python
```

o

```bash
pip
```

Generalmente la solución consiste en:

- reinstalar Python correctamente; o
- configurar manualmente las variables de entorno.

Por ello se recomienda marcar esta opción desde el inicio.

---

## Instalación de Git

Git es el sistema de control de versiones utilizado durante el desarrollo del curso.

Su instalación es directa:

1. Descargar el instalador correspondiente al sistema operativo.
2. Ejecutarlo.
3. Presionar Install.
4. Mantener la configuración predeterminada.

No es necesario modificar opciones avanzadas durante esta instalación.

---

## Diferencia entre Git y GitHub

Es importante distinguir ambos conceptos.

### Git

Es el software instalado en el computador.

Permite:

- registrar cambios;
- crear versiones;
- volver a estados anteriores;
- trabajar con ramas;
- fusionar código.

---

### GitHub

Es una plataforma en línea donde se almacenan repositorios Git.

GitHub permite:

- alojar proyectos;
- colaborar con otros desarrolladores;
- compartir código;
- consultar documentación.

En este curso se utilizará GitHub para acceder al repositorio del curso.

---

## ¿Es obligatorio conocer Git?

No.

El conocimiento de Git no es requisito para seguir este curso de Python.

Sin embargo, se considera una habilidad fundamental para cualquier desarrollador profesional.

El curso recomienda complementar posteriormente con un curso específico de Git y GitHub.

---

## Extensiones recomendadas para Visual Studio Code

El repositorio del curso incluye una lista de extensiones recomendadas para Python.

No es necesario instalarlas inmediatamente.

Posteriormente se configurará un perfil específico para Python que instalará muchas de ellas automáticamente.

---

## Estado esperado al finalizar la instalación

Al concluir este proceso deberán estar instalados:

- Google Chrome.
- Visual Studio Code.
- Python.
- Git.

Con estas herramientas el entorno de desarrollo estará completamente preparado para comenzar a programar.

---

# Ejemplos del curso

## Abrir VS Code desde cualquier carpeta

```bash
code .
```

---

## Verificar instalación de Python

```bash
python --version
```

---

## Ejecutar Python

```bash
python
```

---

# Explicación técnica

## ¿Cómo funciona la variable PATH?

El sistema operativo mantiene una lista de rutas donde busca programas ejecutables.

Cuando el usuario escribe:

```bash
python
```

el sistema:

1. busca el ejecutable dentro del PATH;
2. encuentra `python.exe`;
3. ejecuta el programa.

Si Python no está registrado en el PATH, el sistema no sabrá dónde encontrarlo.

---

## ¿Qué hace Git internamente?

Git registra cada cambio mediante objetos que almacenan:

- archivos;
- historial;
- versiones;
- ramas;
- commits.

Toda esta información queda almacenada en la carpeta:

```text
.git
```

que se crea dentro del proyecto.

---

## ¿Cómo trabaja Visual Studio Code?

VS Code funciona como una plataforma modular.

El editor base es ligero.

Las funcionalidades adicionales se incorporan mediante extensiones.

En Python, la extensión oficial proporciona:

- resaltado de sintaxis;
- IntelliSense;
- depuración;
- ejecución de scripts;
- integración con entornos virtuales.

---

# Casos de uso reales

## Google

Utiliza Git como sistema de control de versiones interno adaptado a gran escala.

---

## Microsoft

Desarrolla Visual Studio Code y mantiene la extensión oficial para Python.

---

## OpenAI

La mayoría de proyectos de investigación utilizan Python y Git.

---

## Anthropic

Claude Code trabaja directamente sobre proyectos Git.

---

## Amazon

Los equipos de desarrollo utilizan VS Code, Git y Python para automatización y servicios cloud.

---

## Netflix

Gran parte de su infraestructura de automatización utiliza Python.

---

# Aplicación empresarial

Este entorno constituye la base para desarrollar:

- APIs con FastAPI.
- Automatizaciones con Python.
- Scripts DevOps.
- Pipelines de datos.
- Machine Learning.
- IA Generativa.
- Agentes inteligentes.
- Automatizaciones empresariales.
- Microservicios.
- Integraciones cloud.

---

# Actualizaciones importantes (Estado del arte)

## Contenido del curso

- Instalación de Chrome.
- Instalación de VS Code.
- Instalación de Python.
- Instalación de Git.

---

## Actualización moderna

Actualmente es recomendable añadir también:

- Ruff (linting y formateo de alto rendimiento).
- uv (gestor moderno de paquetes y entornos virtuales).
- Pylance (mejor autocompletado para Python en VS Code).
- Python Debugger (extensión oficial separada).
- GitHub Copilot (asistencia con IA).
- Dev Containers para entornos reproducibles.

Estas herramientas no forman parte del contenido original de la clase, pero representan buenas prácticas actuales.

---

# Comandos más utilizados por profesionales Senior

| Comando | Frecuencia de uso | Nivel | Explicación |
|----------|------------------|--------|-------------|
| `python --version` | ⭐⭐⭐⭐⭐ | Muy utilizado | Verifica la versión instalada. |
| `python` | ⭐⭐⭐⭐⭐ | Muy utilizado | Inicia el intérprete interactivo. |
| `code .` | ⭐⭐⭐⭐⭐ | Muy utilizado | Abre la carpeta actual en VS Code. |
| `git --version` | ⭐⭐⭐⭐⭐ | Muy utilizado | Comprueba la instalación de Git. |
| `where python` (Windows) / `which python` (Linux/macOS) | ⭐⭐⭐⭐ | Frecuente | Localiza el ejecutable de Python. |

---

# Buenas prácticas

## Qué hacer

- Instalar software únicamente desde sus sitios oficiales.
- Agregar Python y VS Code al PATH.
- Mantener actualizado Python.
- Utilizar VS Code como editor principal.
- Mantener Git instalado incluso si aún no se utiliza.

---

## Qué NO hacer

- Descargar Python desde sitios no oficiales.
- Omitir la opción **Add Python to PATH**.
- Instalar múltiples versiones de Python sin conocer su gestión.
- Modificar opciones avanzadas de Git sin necesidad.

---

## Errores comunes

- No agregar Python al PATH.
- Instalar una versión incorrecta.
- Confundir Git con GitHub.
- Pensar que VS Code incluye Python por defecto.

---

# Ejemplos empresariales

### Nivel Junior

Configurar el entorno de desarrollo para comenzar un proyecto interno.

### Nivel Mid

Preparar el entorno para desarrollar una API REST en FastAPI utilizando Git.

### Nivel Senior

Estandarizar el entorno mediante perfiles de VS Code, contenedores de desarrollo y automatización de configuración para todo el equipo.

---

# Ejercicio práctico

1. Instalar Chrome.
2. Instalar VS Code.
3. Instalar Python marcando **Add Python to PATH**.
4. Instalar Git.
5. Abrir una terminal.
6. Ejecutar:

```bash
python --version
git --version
code .
```

Verificar que todos los comandos funcionen correctamente.

---

# Ejercicio de nivel Senior

Diseñar un procedimiento automatizado para configurar el entorno de desarrollo de un equipo completo utilizando scripts o herramientas de aprovisionamiento, garantizando que todos los desarrolladores dispongan de la misma configuración inicial.

---

# Preguntas de entrevista técnica

### ¿Qué es el PATH?

**Respuesta:** Es una variable de entorno que indica al sistema operativo dónde buscar programas ejecutables.

---

### ¿Cuál es la diferencia entre Git y GitHub?

**Respuesta:** Git es un sistema de control de versiones instalado localmente. GitHub es una plataforma para alojar repositorios Git y colaborar en proyectos.

---

### ¿Por qué es importante agregar Python al PATH?

**Respuesta:** Permite ejecutar Python desde cualquier terminal sin especificar la ruta completa al ejecutable.

---

# Relación con IA

Estas herramientas serán la base para trabajar posteriormente con:

- Prompt Engineering.
- OpenAI SDK.
- Claude SDK.
- Gemini API.
- LangChain.
- RAG.
- AI Agents.
- MCP.
- Azure AI.
- AWS Bedrock.
- MLOps.
- LLMOps.

---

# Herramientas relacionadas

- Visual Studio Code
- Python
- Git
- GitHub
- Chrome
- Pylance
- Ruff
- uv
- Docker
- FastAPI
- LangChain
- OpenAI SDK
- Azure AI Foundry
- n8n

---

# Recursos adicionales

## Documentación oficial

- Python Documentation
- Visual Studio Code Documentation
- Git Documentation
- GitHub Docs

## Libros

- *Automate the Boring Stuff with Python* — Al Sweigart.
- *Pro Git* — Scott Chacon y Ben Straub.

## Repositorios GitHub

- python/cpython
- microsoft/vscode
- git/git

## Cursos

- Python for Everybody.
- CS50 Python.
- Curso de Git y GitHub.

---

# Glosario

| Término | Definición |
|----------|------------|
| PATH | Variable de entorno que contiene las rutas de búsqueda de ejecutables. |
| VS Code | Editor de código fuente desarrollado por Microsoft. |
| Python | Lenguaje de programación de propósito general. |
| Git | Sistema de control de versiones distribuido. |
| GitHub | Plataforma para alojar repositorios Git. |
| Terminal | Interfaz de línea de comandos para interactuar con el sistema operativo. |
| Variable de entorno | Configuración del sistema utilizada por procesos y aplicaciones. |
| Ejecutable | Archivo que puede ser ejecutado por el sistema operativo. |

---

# Resumen Ejecutivo

En esta clase se preparó el entorno de desarrollo instalando Chrome, Visual Studio Code, Python y Git. Se explicó la importancia de configurar correctamente las variables de entorno, especialmente mediante la opción **Add Python to PATH**, y se diferenciaron claramente los conceptos de Git y GitHub. Con estas herramientas instaladas, el entorno queda listo para iniciar el desarrollo de aplicaciones en Python.

---

# Notas personales

> _Espacio para escribir apuntes propios._

---

# Checklist

- [ ] Instalé Google Chrome.
- [ ] Instalé Visual Studio Code.
- [ ] Activé **Add to PATH** en VS Code.
- [ ] Instalé Python.
- [ ] Activé **Add Python to PATH**.
- [ ] Instalé Git.
- [ ] Verifiqué la versión de Python.
- [ ] Verifiqué la versión de Git.
- [ ] Abrí VS Code desde la terminal.
- [ ] Estoy listo para comenzar a programar en Python.
