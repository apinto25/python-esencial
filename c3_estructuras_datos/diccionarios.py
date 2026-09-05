ciudad = {"nombre": "Bogota", "departamento": "Cundinamarca"}
print(ciudad)
print(ciudad["nombre"])

ciudad["poblacion"] = 8000000
print(ciudad)

ciudad["poblacion"] = 7000000
print(ciudad)

ciudad["lugares_turisticos"] = ["Monserrate"]
print(ciudad)

print(ciudad.keys())
print(ciudad.values())
print(ciudad.items())
