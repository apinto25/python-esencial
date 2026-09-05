ciudad = {
    "nombre": "Bogotá",
    "departamento": "Cundinamarca"
}
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla"]

for indice in range(len(ciudades)):
    print(indice, ciudades[indice])

indice = 0
while indice < len(ciudades):
    print(indice, ciudades[indice])
    indice += 1

for llave, valor in ciudad.items():
    print(llave, valor)
