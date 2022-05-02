""""Programa para determinar si los dos ultimos digitos de un numero son iguales"""

print("----------------------------------------------")
print("---------- Ultimos digitos iguales -----------")
print("----------------------------------------------")

X = int(input("Ingrese un número: "))

M = int(str(X)[-1])
N = int(str(X)[-2])

if M == N:
    print("Los ultimos dos digitos de " + str(X) + " son iguales.")

else:
    print("Los ultimos dos digitos de " + str(X) + " no son iguales.")