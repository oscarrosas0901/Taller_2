"""Dados tres números enteros, determinar cuál de ellos es el mayor"""

from cgi import print_form


print("--------------------------------------------")
print("--------------nunmero entero----------------")
print("--------------------------------------------")

N1 = int(input("perimer numero entero: "))
N2 = int(input("segundo numero entero: "))
N3 = int(input("tercer numero entero: "))

##N1 > N2, > N1 > N3
##N2 > N1, > N2 > N3
##N2 > N1, > N3 > N2

if N2 < N1 > N3:
    print("el numero mayor es el primer numero. Numero:", N1)
elif N1 < N2 > N3:
    print("el numero mayor es el segundo numero. Numer:", N2)
elif N1 < N3 > N2:
    print("el numero mayor es el tercer numero. Numero:", N3)
else:
    print("todos los numeros son iguales")