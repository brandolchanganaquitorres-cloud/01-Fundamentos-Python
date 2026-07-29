# Clase 31. Proyecto Integrador: Máquina de Café en Python (Arquitectura Modular)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Aplicar los conceptos aprendidos sobre funciones, módulos, condicionales, bucles, diccionarios, entrada de datos y organización de proyectos para desarrollar una aplicación modular desde la terminal siguiendo prácticas similares a las utilizadas en proyectos profesionales.

---

# Contenido del curso

Hasta este punto del curso ya conoces:

- Variables
- Funciones
- Condicionales
- Bucles
- Diccionarios
- Módulos
- Manejo de archivos

Ahora todos esos conceptos se integran en un único proyecto.

La aplicación consiste en una **Máquina de Café** ejecutada desde la terminal.

El objetivo no es únicamente preparar cafés, sino aprender cómo se organiza un proyecto Python real.

---

# Arquitectura del proyecto

El curso propone dividir la aplicación en varios archivos.

```text
maquina_cafe/

│

├── main.py

├── menu.py

└── pedidos.py
```

Cada archivo tiene una responsabilidad específica.

| Archivo | Responsabilidad |
|----------|-----------------|
| `main.py` | Controlar el flujo principal de la aplicación |
| `menu.py` | Mostrar el menú al usuario |
| `pedidos.py` | Gestionar la selección de cafés |

Esta separación representa uno de los principios más importantes de la Ingeniería de Software:

> **Cada módulo debe tener una única responsabilidad.**

---

# `main.py`

Por convención, el archivo principal de una aplicación Python suele llamarse:

```text
main.py
```

Desde este archivo comienza toda la ejecución.

---

# La función `main()`

Dentro del archivo principal se define una función.

```python
def main():
    pass
```

Posteriormente toda la lógica del programa se incorpora dentro de esta función.

---

# ¿Por qué crear una función `main()`?

Sin función.

```python
print(...)
...

if ...

while ...

...
```

Todo el código queda mezclado en el nivel superior del archivo.

Con una función principal.

```python
def main():
    ...
```

Toda la lógica queda agrupada y organizada.

Esto facilita:

- mantenimiento;
- reutilización;
- pruebas;
- comprensión del flujo principal.

---

# El bucle principal

Dentro de `main()` aparece el siguiente patrón.

```python
while True:
    ...
```

A primera vista parece un ciclo infinito.

Sin embargo, el propio programa decide cuándo finalizar.

---

# Funcionamiento interno

```text
Iniciar programa

↓

Entrar al while

↓

Mostrar menú

↓

Esperar opción

↓

Procesar

↓

¿Salir?

↓

No

↓

Repetir
```

Cuando el usuario decide salir.

```text
↓

break

↓

Finalizar programa
```

---

# ¿Por qué utilizar `while True`?

En un menú interactivo no sabemos cuántas operaciones realizará el usuario.

Puede pedir:

- un café;
- cinco cafés;
- consultar el historial;
- salir inmediatamente.

Por ello se utiliza un ciclo que continúa hasta recibir la orden de salida.

---

# Capturar la opción del usuario

La entrada se obtiene mediante:

```python
opcion = input("Seleccione una opción: ")
```

---

# Expansión técnica

`input()` **siempre devuelve una cadena de texto (`str`)**, independientemente de lo que escriba el usuario.

Ejemplo.

Usuario escribe.

```text
1
```

Python almacena.

```python
"1"
```

No almacena.

```python
1
```

Por esta razón las comparaciones deben realizarse utilizando cadenas.

```python
if opcion == "1":
```

No.

```python
if opcion == 1:
```

---

# Flujo del menú

El programa evalúa la opción mediante condicionales.

```text
Usuario

↓

input()

↓

opcion

↓

if

↓

elif

↓

else
```

---

# Opciones disponibles

## Opción 1

```text
Pedir café
```

---

## Opción 2

```text
Ver historial
```

---

## Opción 3

```text
Salir
```

Cuando el usuario selecciona esta opción.

```python
break
```

interrumpe el ciclo.

---

## Opción inválida

Cualquier otro valor produce.

```text
Opción inválida
```

Posteriormente el programa vuelve al menú principal.

---

# Utilizar `pass`

Mientras una funcionalidad aún no está implementada.

```python
if opcion == "1":
    pass
```

`pass` permite construir el esqueleto del programa sin producir errores de sintaxis.

Este enfoque es habitual durante las primeras etapas del desarrollo.

---

# `if __name__ == "__main__"`

