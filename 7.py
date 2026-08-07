# 7. Leia 10 números e informe a soma e a média.

soma = 0

for i in range(1, 11):
    numero = float(input(f"Informe o {i}º número: "))
    soma = soma + numero

media = soma / 10

print(f"A soma é {soma}.")
print(f"A média é {media}.")