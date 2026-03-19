# Entrada del usuario
usuario = input("Elige piedra, papel o tijera: ").lower()

# Elección de la computadora (según el ejercicio)
pc = "piedra"

# Validar entrada
if usuario != "piedra" and usuario != "papel" and usuario != "tijera":
    print("Opción inválida. Elige piedra, papel o tijera")

else:
    print("PC eligió:", pc)

    # Empate
    if usuario == pc:
        print("EMPATE")

    # Usuario gana
    elif (usuario == "papel" and pc == "piedra") or \
         (usuario == "piedra" and pc == "tijera") or \
         (usuario == "tijera" and pc == "papel"):
        print("GANASTE")
        
        if usuario == "papel":
            print("papel le gana a piedra")
        elif usuario == "piedra":
            print("piedra le gana a tijera")
        else:
            print("tijera le gana a papel")

    # Usuario pierde
    else:
        print("PERDISTE")
        
        if pc == "piedra":
            print("piedra le gana a tijera")
        elif pc == "papel":
            print("papel le gana a piedra")
        else:
            print("tijera le gana a papel")
