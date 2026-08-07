# 5. Leia um número inteiro e mostre sua tabuada de 1 a 10.

numero = int(input("Informe um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")