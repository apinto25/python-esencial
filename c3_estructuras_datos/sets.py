departamentos = {"Antioquia", "Valle del Cauca"}
print(departamentos)

# Error por acceder a elemento de un set a través de un índice
# departamentos[0]

numeros = {1, 2, 3, 1}
print(numeros)

departamentos.add("Santander")
print(departamentos)

departamentos.update(["Narino", "Boyaca"])
print(departamentos)

departamentos.discard("Cundinamarca")
print(departamentos)

# Error por usar remove con un elemento que no existe en el set
# departamentos.remove("Cundinamarca")

departamentos.remove("Boyaca")
print(departamentos)

