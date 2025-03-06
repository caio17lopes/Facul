#Exercicio 1 
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas.count(7))# metodo rapido e simples para fazer a contagem sem criar um laço
print(notas)
# altera o ultimo valor da lista para 4
notas [-1] = 4
print(notas)
# encontrar a maior nota
print(max(notas)) # essa função acha o maior valor dentro da lista 

notas.sort() # organiza as notas por ordem 
print(notas)

# fazer a media das notas

print(sum(notas) / len(notas)) # usando para fazer a media. Sum soma tudo e depois os dividir por len que chega na media
