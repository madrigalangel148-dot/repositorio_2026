N = int(input("Ingresa un número: "))
suma = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        print("Número par:", i)
        suma += i  
print("La suma de los pares es:", suma)
