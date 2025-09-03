'''
Escreva um algoritimo que criei uma tupla com 10 palvras. Enconte dento dessa tuplaas vogais de cada palavra.
Faça um print na tela com o nome da palavra e suas respectivas vogais
'''
palavras = ('Mario','Luigi','Peach','Yoshi','Bowser')

for palavra in palavras:
    print(f'\nPalavra {palavra.upper()}. Vogais:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

