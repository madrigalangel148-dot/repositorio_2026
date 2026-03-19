# Entradas
membresia = input("Ingrese tipo de membresía (regular/silver/gold): ").lower()
compra = int(input("Ingrese el valor de la compra: "))
rebajas = input("¿Es temporada de rebajas? (True/False): ")

# Convertir a booleano
if rebajas == "True":
    rebajas = True
else:
    rebajas = False

# Variables
descuento = 0
envio_gratis = False

# Lógica de membresía
if membresia == "regular":
    descuento = 0

elif membresia == "silver":
    if compra > 50000:
        descuento = 10

elif membresia == "gold":
    descuento = 20
    if compra > 100000:
        envio_gratis = True

else:
    print("Membresía no válida")

# Aumentar descuento por rebajas
if rebajas:
    descuento += 5

# Calcular precio final
precio_final = compra * (1 - descuento / 100)

# Salidas
print("Descuento aplicado:", descuento, "%")

if envio_gratis:
    print("Envío gratis aplicado")

print("Total a pagar: $", int(precio_final))
