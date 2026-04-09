# pedir datos 
pasaporte=input("¿tienes pasaporte?(si/no):").lower()
visa=input("¿tienes visa? (si/no):").lower()
exento=input("¿tu pais esta exento de visa? (si/no):").lower()
# condicion convinada
if pasaporte=="si" and (visa=="si" or exento=="si"):
    print("puedes viajar. ¡buen viaje :) !")
else:
    print("no puedes viajar. revisa tus documentos")
