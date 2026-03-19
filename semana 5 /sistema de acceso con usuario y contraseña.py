usuario_correcto="admin"
clave_correcta="uniminuto2024"

for intento in range(3):
    usuario=input("ingrese usuario:")
    clave=input("ingrese contraseña:")

    if usuario == usuario_correcto:
        if clave == clave_correcta:
            print("acceso concedido.bienvenido, admin!")
            break
        else:
            print("contraseña incorrecta")
    else:
        print("usuario no encontrado")
else:
    print("se agotaron los intentos")
