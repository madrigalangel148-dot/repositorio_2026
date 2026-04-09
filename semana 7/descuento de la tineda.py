# pedir datos 
es_estudiante=input("¿eres estudiante?(si/no):").lower()
total=float(input("total de tu compra en pesos:"))
# condicion con OR
if es_estudiante=="si" or total >200000:
    descuento=total *0.15
    total_final=total-descuento
    print("¡descuentos aplicando del 15%!")
    print("descuento: $", descuento)
    print("total a pagar: $", total_final)
else:
    print("sin descuento. total: $", total)
