class Ciudad:
    pais = "Colombia"

    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = poblacion

    def actualizar_poblacion(self, nueva_poblacion):
        self.poblacion = nueva_poblacion
        print(f"{self.nombre} tiene una población de {self.poblacion}")


class Capital(Ciudad):

    def __init__(self, nombre, poblacion, pais):
        super().__init__(nombre, poblacion)
        self.pais = pais

    def es_capital(self):
        print(f"{self.nombre} es capital de {self.pais}")


bogota = Capital("Bogotá", 8000000, "Colombia")
bogota.actualizar_poblacion(nueva_poblacion=9000000)
bogota.es_capital()
