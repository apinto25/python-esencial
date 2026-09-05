def calcular_promedio(poblaciones):
    return sum(poblaciones)/len(poblaciones)

try:
    promedio = calcular_promedio(["a"])
    print(promedio)
except ZeroDivisionError:
    print("La lista población está vacía")
except Exception as error:
    print("No es posible calcular el promedio")
    print("Detalle:", error)
