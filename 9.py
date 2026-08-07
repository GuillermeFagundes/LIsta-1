# 9. Crie uma função que receba dois números e retorne o maior deles.

def maior_numero(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

maior = maior_numero(numero1, numero2)

print(f"O maior número é {maior}.")