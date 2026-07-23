# Clase 1 — Introducción a Python: El lenguaje que impulsa la Inteligencia Artificial y la Automatización

## Objetivo

Comprender por qué Python se ha convertido en uno de los lenguajes de programación más importantes del mundo, conocer sus principales características, descubrir sus aplicaciones reales en la industria y entender los fundamentos que servirán como base para el desarrollo de software, automatización, Ciencia de Datos e Inteligencia Artificial.

---

# Conceptos principales

## ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, interpretado, multiparadigma y de propósito general, diseñado para ser sencillo de aprender, fácil de leer y extremadamente productivo.

Su filosofía de diseño prioriza:

- Simplicidad
- Claridad
- Legibilidad
- Productividad
- Desarrollo rápido

Gracias a estas características, Python es actualmente uno de los lenguajes más utilizados en el mundo tanto por principiantes como por desarrolladores profesionales.

---

## ¿Por qué Python está en todas partes?

Python es utilizado en prácticamente todos los sectores tecnológicos debido a su enorme ecosistema de bibliotecas, facilidad de uso y gran comunidad.

Algunos ejemplos reales incluyen:

- 📷 Instagram gestiona millones de usuarios utilizando Python en parte de su infraestructura.
- 🚀 La NASA emplea Python para análisis científicos y procesamiento de datos espaciales.
- 🎵 Spotify utiliza Python para sistemas de recomendación musical.
- 🤖 OpenAI desarrolla gran parte de su ecosistema utilizando Python.
- 📦 Amazon emplea Python en automatización, backend y Machine Learning.
- ☁ Microsoft lo integra en Azure AI y herramientas de ciencia de datos.
- 🔍 Google mantiene numerosos proyectos escritos en Python.

Su versatilidad permite utilizar el mismo lenguaje para:

- Desarrollo Web
- Inteligencia Artificial
- Machine Learning
- Ciencia de Datos
- Automatización
- DevOps
- Ciberseguridad
- Robótica
- Cloud Computing
- Videojuegos
- Internet de las Cosas (IoT)

---

## ¿Qué hace que Python sea tan simple?

Python posee una sintaxis muy cercana al lenguaje humano.

Esto permite que el desarrollador se concentre en resolver problemas en lugar de memorizar reglas complejas del lenguaje.

Ejemplo:

```python
print("Hola, mundo")
```

Con una sola línea ya es posible ejecutar un programa funcional.

---

## Python como lenguaje de alto nivel

Python pertenece a la categoría de lenguajes de alto nivel.

Esto significa que abstrae al desarrollador de los detalles internos del hardware.

En lugar de preocuparse por:

- registros
- memoria
- direcciones
- punteros

el desarrollador puede concentrarse en la lógica del negocio.

---

## ¿Qué significa que Python sea interpretado?

Python no necesita compilarse previamente como ocurre con C o C++.

El intérprete ejecuta el código prácticamente en tiempo real.

Flujo simplificado:

```
Código Python
       │
       ▼
 Intérprete CPython
       │
       ▼
 Bytecode (.pyc)
       │
       ▼
 Python Virtual Machine
       │
       ▼
 Resultado
```

---

## Filosofía de Python

Python sigue el famoso documento denominado:

**The Zen of Python**

Algunos de sus principios más importantes son:

- Simple es mejor que complejo.
- Explícito es mejor que implícito.
- La legibilidad cuenta.
- Debería existir una forma obvia de hacer las cosas.
- Los errores nunca deberían pasar silenciosamente.

Puede visualizarse escribiendo:

```python
import this
```

---

# Explicación detallada

Python fue creado por Guido van Rossum y publicado por primera vez en 1991.

Desde entonces ha evolucionado hasta convertirse en uno de los pilares de la ingeniería de software moderna.

Actualmente domina sectores como:

- Inteligencia Artificial
- Ciencia de Datos
- Automatización
- Desarrollo Backend
- Cloud Computing
- Ingeniería Financiera
- Bioinformática
- Robótica

Su éxito se debe a una combinación de factores:

- curva de aprendizaje muy baja
- enorme cantidad de librerías
- gran comunidad
- facilidad para mantener código
- rapidez para desarrollar productos

Python permite que incluso proyectos extremadamente complejos puedan desarrollarse utilizando un código relativamente sencillo.

---

# ¿Qué aprenderás en este curso?

Durante el curso construirás las bases de la programación mediante conceptos fundamentales.

## Variables

Permiten almacenar información.

Ejemplo:

```python
nombre = "Carlos"
edad = 25
```

---

## Booleanos

Representan únicamente dos estados.

```python
True
False
```

Son la base de cualquier sistema de decisiones.

---

## Condicionales

Permiten tomar decisiones.

```python
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

---

## Bucles

Automatizan tareas repetitivas.

```python
for i in range(5):
    print(i)
```

---

## Automatización

Python permite automatizar:

- envío de correos
- generación de reportes
- procesamiento de archivos
- extracción de información
- integración entre sistemas
- bots
- APIs

---

# Ejemplos del curso

## Primer programa

```python
print("Hola, mundo")
```

Salida:

```
Hola, mundo
```

---

## Variable

```python
nombre = "Ana"

