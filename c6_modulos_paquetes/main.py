from geografia.ciudades import describir_ciudad
from geografia.departamentos import describir_departamento

descripcion = describir_ciudad(ciudad="Bogotá", poblacion=8000000)
print(descripcion)

descripcion_departamento = describir_departamento("Cundinamarca", "Bogotá")
print(descripcion_departamento)
