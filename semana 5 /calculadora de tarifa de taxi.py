hora=int(input("ingrese la hora de inicio del viaje (0-23):"))
km=float(input("ingrese la distancia del viaje en km:"))
costo=5000
print("costo base del viaje: $", costo)
#Recargo nocturno
if hora >=21 or hora <=5:
    recargo=costo * 0.30
    costo=costo + recargo
    print("Recargo nocturno aplicando: $", recargo)
#Kilometro adicionales 
if km > 10:
    km_extra = km - 10
    costo_extra = km_extra * 800
    costo = costo + costo_extra
    print("kilometro adicionales:", km_extra)
    print("costo por km extra: $", costo_extra)
print("total a pagar: $", costo)
