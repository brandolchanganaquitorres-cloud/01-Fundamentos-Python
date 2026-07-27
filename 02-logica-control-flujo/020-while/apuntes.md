# Clase 20. El Bucle `while` en Python (`while`, `break`, `continue` y `else`)

> **Nivel:** Fundamentos de Python orientados a Ingeniería de Software y AI Engineering.
>
> **Dificultad:** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (10/10)
>
> **Objetivo:** Comprender el funcionamiento del bucle `while`, aprender a controlar su ejecución mediante una condición, utilizar correctamente `break`, `continue` y `else`, evitar bucles infinitos y aplicar estos conceptos en escenarios reales de desarrollo de software e Inteligencia Artificial.

---

# Contenido del curso

El **bucle `while`** ejecuta un bloque de código **mientras una condición sea verdadera**.

Es una estructura de repetición cuyo número de iteraciones **no tiene por qué conocerse previamente**.

Su funcionamiento depende de una condición booleana que se evalúa antes de cada iteración.

---

# Sintaxis básica

```python
while condicion:
    # código
```

Mientras la condición sea `True`, el bloque continuará ejecutándose.

Cuando pase a ser `False`, el bucle finalizará.

---

# Primer ejemplo

```python
i = 1

while i < 10:
    print(i)
    i += 1
```

Resultado:

```text
1
2
3
4
5
6
7
8
9
```

---

# Contando hasta 10

Modificando la condición.

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

Resultado.

```text
1
2
3
4
5
6
7
8
9
10
```

---

# Funcionamiento interno

Cada iteración sigue exactamente el mismo ciclo.

```text
Evaluar condición

↓

¿True?

↓

Ejecutar bloque

↓

Actualizar variables

↓

Volver a evaluar condición
```

Cuando la condición deja de cumplirse:

```text
↓

Salir del while
```

---

# La variable de control

La variable:

```python
i
```

es conocida como **variable de control** o **contador**.

Su función consiste en modificar el estado del programa para que la condición cambie con el tiempo.

---

# ¿Qué ocurre si no actualizamos el contador?

Ejemplo.

```python
i = 1

while i <= 10:
    print(i)
```

Resultado.

```text
1
1
1
1
1
...
```

El programa nunca termina.

Este fenómeno se conoce como:

> **Bucle infinito (Infinite Loop).**

---

# El orden de las instrucciones importa

Primer caso.

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

Resultado.

```text
1
2
3
...
10
```

---

Segundo caso.

```python
i = 1

while i <= 10:
    i += 1
    print(i)
```

Resultado.

```text
2
3
4
...
11
```

El cambio ocurre porque el incremento sucede antes de imprimir el valor.

---

# Ajustando el contador

Si queremos incrementar primero y seguir imprimiendo del 1 al 10.

```python
i = 0

while i < 10:
    i += 1
    print(i)
```

Resultado.

```text
1
2
3
...
10
```

---

# La sentencia `break`

`break` finaliza inmediatamente el bucle.

Ejemplo.

```python
i = 1

while i <= 10:
    print(i)

    if i == 5:
        break

    i += 1
```

Resultado.

```text
1
2
3
4
5
```

Cuando Python ejecuta `break`, abandona el `while` sin seguir evaluando la condición.

---

# Funcionamiento interno de `break`

```text
Inicio iteración

↓

Evaluar condición

↓

Ejecutar bloque

↓

¿Aparece break?

↓

Sí

↓

Salir inmediatamente del while
```

---

# Cambiando el orden

```python
i = 1

while i <= 10:

    if i == 5:
        break

    print(i)

    i += 1
```

Resultado.

```text
1
2
3
4
```

El número cinco no se imprime porque el `break` ocurre antes del `print()`.

---

# La sentencia `continue`

`continue` no finaliza el bucle.

Simplemente **omite el resto de la iteración actual** y continúa con la siguiente.

Ejemplo.

```python
i = 0

while i < 10:

    i += 1

    if i == 5:
        continue

    print(i)
```

Resultado.

```text
1
2
3
4
6
7
8
9
10
```

El número cinco se omite, pero el bucle continúa normalmente.

---

# Funcionamiento interno de `continue`

```text
Inicio iteración

↓

Actualizar contador

↓

¿Condición especial?

↓

Sí

↓

continue

↓

Saltar al inicio del while
```

Todo el código restante de esa iteración queda sin ejecutarse.

---

# Un error muy común

```python
i = 1

while i <= 10:

    if i == 5:
        continue

    print(i)

    i += 1
```

Cuando:

```python
i == 5
```

se ejecuta:

```python
continue
```

pero nunca ocurre:

```python
i += 1
```

El contador permanece en cinco para siempre.

Resultado.

```text
Bucle infinito
```

---

# Expansión técnica

Este es uno de los errores más frecuentes durante las primeras semanas aprendiendo Python.

Siempre que utilices `continue`, verifica que **las variables que controlan el bucle ya hayan sido actualizadas** antes de ejecutar la instrucción.

---

# Incrementos diferentes

No es obligatorio incrementar de uno en uno.

```python
i = 0

while i <= 10:
    i += 2
    print(i)
```

Resultado.

```text
2
4
6
8
10
```

Como únicamente aparecen números pares, nunca se alcanzará:

```python
i == 5
```

---

# La cláusula `else` del `while`

Una característica poco conocida de Python es que los bucles también pueden tener un bloque `else`.

```python
i = 0

while i < 10:

    i += 1

    print(i)

else:
    print("El bucle terminó")
```

Resultado.

