bogota = 8000000
medellin = 8000000

if bogota > medellin:
    print("Bogotá tiene mas población que Medellín")
elif bogota == medellin:
    print("Bogotá y Medellín tienen la misma población")
else:
    print("Medellín tiene mas población que Bogotá")

es_capital = True
if es_capital and bogota > 5000000:
    print("Es una ciudad capital")
else:
    print("No es una ciudad capital")
