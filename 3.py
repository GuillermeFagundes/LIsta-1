# 3. Leia um número e informe se ele é positivo, negativo ou zero.

numero = float(input("Informe um número: "))

if numero > 0:
    print("Número positivo.")

elif numero == 0:
    print("Número igual a zero.")

else:
    print("Número negativo.")