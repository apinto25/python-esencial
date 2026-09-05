# Ejercicio 1: Paquetes y ambientes virtuales

Este ejercicio es práctico, en la terminal, no un archivo `.py`.

1. Crea un ambiente virtual nuevo llamado `mi_entorno`.
2. Actívalo.
3. Instala el paquete `requests` usando `pip`.
4. Genera un archivo `requirements.txt` con las dependencias instaladas
   (`pip freeze > requirements.txt`) dentro de esta misma carpeta.
5. Desactiva el ambiente virtual.

Comandos que necesitarás (macOS/Linux):

```bash
python3 -m venv mi_entorno
source mi_entorno/bin/activate
pip install requests
pip freeze > requirements.txt
deactivate
```

En Windows, reemplaza el paso de activación por:

```bash
mi_entorno\Scripts\activate
```