Al final del archivo principal aparece una de las líneas más importantes de Python.

```python
if __name__ == "__main__":
    main()
```

---

# ¿Qué significa?

Cada módulo posee una variable especial.

```python
__name__
```

Su valor depende de cómo se utilice el archivo.

---

## Cuando ejecutamos directamente

```text
python main.py
```

Entonces.

```python
__name__
```

vale.

```python
"__main__"
```

La condición es verdadera.

```text
main()

↓

Programa inicia
```

---

## Cuando importamos el archivo

```python
import main
```

Ahora.

```python
__name__
```

vale aproximadamente.

```python
"main"
```

La condición es falsa.

La función principal no se ejecuta automáticamente.

---

# Funcionamiento interno

```text
Ejecutar archivo

↓

¿Es el archivo principal?
```

```text
Sí

↓

main()
```

```text
No

↓

No ejecutar
```

Este mecanismo evita que un módulo comience a ejecutarse accidentalmente cuando solo queremos importar sus funciones.

---

# Separar el menú en un módulo

El curso propone crear.

```text
menu.py
```

Su responsabilidad consiste únicamente en mostrar el menú.

```python
def mostrar_menu():
    print(...)
```

---

# Importar el menú

Desde `main.py`.

```python
from menu import mostrar_menu
```

Posteriormente.

```python
mostrar_menu()
```

---

# ¿Por qué separar el menú?

Sin módulos.

```text
main.py

↓

Mostrar menú

↓

Procesar pedido

↓

Leer archivo

↓

Guardar pedido

↓

...
```

Con módulos.

```text
main.py

↓

mostrar_menu()

↓

pedir_cafe()

↓

ver_historial()
```

El código resulta considerablemente más limpio.

---

# El módulo `pedidos.py`

La lógica relacionada con la selección de cafés se mueve a otro archivo.

```text
pedidos.py
```

Su función principal es.

```python
def pedir_cafe():
    ...
```

---

# Utilizar un diccionario

Las opciones disponibles se almacenan en un diccionario.

```python
cafes = {
    "1": "Expreso",
    "2": "Cappuccino",
    "3": "Latte",
    "4": "Americano"
}
```

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

Cada nuevo café implica añadir otro bloque `if`.

Con diccionario.

```python
cafes[opcion]
```

El acceso es inmediato.

---

# Funcionamiento interno

```text
Usuario escribe

↓

"2"

↓

Diccionario

↓

Buscar clave

↓

"Cappuccino"
```

La búsqueda se realiza mediante una tabla hash, por lo que el acceso promedio es de complejidad **O(1)**.

---

# Escalabilidad

Agregar nuevos cafés únicamente requiere incorporar una nueva entrada.

```python
cafes["5"] = "Mocha"

cafes["6"] = "Macchiato"

cafes["7"] = "Flat White"
```

La lógica del programa permanece exactamente igual.

---

# Flujo completo del proyecto

```text
Usuario

↓

main.py

↓

mostrar_menu()

↓

input()

↓

if

↓

pedir_cafe()

↓

Diccionario

↓

Resultado
```

---

# Arquitectura del proyecto

Aunque este ejemplo es pequeño, representa la misma filosofía utilizada en proyectos empresariales.

```text
Aplicación

│

├── main.py

├── menu.py

├── pedidos.py

├── historial.py

├── configuracion.py

├── utilidades.py

└── archivos.py
```

Cada módulo tiene una responsabilidad concreta.

---

# AI Engineering

La organización modular es indispensable en proyectos de IA.

Una arquitectura típica puede ser.

```text
Proyecto IA

│

├── main.py

├── prompts.py

├── llm.py

├── embeddings.py

├── rag.py

├── agentes.py

├── herramientas.py

├── memoria.py

├── configuracion.py

└── utilidades.py
```

Cada componente puede evolucionar de forma independiente sin afectar al resto del sistema.

### Caso práctico

```python
from llm import generar_respuesta
from rag import recuperar_documentos
from memoria import guardar_historial

def main():
    ...
```

Esta estructura facilita las pruebas, el mantenimiento y la escalabilidad de aplicaciones basadas en modelos de lenguaje.

---

# Problemas reales en producción

## Problema 1

Crear un único archivo enorme.

```text
main.py

↓

12000 líneas
```

Esto dificulta el mantenimiento y la colaboración entre desarrolladores.

---

## Problema 2

Duplicar lógica.

```python
if opcion == "1":
    ...

...

if opcion == "1":
    ...
```

La lógica repetida incrementa el riesgo de inconsistencias y errores.

