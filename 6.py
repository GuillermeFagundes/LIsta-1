# 6. Leia um número N e calcule a soma dos números de 1 até N.

n = int(input("Informe um número: "))

soma = 0

for i in range(1, n + 1):
    soma = soma + i

print(f"A soma dos números de 1 até {n} é {soma}.")