```text
1
2
3
...
10
El bucle terminó
```

---

# ¿Cuándo se ejecuta el `else`?

El bloque `else` se ejecuta **únicamente cuando el bucle termina de forma natural**, es decir, cuando la condición deja de ser verdadera.

```text
Condición

↓

False

↓

Ejecutar else
```

---

# ¿Cuándo NO se ejecuta?

Si el bucle termina mediante `break`.

```python
i = 1

while i <= 10:

    if i == 5:
        break

    i += 1

else:
    print("Finalizó")
```

Resultado.

```text
(No se ejecuta el else)
```

Porque el bucle no terminó por la condición, sino por una interrupción explícita.

---

# AI Engineering

Los bucles `while` aparecen frecuentemente en sistemas de IA y automatización.

| Caso | Uso |
|------|-----|
| APIs | Reintentar solicitudes hasta obtener una respuesta válida |
| Agentes | Esperar nuevas tareas mientras el sistema permanezca activo |
| Chatbots | Mantener la conversación hasta recibir una orden de salida |
| Automatización | Procesar elementos mientras existan trabajos pendientes |
| Streaming | Leer datos continuamente hasta cerrar la conexión |

### Caso práctico

Reintentar una llamada a un modelo de lenguaje.

```python
respuesta = None
intentos = 0

while respuesta is None and intentos < 3:
    respuesta = llamar_llm()
    intentos += 1
```

Este patrón es habitual cuando una API puede fallar temporalmente y se desea implementar una política de reintentos.

---

# Problemas reales en producción

## Problema 1

Olvidar actualizar la variable de control.

```python
while activo:
```

Si `activo` nunca cambia:

```text
Bucle infinito
```

---

## Problema 2

Utilizar `continue` antes de modificar el contador.

```python
if i == 5:
    continue
```

Produce un bucle infinito cuando la condición depende de esa misma variable.

---

## Problema 3

Esperar que `else` se ejecute después de un `break`.

```python
while True:
    break
else:
    print("Fin")
```

El bloque `else` nunca se ejecutará.

---

## Problema 4

Modificar la condición dentro del cuerpo del bucle sin comprender su efecto.

```python
while contador < limite:
```

Si `limite` cambia durante la ejecución, el número de iteraciones también cambiará, pudiendo generar comportamientos inesperados.

---

# Buenas prácticas

- Define claramente la condición de salida antes de escribir el bucle.
- Actualiza siempre la variable de control en cada iteración.
- Utiliza `break` únicamente cuando exista una condición clara para terminar el proceso.
- Coloca el incremento antes de `continue` cuando el contador controle el bucle.
- Usa `else` únicamente cuando necesites distinguir entre una finalización natural y una terminación mediante `break`.

---

# Errores conceptuales detectados en el curso

## Corrección 1. "`continue` salta la siguiente iteración"

### Corrección técnica

`continue` **no salta una iteración futura**. Finaliza inmediatamente la iteración **actual** y devuelve el control al inicio del bucle para evaluar nuevamente la condición.

---

## Corrección 2. "`else` se ejecuta cuando termina el while"

### Corrección técnica

Más precisamente, `else` solo se ejecuta cuando el `while` finaliza **porque la condición se volvió falsa**. Si el bucle termina mediante `break`, el bloque `else` se omite.

---

## Corrección 3. "Todos los bucles `while` utilizan un contador"

### Corrección técnica

No necesariamente. Muchos `while` en producción dependen del estado de un recurso o de un evento externo, no de un contador.

Ejemplo.

```python
while conexion_activa:
    procesar_mensajes()
```

Aquí la condición depende del estado de la conexión, no de un número.

---

# Preguntas técnicas de entrevista

## Pregunta 1

¿Cuál es la diferencia entre `break` y `continue`?

### Qué evalúa

Comprensión del flujo de ejecución.

### Errores comunes

- Pensar que ambos finalizan el bucle.

### Respuesta de alto impacto

> `break` termina inmediatamente el bucle y continúa con la primera instrucción posterior al `while`. En cambio, `continue` solo interrumpe la iteración actual y vuelve al inicio del bucle para evaluar nuevamente la condición.

---

## Pregunta 2

¿Cuándo se ejecuta el bloque `else` de un `while`?

### Qué evalúa

Conocimiento de una característica específica de Python.

### Errores comunes

- Creer que siempre se ejecuta al finalizar el bucle.

### Respuesta de alto impacto

> El bloque `else` solo se ejecuta cuando el `while` termina de forma natural porque la condición deja de cumplirse. Si la salida ocurre mediante `break`, el bloque `else` no se ejecuta.

---

## Pregunta 3

¿Cuál es la causa más frecuente de un bucle infinito?

### Qué evalúa

Capacidad para identificar errores comunes.

### Errores comunes

- Pensar únicamente en una condición mal escrita.

### Respuesta de alto impacto

> La causa más habitual es que la condición del bucle nunca cambia porque la variable de control no se actualiza o porque un `continue` impide dicha actualización. Antes de escribir un `while`, siempre verifico cuál será el mecanismo que garantizará su finalización.

---

# Recursos recomendados

## Documentación oficial

- Python Documentation — The `while` Statement.
- Python Documentation — `break` and `continue`.
- Python Documentation — Compound Statements.

## PEPs

- **PEP 8** — Style Guide for Python Code.

## Libros

- *Fluent Python* — Luciano Ramalho.
- *Effective Python* — Brett Slatkin.
- *Python Cookbook* — David Beazley y Brian K. Jones.