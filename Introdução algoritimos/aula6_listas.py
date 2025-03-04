#Listas
'''
Estruturas de dados dinâmicos
Podemos alterar dados e tamanhos
Indexadas por valores numéricos interios
Representadas em Python por colchetes[]
'''
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('tupla',mochila)
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('lista',mochila)

# Com a lista conseguimos alterar os dados como o exemplo a baixo:
mochila[2] = 'Laranja' # Susbstitui o bacon, lembrando que lista começa pelo 0 
print('lista',mochila)

# Podemos adicionar usando instruções:
mochila.append('Ovos') # Inseri o item indo para ultima posição da lista
print('lista',mochila)

# Inserir algum item na posição desejada
mochila.insert(1,'canivete') # aqui ele entra na posição  da camisa mas sem substituir ela 
print('lista',mochila)

del mochila[1] # deleta algum item na posição 1
print('lista',mochila)

mochila.remove('Ovos') # deleta o item informado 
print('lista',mochila)


# Copia de listas 
lista_original = [5,7,9,11]
lista_referenciada = lista_original
print(lista_original)
print(lista_referenciada)

# Alterando um dado
lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)
# Fazendo desta forma eu não altero o valor de uma lista porque, eu não estou criando um novo espaço na memoria 
# Porque a variaavel de referencia so serve como apontador

# Fazendo uma copia certa
lista_original = [5,7,9,11]
lista_referenciada = lista_original[:]# Dessa forma estou copiando a lista da forma correta, tambem posso fazer o ftiamento como de [0:2]
print(lista_original)
print(lista_referenciada)

# O que são metodos ?
'''
Uma lista é um objeto de uma classe dentro do python
Paradigmas de programação orientada a objetos (POO)
Metodo é equeivalnte a função 
    mochila.appended('Ovos)
    variavel.função(parâmetro)
'''