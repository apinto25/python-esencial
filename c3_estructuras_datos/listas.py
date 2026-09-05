ciudades = ["Bogota", "Medellin", "Cali"]

print(ciudades[0])
print(ciudades[-1])
print(len(ciudades))

ciudades[0] = "Popayan"
print(ciudades)

ciudades.append("Bucaramanga")
print(ciudades)

otras_ciudades = ["Cartagena", "Manizales"]
ciudades.extend(otras_ciudades)
print(ciudades)

ciudades.pop(2)
print(ciudades)
