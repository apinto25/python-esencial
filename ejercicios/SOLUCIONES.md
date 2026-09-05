# Soluciones

Estas son soluciones de referencia para los ejercicios de la carpeta [`ejercicios/`](.). Hay más de una forma correcta de resolver cada ejercicio: esta es solo una posible solución.

Intenta resolver el ejercicio por tu cuenta antes de mirar la solución.

## c2_conceptos

### ejercicio_1_variables.py

```python
nombre = "Ana"
edad = 30
ciudad = "Bogotá"

print(f"Hola, me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")
```

### ejercicio_2_operaciones.py

```python
precio = 25000
cantidad = 3

total = precio * cantidad
total_descuento = total * 0.9

print(f"Total a pagar: {total}")
print(f"Total con descuento: {total_descuento}")
```

## c3_estructuras_datos

### ejercicio_1_listas.py

```python
frutas = ["pera", "banano", "uva", "mango", "fresa"]

frutas.append("kiwi")
frutas.pop(0)

frutas_ordenadas = sorted(frutas)
cantidad_frutas = len(frutas)

print(frutas_ordenadas)
print(cantidad_frutas)
```

### ejercicio_2_diccionarios.py

```python
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Bogotá"}

print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Ciudad: {persona['ciudad']}")

persona["profesion"] = "Ingeniera"
persona["edad"] = persona["edad"] + 1

print(persona)
```

## c4_condiciones_ciclos

### ejercicio_1_condiciones.py

```python
edad = 15

if edad < 2:
    print("Es un bebé")
elif edad <= 12:
    print("Es un niño")
elif edad <= 17:
    print("Es un adolescente")
else:
    print("Es un adulto")
```

### ejercicio_2_ciclos.py

```python
nombres = ["ana", "luis", "carla", "pedro"]

for numero in range(1, 21):
    if numero % 3 == 0:
        print(numero)

suma_total = 0
n = 1
while n <= 10:
    suma_total += n
    n += 1
print(suma_total)

for nombre in nombres:
    print(nombre.upper())
```

## c5_funciones

### ejercicio_1_funciones.py

```python
def es_par(numero):
    return numero % 2 == 0


def saludar(nombre, idioma):
    if idioma == "es":
        return f"Hola, {nombre}!"
    elif idioma == "en":
        return f"Hello, {nombre}!"
    else:
        return "Idioma no soportado"


print(es_par(4))
print(es_par(7))
print(saludar("Ana", "es"))
print(saludar("Ana", "en"))
print(saludar("Ana", "fr"))
```

## c6_modulos_paquetes

### conversiones.py (archivo nuevo que crea el ejercicio)

```python
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
```

### ejercicio_1_modulos.py

```python
import conversiones

print(conversiones.celsius_a_fahrenheit(0))
print(conversiones.celsius_a_fahrenheit(100))
print(conversiones.fahrenheit_a_celsius(32))
print(conversiones.fahrenheit_a_celsius(212))
```

## c7_paquetes_ambientes

### ejercicio_1_ambiente_virtual.md

```bash
python3 -m venv mi_entorno
source mi_entorno/bin/activate
pip install requests
pip freeze > requirements.txt
deactivate
```

Al final, `requirements.txt` debe contener una línea similar a `requests==2.31.0`.

## c8_clases

### ejercicio_1_clases.py

```python
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"{self.nombre} hace {self.sonido}")


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Guau")


mi_perro = Perro("Rex")
mi_perro.hacer_sonido()
```

## c9_errores_excepciones

### ejercicio_1_try_except.py

```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    except TypeError:
        print("Ambos valores deben ser números.")


print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "a"))
```
