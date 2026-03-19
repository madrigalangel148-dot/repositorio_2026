anio=int(input("ingrese un año:"))
if(anio % 4 == 0 and anio % 100 !=0) or(anio % 400 == 0):
    print("el año", anio, "es bisiesto(366 dias)")
else:
    print("el año", anio,"no es bisiesto(365 dias)")
