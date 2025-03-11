# 7. Criar uma lista de strings e verificar quantas vezes uma palavra específica aparece.
lista = ["1","2","3","4","2","2","3","4","5","3","1"]
contagem = 0
for i in lista:
    if i == "2":  #Verifica quantas vezes o numero 2 aparece
        contagem +=1
print(contagem)