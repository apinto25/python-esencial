def mostrar_capital(pais, capital):
    print(f"La capital de {pais} es {capital}")


mostrar_capital(pais="Colombia", capital="Bogotá")


def describir_ciudad(ciudad, poblacion):
    es_grande = poblacion > 5000000
    return f"{ciudad} tiene una población de {poblacion} habitantes", es_grande


descripcion, es_grande = describir_ciudad("Bogotá", 8000000)
print(descripcion, es_grande)

def describir_ciudad(ciudad, poblacion):
    return f"{ciudad} tiene una población de {poblacion} habitantes"
