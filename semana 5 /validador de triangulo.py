a= float(input("ingrese el lado A:"))
b= float(input("ingrese el lado b:"))
c= float(input("ingrese el lado c:"))

# verificar si forman un triangulo
if (a+b>c) and (a+c>b) and (b+c>a):
    # clasificacion del triangulo
    if a == b and b == c:
        print("triangulo equilatero")
    elif a == b or a == c or b == c:
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")
else:
    print("no forman un triangulo")
