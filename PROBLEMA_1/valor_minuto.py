"""tiempo de duración de una llamada telefónica y determinar la cantidad a pagar"""

print ("-------------------------------------------")
print ("-------Valor a pagar por minuto------------")
print ("-------------------------------------------")

X = int(input("Tiempo de la llamada en (minutos): "))

if X <= 3:
    print("La llamada tiene un costo de 300");
elif X > 3:
    Y = (((X * 50) + 150))
    print("La llamada tiene un costo de: " + str(Y))