print(nombre)
```

---

## Booleano

```python
es_estudiante = True
```

---

## Condicional

```python
if es_estudiante:
    print("Tiene descuento")
else:
    print("Precio normal")
```

---

## Bucle

```python
for numero in range(3):
    print(numero)
```

Resultado:

```
0
1
2
```

---

# Explicación técnica

Internamente Python funciona mediante varias etapas.

```
Código fuente (.py)

        │

        ▼

Parser

        │

        ▼

AST
(Abstract Syntax Tree)

        │

        ▼

Compilación a Bytecode

        │

        ▼

Python Virtual Machine

        │

        ▼

Sistema Operativo
```

El bytecode es independiente del sistema operativo.

La Python Virtual Machine ejecuta dicho bytecode.

Esto proporciona portabilidad.

---

# Casos de uso reales

## Google

- Automatización
- Testing
- Infraestructura

---

## Microsoft

- Azure AI
- Machine Learning
- Power Platform

---

## Amazon

- AWS
- Automatización
- Backend

---

## Meta

- Herramientas internas
- IA

---

## Netflix

- Procesamiento de datos
- Recomendaciones

---

## Spotify

- Sistemas de recomendación
- Ciencia de Datos

---

## NASA

- Simulación
- Procesamiento científico

---

## OpenAI

- Modelos de IA
- APIs
- Entrenamiento
- Evaluación

---

## Anthropic

- LLMs
- Agentes
- Evaluación de modelos

---

# Aplicación empresarial

Python se utiliza ampliamente en:

## Automatización

- generación de PDFs
- reportes
- ETLs
- procesamiento masivo

---

## APIs

FastAPI

Flask

Django

---

## Inteligencia Artificial

TensorFlow

PyTorch

LangChain

Semantic Kernel

CrewAI

AutoGen

OpenAI SDK

---

## Cloud

AWS Lambda

Azure Functions

Google Cloud Functions

---

## Microservicios

FastAPI

Django REST

Flask

---

## Data Engineering

Apache Airflow

PySpark

Pandas

Polars

---

# Actualizaciones importantes (Estado del arte)

## Contenido del curso

- Variables
- Booleanos
- if
- else
- bucles
- print()

---

## Actualización moderna (2026)

Actualmente Python domina el ecosistema de IA gracias a herramientas como:

- OpenAI SDK
- Anthropic SDK
- Google GenAI SDK
- LangGraph
- CrewAI
- AutoGen
- MCP (Model Context Protocol)
- FastAPI
- uv
- Ruff
- Pydantic AI
- LlamaIndex
- Polars (como alternativa moderna a Pandas en ciertos casos)

**Mejores prácticas actuales:**

- Utilizar entornos virtuales (`venv` o `uv`).
- Preferir tipado estático con `typing`.
- Formatear código con `ruff format` o `black`.
- Validar datos con `Pydantic`.
- Escribir pruebas automatizadas con `pytest`.
- Mantener dependencias actualizadas y fijadas mediante archivos de requisitos o gestores modernos.

---

# Comandos más utilizados por profesionales Senior

| Comando | Frecuencia | Importancia | Explicación |
|----------|------------|-------------|-------------|
| print() | ⭐⭐⭐⭐⭐ | Muy alta | Mostrar información en pantalla |
| input() | ⭐⭐⭐⭐⭐ | Muy alta | Leer datos del usuario |
| if | ⭐⭐⭐⭐⭐ | Muy alta | Tomar decisiones |
| else | ⭐⭐⭐⭐⭐ | Muy alta | Ejecutar alternativa |
| elif | ⭐⭐⭐⭐⭐ | Muy alta | Varias condiciones |
| for | ⭐⭐⭐⭐⭐ | Muy alta | Repetición controlada |
| while | ⭐⭐⭐⭐ | Alta | Repetición basada en condición |
| import | ⭐⭐⭐⭐⭐ | Muy alta | Importar módulos |
| def | ⭐⭐⭐⭐⭐ | Muy alta | Crear funciones |
| class | ⭐⭐⭐⭐ | Alta | Programación orientada a objetos |

---

# Buenas prácticas

## ✅ Qué hacer

- Escribir nombres descriptivos.
- Mantener funciones pequeñas.
- Documentar cuando sea necesario.
- Seguir PEP 8.
- Utilizar comentarios solo cuando aporten contexto.

---

## ❌ Qué NO hacer

- Variables con nombres ambiguos.

```python
a=5
b=10
```

---

Mejor:

```python
precio = 5
cantidad = 10
```

---

## Errores comunes

- Mezclar espacios y tabulaciones.
- No usar indentación correcta.
- Crear funciones demasiado largas.
- Repetir código innecesariamente.

---

# Ejemplos empresariales

## Nivel Junior

Automatizar el cambio de nombre de cientos de archivos.

---

## Nivel Mid

Consumir una API REST y almacenar la información en una base de datos.

---

## Nivel Senior

Construir un sistema de agentes de IA que coordine múltiples modelos de lenguaje para automatizar procesos empresariales.

---

## Sectores

### 🏦 Banca

Detección de fraude.

### 🛒 Retail

Predicción de ventas.

### 📡 Telecomunicaciones

Optimización de redes.

### 🏥 Salud

Diagnóstico asistido mediante IA.

### 🏭 Industria

Mantenimiento predictivo.

### ☁ Cloud

Automatización de infraestructura.

### 🤖 IA

Entrenamiento de modelos.

---

# Ejercicio práctico

Crear un programa que:

1. Muestre un saludo.
2. Guarde tu nombre.
3. Pregunte tu edad.
4. Indique si eres mayor de edad.
5. Muestre un mensaje final.

---

# Ejercicio de nivel Senior

Diseña un asistente en Python que:

- reciba solicitudes desde una API,
- consulte una base de datos,
- invoque un modelo de IA,
- genere un reporte,
- almacene los resultados,
- notifique por correo electrónico al usuario.

---

# Preguntas de entrevista técnica

## ¿Por qué Python es considerado un lenguaje de alto nivel?

**Respuesta:**

Porque abstrae los detalles del hardware y permite centrarse en la lógica del programa.

---

## ¿Qué significa que Python sea interpretado?

**Respuesta:**

Que el código es ejecutado por un intérprete sin requerir una compilación tradicional previa del programa completo.

---

## ¿Qué ventaja ofrece la sintaxis de Python?

**Respuesta:**

Mayor legibilidad, menor curva de aprendizaje y mayor productividad.

---

## ¿Por qué Python domina la IA?

**Respuesta:**

Por su ecosistema de bibliotecas, comunidad, facilidad de integración y soporte de los principales frameworks de Machine Learning y Deep Learning.

---

# Relación con IA

Python es el lenguaje principal para desarrollar:

- Prompt Engineering
- RAG
- AI Agents
- LangChain
- LangGraph
- CrewAI
- Semantic Kernel
- AutoGen
- OpenAI SDK
- Azure AI Foundry
- MLOps
- LLMOps
- Fine-Tuning
- Vector Databases

Aprender Python es uno de los requisitos fundamentales para convertirse en un AI Engineer moderno.

---

# Herramientas relacionadas

- Python
- VS Code
- PyCharm
- Jupyter Notebook
- FastAPI
- Django
- Flask
- OpenAI SDK
- Anthropic SDK
- LangChain
- LangGraph
- CrewAI
- AutoGen
- Semantic Kernel
- Docker
- Kubernetes
- Git
- GitHub
- PostgreSQL
- Redis
- MongoDB
- Pandas
- NumPy
- Polars
- PyTorch
- TensorFlow

---

# Recursos adicionales

## Documentación oficial

- https://docs.python.org/3/

## Libros

- *Python Crash Course* — Eric Matthes
- *Fluent Python* — Luciano Ramalho
- *Effective Python* — Brett Slatkin

## Artículos

- PEP 8 — Style Guide for Python Code
- The Zen of Python (PEP 20)

## Repositorios GitHub

- python/cpython
- pallets/flask
- fastapi/fastapi
- pydantic/pydantic

## Cursos

- Python for Everybody
- CS50 Python
- Documentación oficial de Python

---

# Glosario

| Término | Definición |
|----------|------------|
| Python | Lenguaje de programación de alto nivel |
| Variable | Espacio para almacenar datos |
| Booleano | Tipo de dato con valores `True` o `False` |
| Condicional | Estructura para tomar decisiones |
| Bucle | Repetición automática de instrucciones |
| Intérprete | Programa que ejecuta el código Python |
| Bytecode | Representación intermedia del código Python |
| PVM | Python Virtual Machine |
| Biblioteca | Conjunto reutilizable de funciones y clases |
| Sintaxis | Reglas para escribir código válido |

---

# Resumen Ejecutivo

Python es un lenguaje de programación de alto nivel, interpretado y multiparadigma que destaca por su simplicidad, claridad y productividad. Su sintaxis cercana al lenguaje natural permite enfocarse en la resolución de problemas en lugar de la complejidad del lenguaje.

Gracias a su amplio ecosistema y a una comunidad global muy activa, Python se ha convertido en el estándar de facto para la Inteligencia Artificial, la Ciencia de Datos, la automatización, el desarrollo web y la computación en la nube. Aprender sus fundamentos —variables, tipos de datos, estructuras de control y bucles— constituye la base para desarrollar aplicaciones profesionales y sistemas de IA modernos.

---

# Notas personales

> ✍️ Espacio para escribir observaciones, ejemplos propios, comandos útiles y dudas surgidas durante el estudio.

---

# Checklist

- [ ] Entendí qué es Python.
- [ ] Comprendí por qué es un lenguaje de alto nivel.
- [ ] Ejecuté mi primer programa con `print()`.
- [ ] Comprendí el flujo de ejecución de Python.
- [ ] Identifiqué aplicaciones reales de Python.
- [ ] Revisé las buenas prácticas recomendadas.
- [ ] Realicé el ejercicio práctico.
- [ ] Analicé el reto de nivel Senior.
- [ ] Respondí las preguntas de entrevista técnica.
- [ ] Estoy listo para continuar con la siguiente clase.