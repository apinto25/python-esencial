# Python esencial

A lo largo de este curso escribimos código en Python que queda disponible en este repositorio de GitHub.

Cada módulo del curso tiene su propia carpeta dentro del repositorio (`cN_...`), y dentro de cada carpeta vas a encontrar un archivo por cada video de ese módulo, con el código que trabajamos en el video correspondiente. Además, algunos módulos cuentan con una sección de ejercicios, donde vas a encontrar ejercicios para practicar por tu cuenta lo que hayamos visto y así reforzar lo aprendido antes de pasar al siguiente módulo.

## Contenido del curso

### 0. Introducción
- Iniciando con Python
- Recursos del curso

### 1. Qué es Python
- Qué puede hacer Python por ti
- Instalación de Python
- Línea de comandos de Python
- Editores de texto para Python

### 2. Conceptos básicos de Python — [`c2_conceptos/`](c2_conceptos/)
- Primer programa en Python: "Hello World!" → [`hello_world.py`](c2_conceptos/hello_world.py)
- Comentarios en Python → [`comentarios.py`](c2_conceptos/comentarios.py)
- Variables en Python → [`variables.py`](c2_conceptos/variables.py)
- Operaciones básicas en Python → [`operaciones.py`](c2_conceptos/operaciones.py)
- Indentación en Python → [`indentacion.py`](c2_conceptos/indentacion.py)

### 3. Estructuras de datos — [`c3_estructuras_datos/`](c3_estructuras_datos/)
- Qué son las estructuras de datos
- Listas en Python → [`listas.py`](c3_estructuras_datos/listas.py)
- Tuplas en Python → [`tuplas.py`](c3_estructuras_datos/tuplas.py)
- Diccionarios en Python → [`diccionarios.py`](c3_estructuras_datos/diccionarios.py)
- Sets en Python → [`sets.py`](c3_estructuras_datos/sets.py)

### 4. Condiciones y ciclos — [`c4_condiciones_ciclos/`](c4_condiciones_ciclos/)
- Qué son las condiciones
- Condiciones (if) en Python → [`condicion.py`](c4_condiciones_ciclos/condicion.py)
- Qué son los ciclos
- Ciclos for en Python → [`ciclo_for.py`](c4_condiciones_ciclos/ciclo_for.py)
- Ciclos while en Python → [`ciclo_while.py`](c4_condiciones_ciclos/ciclo_while.py)
- Iterando sobre estructuras de datos en Python → [`ciclo_estructura_datos.py`](c4_condiciones_ciclos/ciclo_estructura_datos.py)

### 5. Funciones — [`c5_funciones/`](c5_funciones/)
- Introducción a las funciones en Python
- Primera función en Python
- Argumentos y parámetros en las funciones de Python
- Retorno de valores en una función de Python
- → [`funciones.py`](c5_funciones/funciones.py)

### 6. Módulos — [`c6_modulos_paquetes/`](c6_modulos_paquetes/)
- Módulos y paquetes en Python
- Creando el primer módulo en Python → [`main.py`](c6_modulos_paquetes/main.py)
- Creando un paquete en Python → [`geografia/`](c6_modulos_paquetes/geografia/)

### 7. Paquetes y ambientes virtuales — [`c7_paquetes_ambientes/`](c7_paquetes_ambientes/)
- Paquetes de Python y pip
- Ambientes virtuales con venv para Python
- Archivo de requerimientos para Python → [`requirements.txt`](c7_paquetes_ambientes/requirements.txt)

### 8. Programación orientada a objetos — [`c8_clases/`](c8_clases/)
- Introducción a la programación orientada a objetos en Python
- Clases e instancias en Python
- Constructor y atributos de una clase en Python
- Métodos de una clase en Python
- Herencia de clases en Python
- → [`clases.py`](c8_clases/clases.py)

### 9. Errores y excepciones — [`c9_errores_excepciones/`](c9_errores_excepciones/)
- Errores de sintaxis en Python → [`errores_excepciones.py`](c9_errores_excepciones/errores_excepciones.py)
- Try - Except para el manejo de excepciones en Python → [`try_except.py`](c9_errores_excepciones/try_except.py)

## Cómo descargar el repositorio

Para tener el repositorio en tu computador tienes dos opciones:

**Opción 1: clonarlo con Git**, si ya tienes experiencia con esta herramienta:

```bash
git clone https://github.com/<tu-usuario>/python-esencial.git
cd python-esencial
```

**Opción 2: descargarlo como archivo comprimido**, si no usas Git: en la página del repositorio, busca el botón verde que dice **Code** y selecciona **Download ZIP**. Luego descomprime el archivo en tu equipo.

## Requisitos previos

- Tener [Python 3](https://www.python.org/downloads/) instalado (versión 3.10 o superior recomendada).
- Verifica la instalación con:

```bash
python3 --version
```

## Cómo ejecutar el código

Cada capítulo contiene archivos `.py` independientes que puedes ejecutar directamente:

```bash
python3 c2_conceptos/hello_world.py
```

Cambia la ruta del archivo según el capítulo y el ejemplo que quieras probar.

### Capítulo 7: ambiente virtual y dependencias

El capítulo 7 muestra cómo crear un ambiente virtual e instalar paquetes con `pip`. Para replicarlo:

```bash
# Crear el ambiente virtual
python3 -m venv venv

# Activar el ambiente virtual
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# Instalar las dependencias del curso
pip install -r c7_paquetes_ambientes/requirements.txt
```

## Autor

[Ana Maria Pinto](https://www.linkedin.com/in/ana-maria-pinto-v/)
