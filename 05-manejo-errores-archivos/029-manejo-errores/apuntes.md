# Clase 29. Manejo de Excepciones en Python (`try`, `except`, `finally`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender cómo funciona el sistema de manejo de excepciones en Python, aprender a utilizar `try`, `except` y `finally`, capturar errores específicos como `ZeroDivisionError` y `NameError`, y aplicar buenas prácticas para desarrollar aplicaciones robustas y tolerantes a fallos.

---

# Contenido del curso

Durante la ejecución de un programa pueden producirse situaciones inesperadas:

- dividir un número entre cero;
- acceder a una variable inexistente;
- abrir un archivo que no existe;
- conectarse a un servidor sin conexión;
- recibir datos inválidos del usuario.

Cuando ocurre alguno de estos problemas, Python genera una **excepción** (*exception*).

Si la excepción no es manejada, el programa finaliza inmediatamente mostrando un mensaje de error.

El manejo de excepciones permite controlar estos errores y decidir cómo responder ante ellos.

---

# ¿Qué es una excepción?

Una excepción es un objeto que representa un error ocurrido durante la ejecución del programa.

Flujo normal.

```text
Programa

↓

Ejecutar instrucciones

↓

Finalizar correctamente
```

Flujo con excepción.

```text
Programa

↓

Ejecutar instrucciones

↓

Error

↓

Excepción

↓

Programa termina
```

---

# La estructura `try` y `except`

Python proporciona una estructura específica para manejar excepciones.

```python
try:
    print("Intentamos ejecutar código")
except:
    print("Ocurrió un error")
```

El bloque `try` contiene las instrucciones que podrían generar una excepción.

El bloque `except` define cómo responder si dicha excepción ocurre.

---

# Funcionamiento interno

```text
Entrar en try

↓

Ejecutar instrucciones

↓

¿Hay excepción?
```

```text
No

↓

Continuar normalmente
```

```text
Sí

↓

Buscar except compatible

↓

Ejecutar except

↓

Continuar programa
```

---

# Capturar `ZeroDivisionError`

Uno de los errores más comunes consiste en dividir un número entre cero.

Sin manejo de excepciones.

```python
resultado = 10 / 0
```

Resultado.

```text
ZeroDivisionError
```

El programa termina inmediatamente.

---

# Manejo específico

```python
try:
    resultado = 10 / 0
    print(resultado)

except ZeroDivisionError:
    print("No se puede dividir por cero.")
```

Resultado.

```text
No se puede dividir por cero.
```

La excepción es capturada y el programa continúa ejecutándose.

---

# ¿Por qué capturar excepciones específicas?

Python permite escribir.

```python
except:
```

Sin embargo, esta práctica no es recomendable.

Es preferible indicar explícitamente qué error esperamos.

```python
except ZeroDivisionError:
```

Esto comunica claramente la intención del código y evita ocultar errores inesperados.

---

# Capturar `NameError`

Cuando se intenta utilizar una variable inexistente, Python genera un `NameError`.

```python
print(x)
```

Resultado.

```text
NameError
```

---

# Manejo específico

```python
try:
    print(x)

except NameError:
    print("Esta variable no ha sido definida.")
```

Resultado.

```text
Esta variable no ha sido definida.
```

---

# Funcionamiento interno

```text
print(x)

↓

Buscar variable

↓

¿Existe?
```

```text
Sí

↓

Imprimir
```

```text
No

↓

NameError

↓

except NameError
```

---

# El bloque `finally`

Existe un tercer bloque opcional.

```python
finally
```

Su característica principal es que **siempre se ejecuta**, independientemente de que ocurra una excepción o no.

---

# Ejemplo con excepción

```python
try:
    print(x)

except NameError:
    print("Esta variable no ha sido definida.")

finally:
    print("Esto se ejecuta siempre.")
```

Resultado.

```text
Esta variable no ha sido definida.
Esto se ejecuta siempre.
```

---

# Ejemplo sin excepción

```python
x = 1

try:
    print(x)

except NameError:
    print("Esta variable no ha sido definida.")

finally:
    print("Esto se ejecuta siempre.")
```

Resultado.

```text
1
Esto se ejecuta siempre.
```

---

# Funcionamiento interno de `finally`

```text
Entrar en try

↓

Ejecutar código

↓

¿Hay excepción?
```

```text
No

↓

Continuar
```

```text
Sí

↓

Ejecutar except
```

↓

Ejecutar

```text
finally
```

↓

Continuar programa

El bloque `finally` representa el último paso del proceso.

---

# Flujo completo del manejo de excepciones

```text
try

↓

Código

↓

¿Error?
```

```text
No

↓

finally

↓

Continuar
```

```text
Sí

↓

except

↓

finally

↓

Continuar
```

---

# Múltiples excepciones

Una misma operación puede generar distintos tipos de errores.

Python permite manejar cada uno por separado.

```python
try:
    resultado = 10 / numero

except ZeroDivisionError:
    print("División por cero.")

except NameError:
    print("Variable inexistente.")
```

Cada bloque responde únicamente al tipo de excepción indicado.

---

# Capturar varias excepciones en un mismo bloque

También es posible agrupar varias excepciones.

```python
try:
    ...

except (TypeError, ValueError):
    print("Dato inválido.")
```

Este patrón es útil cuando diferentes excepciones requieren exactamente el mismo tratamiento.

---

# Capturar la excepción como objeto

La excepción puede almacenarse en una variable.

```python
try:
    resultado = 10 / 0

except ZeroDivisionError as error:
    print(error)
```

Resultado.

```text
division by zero
```

Esto permite registrar información útil para depuración o generación de registros (*logs*).

---

# La cláusula `else`

Existe otro bloque opcional poco conocido.

```python
else
```

