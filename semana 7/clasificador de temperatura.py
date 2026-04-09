# pedir dato
temp=float(input("temperatura en grados celsius:"))
#evaluar rangos
if temp <0:
    print("bajo cero: te estas muriendo de frio")
elif temp >=0 and temp <15:
    print("fria")
elif temp >=15 and temp <=25:
    print("templada: temperatura ideal")
elif temp >25 and temp <=35:
    print("calida")
else:
    print("mucho calor")
