#Compreensão de listas 
'''
Permite criar uma nova lista a partir de uma expressão ou iteração em uma unica linha 
    Caso com somente uma condição 
'''
# Lista classica
lista_pares_quadrado =[]
for num in range(10):
    if num % 2 == 0:
        lista_pares_quadrado.append(num*num)
# Lista de forma otimizada de fazer 
lista_pares_quadrado = [num*num for num in range(10) if num %2 ==0]

# Caso com duas condições 

lista_pares_quadrado =[]
for num in range(10):
    if num % 2 == 0:
        lista_pares_quadrado.append(num*num)
    else: 
        lista_pares_quadrado.append('impar')
# criei uma nova lista / esses elementos/ se oebedecem a seguinte condição/ senão use esses elementos/ dentro do intervalo
lista_pares_quadrado = [num*num if num % 2 == 0 else 'impar' for num in range(10)]
print(lista_pares_quadrado)