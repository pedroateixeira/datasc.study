limite_termos = 10
limite_valor = 100

text = f"""
{"=" * 10}
SEQUÊNCIA DE FIBONACCI
Limite de termos: {limite_termos}
Limite de valor: {limite_valor}
{"=" * 10}
"""
print(text)

n = int(input("quantos termos da sequencia de fibonacci voce deseja ver? "))

fibonacci = [0, 1]

for valor in range(2, n):
    proximo = fibonacci[valor - 1] + fibonacci[valor - 2]

    fibonacci.append(proximo)

print(fibonacci)


fibonacci_while = [0, 1]
indice = 2
while True:
    proximo = fibonacci_while[indice - 1] + fibonacci_while[indice - 2]
    if proximo > limite_valor:
        break
    fibonacci_while.append(proximo)
    indice = indice + 1

print(fibonacci_while)
