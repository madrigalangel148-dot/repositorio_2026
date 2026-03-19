peso=float(input("ingrese su peso en kg:"))
altura=float(input("ingrese su altura en metros:"))
imc=peso/(altura ** 2)
imc=round(imc,2)
print("su IMC es:", imc)
if imc < 18.5:
    print("categoria: bajo peso")
elif imc <= 24.9:
    print("categoria: normal")
elif imc <= 29.9:
    print("categoria: sobrepeso")
else:
    print("categoria: obesidad")
