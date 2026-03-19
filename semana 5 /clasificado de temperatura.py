temp=int(input("ingrese la temperatura en °C:"))
if temp < 5:
    print("muy frio: usa ropa de invierno")
elif 5 <= temp <= 14:
    print("frio: usa chaqueta")
elif 15 <= temp <=24:
    print("templado: ropa comoda de diario")
elif 25 <= temp <= 34:
    print("caliente: usa ropa ligera")
else:
    print("muy caliente: hidratate bien")
