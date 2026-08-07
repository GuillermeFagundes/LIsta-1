# 1. Leia dois números e exiba a soma, subtração, multiplicação e divisão.

print("Este programa lê dois números e exibe a soma, a subtração, a multiplicação e a divisão.")

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2

print(f"A soma é {soma}")
print(f"A subtração é {subtracao}")
print(f"A multiplicação é {multiplicacao}")

if n2 != 0:
    divisao = n1 / n2
    print(f"A divisão é {divisao}")
else:
    print("Não é possível dividir por zero.")