---

## Problema 3

Comparar `input()` con enteros.

```python
if opcion == 1:
```

Nunca será verdadero.

Debe utilizarse.

```python
if opcion == "1":
```

---

## Problema 4

Utilizar múltiples `if` cuando un diccionario resuelve el problema.

```python
if ...

elif ...

elif ...

elif ...
```

Cuando la decisión consiste únicamente en asociar una clave con un valor, un diccionario suele ser una solución más simple y escalable.

---

## Problema 5

No validar la entrada del usuario.

```python
cafes[opcion]
```

Si la clave no existe, Python generará un `KeyError`.

En aplicaciones reales es recomendable validar previamente la existencia de la clave o utilizar `dict.get()` para evitar excepciones inesperadas.

---

# Buenas prácticas

- Organiza el proyecto en módulos con responsabilidades bien definidas.
- Mantén `main.py` como punto de entrada y coordinador del flujo.
- Utiliza `if __name__ == "__main__":` para evitar ejecuciones accidentales al importar módulos.
- Aprovecha diccionarios para representar catálogos o menús en lugar de largas cadenas de `if` y `elif`.
- Valida siempre la entrada del usuario antes de utilizarla.
- Implementa funciones pequeñas y reutilizables en lugar de concentrar toda la lógica en un único archivo.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`while True` crea un bucle infinito"

### Corrección técnica

`while True` define un ciclo cuya condición es siempre verdadera, pero no implica necesariamente un bucle infinito. El flujo puede finalizar mediante instrucciones como `break`, `return`, una excepción no controlada o incluso la finalización del proceso. En menús interactivos, `break` es el mecanismo habitual para salir del ciclo.

---

## Corrección 2. "`from menu import mostrar_menu` importa solo esa función"

### Corrección técnica

Conceptualmente es correcto, pero internamente Python **carga y ejecuta el módulo completo** la primera vez que se importa. Posteriormente expone únicamente el nombre `mostrar_menu` en el espacio de nombres actual. No se carga únicamente la función de forma aislada.

---

## Corrección 3. "El diccionario evita escribir cuatro `if`"

### Corrección técnica

Más importante aún, un diccionario transforma una secuencia de comparaciones en una búsqueda por clave basada en una tabla hash. Esto hace que el código sea más declarativo, más fácil de extender y, en promedio, más eficiente para recuperar valores.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Por qué es recomendable encapsular el flujo principal dentro de una función `main()`?

### Qué evalúa

Conocimientos sobre organización de aplicaciones.

### Errores comunes

- Responder únicamente que "porque se ve más ordenado".

### Respuesta de alto impacto

> Encapsular el flujo principal en `main()` mejora la modularidad, facilita las pruebas unitarias, evita ejecutar lógica en el nivel superior del módulo y hace que el punto de entrada de la aplicación sea explícito. Además, combinado con `if __name__ == "__main__":`, permite reutilizar el módulo sin ejecutar automáticamente el programa.

---

## Pregunta 2

¿Qué hace realmente `if __name__ == "__main__":`?

### Qué evalúa

Comprensión del sistema de módulos de Python.

### Errores comunes

- Pensar que es obligatorio para que el programa funcione.

### Respuesta de alto impacto

> La variable especial `__name__` toma el valor `"__main__"` cuando el archivo se ejecuta directamente. Si el archivo se importa desde otro módulo, `__name__` contiene el nombre del módulo. Esta condición permite diferenciar ambos escenarios y evita que el código principal se ejecute de forma accidental durante una importación.

---

## Pregunta 3

¿Por qué un diccionario suele ser mejor que una larga cadena de `if` y `elif` para representar un menú?

### Qué evalúa

Capacidad para seleccionar estructuras de datos adecuadas.

### Errores comunes

- Responder únicamente que "es más corto".

### Respuesta de alto impacto

> Un diccionario expresa directamente la relación entre una opción y su resultado mediante pares clave-valor. Esto elimina comparaciones repetitivas, facilita la incorporación de nuevas opciones y aprovecha búsquedas promedio de complejidad O(1) gracias a la implementación basada en tablas hash.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — `input()`.
- Python Documentation — The `__main__` Module.
- Python Documentation — Modules.
- Python Documentation — Mapping Types (`dict`).

## PEPs

- **PEP 8** — Style Guide for Python Code.
- **PEP 20** — The Zen of Python.
- **PEP 328** — Imports: Multi-Line and Absolute/Relative Imports.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Architecture Patterns with Python* — Harry Percival y Bob Gregory.