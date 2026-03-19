compra=int(input("ingrese el valor total de la compra:"))
if compra > 100000:
    precio_final= compra * 0.85
    print("descuento aplicando. total a pagar: $", precio_final)
else:
    print("sin descuento. total a pagar: $", compra)
