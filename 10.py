# 10. Leia 5 números e informe o maior e o menor valor.

numero = float(input("Informe o 1º número: "))

maior = numero
menor = numero

for i in range(2, 6):
    numero = float(input(f"Informe o {i}º número: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")