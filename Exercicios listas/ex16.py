# 16. Criar uma lista de nomes e exibir apenas os nomes que começam com a letra A
Nomes = ['Ana', 'Lucia', ' Ariel', 'Ada', 'Joao', 'Gabrel', 'Alicia', 'Jessica'] # Variavel recebendo a lista                                                                              
for i in Nomes:
    if i.startswith("A"): #Exibe os nomes que iniciam com a letra A
        print(i)
