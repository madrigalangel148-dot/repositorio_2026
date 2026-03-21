#pedir el nombre del usuario 
#pedir el consumo de agua en m3
#convertir el consumo a numero entero
#si el consumo es mayor o igual a 0:
#mostrar mensaje de error
#si el consumo esta entre 1 y 15:
#mostrar "bajo consumo" y mensaje
#si el consumo esta entre 16 y 30:
#mostrar "consumo normal" y mensaje
#si el consumo es mayor a 30:
#mostrar "alto consumo" y mensaje

# pedir datos al usuario
nombre=input("ingrese nombre")
consumo=int(input("ingrese su consumo de agua en m3:"))

#validar consumo 
if consumo <=0:
    print("error el consumo debe mayor a 0")

elif consumo <=15:
    print(nombre,"bajo consumo")
    print("exelente eres un usuario que cuida el agua")

elif consumo <=30:
    print(nombre,"consumo normal")
    print("tu consumo esta dentro del promedio de tu casita")

else:
    print(nombre,"alto consumo")
    print("cuidado: tu consumo es alto, revisa alguna tuberia dañada")
