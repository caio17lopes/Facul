# Dicionários
'''
Estrutura de dados dinâmica
Podemos alterar dados e tamanho
Indexados por chaves (palvras-chave)
Representados em python por {} chaves
'''
# Exemplos

game = {'nome':'Super Mario', # O dado é nome e a palvara chave é Super mario
        'desenvolvedora' : 'Nitendo', # O dado é desenvolvedora e a palvra chave é nintendo
        'ano' : 1990} # O dado é ano e a palavra chave é  1990
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

# Metodos para dicionários
'''
values: obtém somente dados
keys: obtém somente as chaves 
items: obtem o par chave : dado
'''
print(game.values()) # Aqui eu pego apenas os valores finais ou seja os dados 

for values in game.values(): # Aqui eu pego apenas os valores finais ou seja os dados 
    print(values)

print(game.keys()) # Assim eu consigo apenas pegar as chaves

for keys in game.keys(): # Assim eu consigo apenas pegar as chaves
    print(keys)

print(game.itens()) # Fazendo assim consigo pegar a chaves e os dados 

for keys, values in game.items():
    print(f'{keys} = {values}') # Fazendo assim consigo pegar a chaves e os dados 

# Listas com dicionários
'''
Uma lista contendo, em cada índice, um dicionário
Vejamos em python
'''

games = []
game1 = {'nome':'Super Mario', 
        'desenvolvedora' : 'Nitendo', 
        'ano' : 1990}
game2 = {'nome':'Star WArs Battlefront II',
        'desenvolvedor':'EA Games',
        'ano' : 2004 }
game3 = {'nome':'Need For Speed Underground 2',
        'desenvolvedora':'EA Games',
        'ano': 2005}
games = [game1,game2,game3]
print(games)

# Fazendo a mesma implementação so que dinâmica

game = {}
games = []

for i in range(3):
    game['nome'] = input('Qual o nome do jogo: ')
    game['videogame'] = input('Para qual video-game ele foi lançado? ')
    game['ano'] = input('Qual o ano de lançamento? ')
    games.append(game.copy())
print('-' * 20)
for jogos in games:
    for chave,valor in jogos.items():
        print(f'O campo {chave} tem o valor {valor}')

# Dicionarios com listas

games = {'nome': ['Super Mario', 'Star Wars Battlefront 2', 'NFS2'],
        'video game': ['Nntendo 64', 'PS1','PS1'],
        'ano' : [1990,2004,2005]
        }
print(games)

# Fazendo a mesma implementação so que dinâmica

games = {'nome':[], 'videogame':[],'ano':[]}
for i in range(3):
    nome = input('Qual o nome do jogo? ')
    videogame = input('Para qual videogame foi lançado? ')
    ano = int(input('Digite o ano de lançamento: '))
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)