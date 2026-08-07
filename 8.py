# 8. Leia vários números até que o usuário digite 0.
# Ao final, informe a soma dos valores digitados.

soma = 0

numero = float(input("Informe um número: "))

while numero != 0:
    soma = soma + numero
    numero = float(input("Informe outro número: "))

print(f"A soma dos valores é {soma}.")