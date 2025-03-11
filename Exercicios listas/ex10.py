# 10. Ordenar uma lista de números em ordem crescente e decrescente.
Numeros = [2, 1, 3, 4, 10, 6, 8, 9, 5, 7]
crescente = sorted(Numeros) #Coloca a lista na ordem
print("Ordem crescente:", crescente)
decrescente = sorted(Numeros, reverse=True) #Reverte a cresce para ficar decrescente
print("Ordem decrescente:", decrescente)