# Conversa inicial
'''
Estrutura de dados
    Tuplas ()
    Listas []
    Dicionários {}

Aprenderemos também 
    Conceito de método
    Métodos para string
'''
#Variáveis
'''
Simples: armazena um só dado
Composta: armazena um conjunto de dados

'''
# Estrutura de dados 
'''
É um conjunto de dados organizados de uma maneira especifica na memoria do programa
A maneira como os dados estão organizados na memória, como podem ser buscados,
manipulados e acessados, é o que define e diferencia as aestrutras de dados.
'''
# Tupla
'''
Estrutra de dados estática
A tupla é imutável
Repesentadad em python pelo parênteses()
'''
#Exemplo:
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

# Buscando na forma de indice:
print(mochila[0]) # print do elemento 1 - Índice 0 
print(mochila[2]) # print do elemento 3 - Índice 2
print(mochila[0:2]) # print do elemento 1 e 2 - Índice 0 e 1
print(mochila[2:]) # print dos elementos a partir do indice 2
print(mochila[-1]) # print do elemento 4 o ultimo de tras para frente

#mochila[2] = 'Ovos' # Da erro , tupla é imutavel!

# Varredura de item por item na tupla usando for

for item in mochila:
    print(f'Itens na mochila, {item}')

tam = len(mochila)
for i in range(0,tam,0):
    print(f'Itens na mochila {i}')

# Adicionando itens na tupla:
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo','Canivete')
mochila_grande = mochila + upgrade
print (mochila)
print(upgrade)
print(mochila_grande)

# modo invertido ]
mochila_grande_invertida = upgrade + mochila # É so adicionar o upgrade na frente da mochila que eles vm primeiro na lista 
print(mochila_grande)
print (mochila_grande_invertida)

#Desempacotamento de parÂmetros em funções
def soma(*num): # * em uma variavel dentro de uma função siginifica que ela é uma tupla
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador

#PRograma principal 
print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9)} \n')