Se ejecuta únicamente cuando **no ocurre ninguna excepción**.

```python
try:
    resultado = 10 / 2

except ZeroDivisionError:
    print("No se puede dividir.")

else:
    print("Resultado:", resultado)
```

Resultado.

```text
Resultado: 5.0
```

Aunque el curso no lo menciona, `else` forma parte de la estructura completa de manejo de excepciones y ayuda a separar el código exitoso del código de recuperación.

---

# ¿Cuándo utilizar `finally`?

El bloque `finally` suele emplearse para liberar recursos.

Ejemplos.

- cerrar archivos;
- cerrar conexiones a bases de datos;
- liberar sockets;
- cerrar conexiones HTTP;
- liberar memoria administrada por bibliotecas externas;
- registrar el final de una operación.

---

# AI Engineering

El manejo de excepciones es crítico en aplicaciones de IA.

| Caso | Posible excepción |
|------|-------------------|
| OpenAI SDK | Error de autenticación |
| APIs REST | Tiempo de espera agotado |
| Base de datos vectorial | Conexión fallida |
| Lectura de documentos | Archivo inexistente |
| Embeddings | Formato no válido |
| Automatización | Permisos insuficientes |

### Caso práctico

```python
try:
    respuesta = cliente.responses.create(
        model="gpt-5",
        input="Hola"
    )

except Exception:
    print("No fue posible comunicarse con el modelo.")
```

En producción, este tipo de manejo evita que una única llamada fallida detenga todo un sistema.

---

# Problemas reales en producción

## Problema 1

Capturar todas las excepciones indiscriminadamente.

```python
except:
    pass
```

Esto oculta errores importantes y dificulta enormemente el diagnóstico.

---

## Problema 2

Ignorar la excepción.

```python
except:
    pass
```

El programa continúa ejecutándose como si nada hubiera ocurrido.

Este patrón suele generar errores mucho más difíciles de detectar posteriormente.

---

## Problema 3

Utilizar excepciones para controlar el flujo normal del programa.

```python
try:
    ...

except:
    ...
```

Las excepciones deben representar situaciones excepcionales, no reemplazar estructuras de control como `if`.

---

## Problema 4

No registrar información del error.

```python
except ValueError:
    print("Error")
```

En aplicaciones reales es recomendable registrar el detalle de la excepción para facilitar la depuración.

---

# Buenas prácticas

- Captura únicamente las excepciones que realmente esperas.
- Evita utilizar `except:` sin especificar el tipo de excepción.
- Utiliza `finally` para liberar recursos importantes.
- Aprovecha `else` para separar el flujo exitoso del manejo de errores.
- Registra las excepciones en sistemas de *logging* en lugar de ocultarlas.
- No utilices excepciones como sustituto de validaciones normales.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`finally` sirve para mostrar un mensaje al final"

### Corrección técnica

Aunque puede utilizarse para imprimir mensajes, su propósito principal es **garantizar la ejecución de tareas de limpieza** (*cleanup*), como cerrar archivos, liberar conexiones o liberar recursos del sistema.

---

## Corrección 2. "Siempre conviene capturar cualquier excepción"

### Corrección técnica

No.

Capturar todas las excepciones indiscriminadamente puede ocultar errores graves del programa. Siempre que sea posible deben capturarse excepciones específicas como:

- `ZeroDivisionError`
- `NameError`
- `ValueError`
- `TypeError`

Esto hace que el código sea más seguro y fácil de mantener.

---

## Corrección 3. "El programa continúa exactamente donde ocurrió el error"

### Corrección técnica

No.

Cuando una excepción es capturada, Python abandona inmediatamente el resto del bloque `try` y transfiere el control al bloque `except` correspondiente. Las instrucciones restantes dentro del `try` ya no se ejecutan.

Ejemplo.

```python
try:
    print("Inicio")
    10 / 0
    print("Nunca se ejecuta")

except ZeroDivisionError:
    print("Error controlado")
```

Resultado.

```text
Inicio
Error controlado
```

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre un error de sintaxis y una excepción?

### Qué evalúa

Comprensión del modelo de ejecución de Python.

### Errores comunes

- Considerar que ambos conceptos son equivalentes.

### Respuesta de alto impacto

> Un error de sintaxis ocurre antes de ejecutar el programa e impide que el intérprete lo compile correctamente. Una excepción, en cambio, se produce durante la ejecución cuando ocurre una situación inesperada, como una división entre cero o el acceso a una variable inexistente. Las excepciones pueden capturarse con `try` y `except`; los errores de sintaxis no.

---

## Pregunta 2

¿Por qué es recomendable capturar excepciones específicas?

### Qué evalúa

Buenas prácticas de desarrollo.

### Errores comunes

- Utilizar siempre `except:` o `except Exception:` sin necesidad.

### Respuesta de alto impacto

> Porque capturar excepciones específicas hace explícita la intención del código y evita ocultar errores no previstos. Además, facilita la depuración y permite aplicar una estrategia distinta para cada tipo de problema.

---

## Pregunta 3

¿Para qué sirve realmente el bloque `finally`?

### Qué evalúa

Conocimiento del ciclo de vida de una excepción.

### Errores comunes

- Pensar que solo sirve para imprimir mensajes al finalizar.

### Respuesta de alto impacto

> `finally` garantiza la ejecución de un bloque de código independientemente de que ocurra una excepción o no. En aplicaciones profesionales se utiliza para liberar recursos críticos, como cerrar archivos, conexiones de bases de datos, sockets o sesiones de red, asegurando que el sistema quede en un estado consistente.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — Errors and Exceptions.
- Python Documentation — Built-in Exceptions.
- Python Documentation — The `try` Statement.

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 3134** — Exception Chaining and Embedded Tracebacks.
- **PEP 409** — Suppressing Exception Context.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.