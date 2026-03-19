nota=float(input("ingrese la nota del estudiante(0.0 - 5.0:):"))
if nota>= 4.5:
    print("A - execelente | aprobado")
elif nota >=4.0:
    print("B - sobresaliente | aprobado")
elif nota>=3.5:
    print("C - bueno | aprobado")
elif nota >=3.0:
    print("D - acectable | aprobado")

else:
    if 2.0 <= nota <= 2.9:
        print("E - reprobado | puede presentar habilitacion")
    else:
        print("E - reprobado | sin derecho a habilitacion")
